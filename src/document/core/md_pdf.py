import os
from pathlib import Path
import logging
import sys
import markdown
import re
from datetime import datetime
import locale

from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Enhanced CSS including print media rules, semantic styling, and improved page-break handling
CUSTOM_CSS = r"""
    /* Page Setup */
    @page {
        size: A4 portrait;
        margin: 2.5cm 2cm;
        @bottom-center {
            content: "Page " counter(page) " of " counter(pages);
            font-size: 9pt;
            color: #999;
        }
    }

    /* Import a clean sans-serif font */
    @import url('https://api.fontshare.com/v2/css?f[]=general-sans@500,600,400&display=swap');

    body {
        font-family: 'General Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        font-size: 11pt;
        line-height: 1.6;
        color: #333;
        margin: 0;
        padding: 0;
        font-feature-settings: "ss01" 1, "ss02" 1, "ss03" 1;
    }

    /* Semantic sections for improved structure */
    header, main, nav, footer {
        margin-bottom: 1em;
    }

    p {
        orphans: 2;
        widows: 2;
        margin-bottom: 1em;
        text-align: justify;
    }

    /* Cover Page Styling */
    .cover-page {
        text-align: center;
        margin-top: 100px;
        margin-bottom: 2em;
    }
    .cover-title {
        font-size: 2em;
        color: #2c3e50;
        font-weight: 600;
        margin-bottom: 0.1em;
        border-bottom: 1px solid #eee;
        display: inline-block;
        padding-bottom: 0.3em;
        letter-spacing: -0.02em;
    }
    .cover-author, .cover-date {
        font-size: 1em;
        color: #666;
        margin: 0.3em 0;
        font-weight: 500;
    }

    /* Page break helpers */
    .page-break-after { page-break-after: always; }
    .page-break-before { page-break-before: always; }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #2c3e50;
        margin-top: 1.4em;
        margin-bottom: 0.6em;
        line-height: 1.25;
        letter-spacing: -0.02em;
    }
    h1 { font-size: 1.8em; }
    h2 { font-size: 1.6em; border-bottom: 1px solid #eee; padding-bottom: 0.2em; }
    h3 { font-size: 1.4em; }
    h4 { font-size: 1.2em; }

    /* Links */
    a {
        color: #0072b1;
        text-decoration: none;
    }
    a:hover { text-decoration: underline; }

    /* Code blocks */
    code {
        font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
        background-color: #f8f8f8;
        padding: 0.2em 0.4em;
        border-radius: 3px;
        font-size: 0.9em;
    }
    pre {
        background-color: #f8f8f8;
        padding: 1em;
        border-radius: 5px;
        overflow-x: auto;
        margin: 1em 0;
    }
    pre code { background-color: transparent; padding: 0; }

    /* Blockquotes */
    blockquote {
        border-left: 4px solid #ddd;
        padding-left: 1em;
        color: #666;
        margin: 1em 0;
    }

    /* Tables */
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 1em 0;
    }
    th, td {
        border: 1px solid #ddd;
        padding: 0.6em;
        text-align: left;
    }
    th { background-color: #f1f1f1; }
    tr:nth-child(even) { background-color: #f9f9f9; }

    hr {
        border: none;
        border-top: 1px solid #ddd;
        margin: 2em 0;
    }

    /* Images */
    img {
        max-width: 100%;
        height: auto;
        display: block;
        margin: 1em auto;
    }

    /* Table of Contents */
    .toc {
        background: #fafafa;
        border: 1px solid #eee;
        padding: 1em;
        margin: 1em 0;
        border-radius: 5px;
    }
    .toc ul { list-style-type: none; margin: 0; padding: 0; }
    .toc li { margin: 0.5em 0; }
    .toc a { color: #0072b1; text-decoration: none; }
    .toc a:hover { text-decoration: underline; }

    /* Prevent page breaks inside critical elements */
    h1, h2, h3, h4, p, blockquote, table, pre {
        page-break-inside: avoid;
    }

    /* Print media tweaks */
    @media print {
        body { font-size: 10pt; margin: 1cm; }
    }
"""

def parse_markdown_metadata(content: str):
    """
    Extract title, author, and date from the first lines of the Markdown file.
    """
    lines = content.split('\n')
    meta = {}
    new_lines = []
    found_title = found_author = found_date = False

    for line in lines:
        stripped = line.strip()
        if not found_title and stripped.startswith('# '):
            meta['title'] = stripped[2:].strip()
            found_title = True
            continue
        if not found_author and stripped.lower().startswith('**author:**'):
            author_part = stripped.split(':', 1)[1].strip().strip('*')
            meta['author'] = author_part
            found_author = True
            continue
        if not found_date and stripped.lower().startswith('**date:**'):
            date_part = stripped.split(':', 1)[1].strip().strip('*')
            meta['date'] = date_part
            found_date = True
            continue
        new_lines.append(line)
    cleaned_content = '\n'.join(new_lines)
    return meta, cleaned_content

def build_cover_page(meta):
    """
    Create an HTML cover page using extracted metadata.
    """
    title = meta.get('title', '')
    author = meta.get('author', '')
    date_str = meta.get('date', '')
    date_block = ""
    if date_str:
        try:
            try:
                locale.setlocale(locale.LC_TIME, 'nl_NL.UTF-8')
            except Exception:
                try:
                    locale.setlocale(locale.LC_TIME, 'nl_NL')
                except Exception:
                    pass
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            formatted_date = date_obj.strftime("%d %B %Y")
            date_block = f'<div class="cover-date">{formatted_date}</div>'
        except Exception:
            date_block = f'<div class="cover-date">{date_str}</div>'
    title_block = f'<div class="cover-title">{title}</div>' if title else ""
    author_block = f'<div class="cover-author">{author}</div>' if author else ""
    cover_html = f"""
    <div class="cover-page">
      {title_block}
      {author_block}
      {date_block}
    </div>
    <div class="page-break-after"></div>
    """
    return cover_html

def separate_table_of_contents(html_content):
    """
    Extract a TOC block (if present) from the HTML and build a separate TOC page.
    """
    toc_pattern = re.compile(r'(<div class="toc">.*?</div>)', re.DOTALL)
    match = toc_pattern.search(html_content)
    if not match:
        return html_content, ""
    toc_html = match.group(1)
    modified_html = toc_pattern.sub('', html_content, count=1)
    toc_page = f"""
    <div class="toc-page">
      <h1>Table of Contents</h1>
      {toc_html}
    </div>
    <div class="page-break-after"></div>
    """
    return modified_html, toc_page

def convert_markdown_to_pdf(input_path: Path, output_path: Path = None) -> None:
    """
    Convert the provided Markdown file to a PDF with enhanced formatting.
    """
    try:
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")
        if output_path is None:
            output_path = input_path.with_suffix('.pdf')
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"Reading markdown file: {input_path}")
        raw_content = input_path.read_text(encoding='utf-8')

        # Parse metadata and remove those lines from content
        meta, markdown_content = parse_markdown_metadata(raw_content)

        # Replace custom page-break marker with our HTML marker
        markdown_content = markdown_content.replace('[PAGEBREAK]', '<div class="page-break-after"></div>')

        # Convert Markdown to HTML with helpful extensions, including nl2br for newlines
        md = markdown.Markdown(
            extensions=[
                'markdown.extensions.tables',
                'markdown.extensions.fenced_code',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
                'markdown.extensions.sane_lists',
                'markdown.extensions.nl2br'
            ]
        )
        html_body = md.convert(markdown_content)

        # Build cover page from metadata
        cover_html = build_cover_page(meta)

        # Extract table of contents if present
        remaining_html, toc_html = separate_table_of_contents(html_body)

        # Combine final HTML using semantic elements
        html_document = f"""
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <title>{meta.get('title') or input_path.stem}</title>
          </head>
          <body>
            <header>
              {cover_html}
            </header>
            <nav>
              {toc_html}
            </nav>
            <main>
              {remaining_html}
            </main>
            <footer>
              <p style="text-align:center; font-size:9pt; color:#999;">Page footer if needed</p>
            </footer>
          </body>
        </html>
        """
        font_config = FontConfiguration()
        logger.info(f"Converting to PDF: {output_path}")
        HTML(string=html_document, base_url=str(input_path.parent)).write_pdf(
            output_path,
            stylesheets=[CSS(string=CUSTOM_CSS)],
            font_config=font_config
        )
        logger.info(f"Successfully created PDF: {output_path}")
    except Exception as e:
        logger.error(f"Error converting markdown to PDF: {str(e)}")
        raise

def main():
    if len(sys.argv) < 2:
        logger.error("Please provide the path to the markdown file")
        sys.exit(1)
    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    try:
        convert_markdown_to_pdf(input_path, output_path)
    except Exception as e:
        logger.error(f"Conversion failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()