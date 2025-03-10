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

# Enhanced CSS for modern, professional PDF output with improved typography and layout
CUSTOM_CSS = r"""
    /* Page Setup with improved margins and sophisticated footer */
    @page {
        size: A4 portrait;
        margin: 2.2cm 2.5cm;
        @bottom-right {
            content: "Page " counter(page) " of " counter(pages);
            font-size: 9pt;
            color: #777;
            font-weight: 400;
            font-family: 'Inter', sans-serif;
            padding-right: 1em;
        }
        @bottom-left {
            content: string(document-title);
            font-size: 9pt;
            color: #777;
            font-weight: 400;
            font-family: 'Inter', sans-serif;
            padding-left: 1em;
            max-width: 60%;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
    }

    /* Modern web fonts for premium typography */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&display=swap');

    :root {
        --text-primary: #1f2937;
        --text-secondary: #4b5563;
        --accent-color: #2563eb;
        --border-light: #e5e7eb;
        --bg-light: #f9fafb;
        --code-bg: #f3f4f6;
        --heading-color: #111827;
        --quote-color: #4b5563;
        --link-color: #2563eb;
        --table-header-bg: #f3f4f6;
        --table-alt-bg: #f9fafb;
    }

    body {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 10.5pt;
        line-height: 1.6;
        color: var(--text-primary);
        margin: 0;
        padding: 0;
        font-feature-settings: "kern", "liga", "calt";
        font-weight: 400;
        text-rendering: optimizeLegibility;
        -webkit-font-smoothing: antialiased;
    }

    /* Use string() to capture document title for the footer */
    h1.document-title {
        string-set: document-title content();
    }

    /* Modern semantic sections with proper spacing */
    header, main, nav, footer {
        margin-bottom: 1.5em;
    }

    p {
        orphans: 3;
        widows: 3;
        margin-bottom: 1.2em;
        text-align: justify;
        hyphens: auto;
        line-height: 1.7;
    }

    /* Enhanced Cover Page with modern layout */
    .cover-page {
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 70vh;
        text-align: left;
        padding: 2.5cm 0;
    }
    .cover-title {
        font-size: 2.4em;
        color: var(--heading-color);
        font-weight: 700;
        margin-bottom: 0.8em;
        line-height: 1.2;
        letter-spacing: -0.02em;
    }
    .cover-author {
        font-size: 1.1em;
        color: var(--text-secondary);
        margin: 0.5em 0;
        font-weight: 500;
    }
    .cover-date {
        font-size: 1em;
        color: var(--text-secondary);
        margin-top: 0.3em;
        font-weight: 400;
    }
    .cover-line {
        width: 40px;
        height: 4px;
        background-color: var(--accent-color);
        margin: 2em 0;
    }

    /* Page break helpers */
    .page-break-after { page-break-after: always; }
    .page-break-before { page-break-before: always; }

    /* Modern heading typography */
    h1, h2, h3, h4, h5, h6 {
        color: var(--heading-color);
        margin-top: 1.8em;
        margin-bottom: 0.8em;
        line-height: 1.3;
        letter-spacing: -0.02em;
        font-weight: 600;
        page-break-after: avoid;
    }
    h1 { 
        font-size: 1.8em; 
        font-weight: 700;
    }
    h2 { 
        font-size: 1.5em; 
        border-bottom: 1px solid var(--border-light); 
        padding-bottom: 0.3em;
    }
    h3 { font-size: 1.3em; }
    h4 { font-size: 1.1em; }
    h5 { font-size: 1em; }
    h6 { font-size: 0.9em; text-transform: uppercase; letter-spacing: 0.05em; }

    /* Links with hover states and better styling */
    a {
        color: var(--link-color);
        text-decoration: none;
        border-bottom: 1px solid rgba(37, 99, 235, 0.2);
        transition: border-color 0.2s ease;
    }
    a:hover { 
        border-bottom-color: var(--link-color);
    }

    /* Better code blocks with modern monospace font */
    code {
        font-family: "IBM Plex Mono", "SFMono-Regular", Consolas, monospace;
        background-color: var(--code-bg);
        padding: 0.2em 0.4em;
        border-radius: 4px;
        font-size: 0.9em;
        font-weight: 500;
        color: #6366f1;
    }
    pre {
        background-color: var(--code-bg);
        padding: 1em 1.2em;
        border-radius: 6px;
        overflow-x: auto;
        margin: 1.5em 0;
        border: 1px solid var(--border-light);
    }
    pre code { 
        background-color: transparent; 
        padding: 0;
        color: var(--text-primary);
        font-weight: 400;
    }

    /* Modern blockquotes */
    blockquote {
        border-left: 3px solid var(--accent-color);
        padding: 0.8em 0 0.8em 1.5em;
        margin: 1.5em 0;
        background-color: rgba(37, 99, 235, 0.05);
        border-radius: 0 4px 4px 0;
        color: var(--quote-color);
        font-style: italic;
    }
    blockquote p:last-child {
        margin-bottom: 0;
    }

    /* Clean modern tables */
    table {
        border-collapse: separate;
        border-spacing: 0;
        width: 100%;
        margin: 1.5em 0;
        border: 1px solid var(--border-light);
        border-radius: 6px;
        overflow: hidden;
    }
    th, td {
        border: none;
        border-bottom: 1px solid var(--border-light);
        padding: 0.8em 1em;
        text-align: left;
    }
    tr:last-child td {
        border-bottom: none;
    }
    thead tr {
        background-color: var(--table-header-bg);
    }
    th { 
        font-weight: 600;
        color: var(--heading-color);
    }
    tbody tr:nth-child(even) { 
        background-color: var(--table-alt-bg);
    }

    /* Clean horizontal rule */
    hr {
        border: none;
        height: 1px;
        background-color: var(--border-light);
        margin: 2.5em 0;
    }

    /* Image improvements */
    img {
        max-width: 100%;
        height: auto;
        display: block;
        margin: 2em auto;
        border-radius: 6px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05), 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    figure {
        margin: 2em 0;
        text-align: center;
    }
    figcaption {
        font-size: 0.9em;
        color: var(--text-secondary);
        margin-top: 0.7em;
        font-style: italic;
    }

    /* Modern Table of Contents */
    .toc {
        background: var(--bg-light);
        border: 1px solid var(--border-light);
        border-radius: 8px;
        padding: 1.5em 2em;
        margin: 2em 0;
    }
    .toc-title {
        font-weight: 600;
        color: var(--heading-color);
        margin-bottom: 1em;
        font-size: 1.2em;
    }
    .toc ul { 
        list-style-type: none; 
        margin: 0; 
        padding: 0; 
    }
    .toc li { 
        margin: 0.7em 0;
        line-height: 1.4;
    }
    .toc a { 
        color: var(--text-secondary);
        text-decoration: none;
        border-bottom: none;
        transition: color 0.2s ease;
    }
    .toc a:hover { 
        color: var(--link-color);
    }
    .toc > ul > li > a {
        font-weight: 500;
    }
    .toc ul ul {
        padding-left: 1.5em;
    }
    .toc-page h1 {
        font-size: 1.8em;
        margin-bottom: 1.5em;
    }

    /* Lists with better spacing */
    ul, ol {
        padding-left: 1.8em;
        margin: 1.2em 0;
    }
    li {
        margin-bottom: 0.5em;
    }
    li > ul, li > ol {
        margin: 0.5em 0;
    }

    /* Definition lists */
    dl {
        margin: 1.5em 0;
    }
    dt {
        font-weight: 600;
        color: var(--heading-color);
        margin-top: 1em;
    }
    dd {
        margin-left: 1.5em;
        margin-top: 0.3em;
    }

    /* Callouts and notes */
    .note, .warning, .tip, .info {
        padding: 1em 1.5em;
        margin: 1.5em 0;
        border-radius: 6px;
        border-left: 4px solid;
    }
    .note {
        background-color: #f0f9ff;
        border-left-color: #0ea5e9;
    }
    .warning {
        background-color: #fff7ed;
        border-left-color: #f97316;
    }
    .tip {
        background-color: #f0fdf4;
        border-left-color: #10b981;
    }
    .info {
        background-color: #f5f3ff;
        border-left-color: #8b5cf6;
    }

    /* Footer styling */
    footer {
        border-top: 1px solid var(--border-light);
        padding-top: 1.5em;
        margin-top: 3em;
        color: var(--text-secondary);
        font-size: 0.9em;
    }

    /* Prevent page breaks inside critical elements */
    li, dt, dd, tr, figure {
        page-break-inside: avoid;
    }

    /* Print-specific optimizations */
    @media print {
        body { font-size: 10pt; }
        a { border-bottom: none; }
        
        /* Ensure URLs are printed for links if desired */
        a[href^="http"]:after {
            content: " (" attr(href) ")";
            font-size: 0.9em;
            color: var(--text-secondary);
            font-style: italic;
        }
        
        /* Hide non-essential decorative elements */
        .cover-line {
            display: none;
        }
    }
"""

def parse_markdown_metadata(content: str):
    """
    Extract comprehensive metadata from the first lines of the Markdown file.
    Supports title, author, date, organization, version, status, and tags.
    """
    lines = content.split('\n')
    meta = {}
    new_lines = []
    
    # Track which metadata we've found
    found_metadata = {
        'title': False,
        'author': False, 
        'date': False,
        'organization': False,
        'version': False,
        'status': False,
        'tags': False
    }
    
    # Process header section
    in_metadata_section = True
    
    for line in lines:
        stripped = line.strip()
        
        # Title is usually the first heading
        if not found_metadata['title'] and stripped.startswith('# '):
            meta['title'] = stripped[2:].strip()
            found_metadata['title'] = True
            continue
            
        # Check for metadata in format: **Key:** Value or **Key**: Value
        metadata_match = re.match(r'^\*\*([\w\s]+)[:]\*\*\s*(.+)$', stripped)
        if metadata_match:
            key = metadata_match.group(1).lower().strip()
            value = metadata_match.group(2).strip()
            
            if key == 'author' and not found_metadata['author']:
                meta['author'] = value
                found_metadata['author'] = True
                continue
            elif key == 'date' and not found_metadata['date']:
                meta['date'] = value
                found_metadata['date'] = True
                continue
            elif key == 'organization' and not found_metadata['organization']:
                meta['organization'] = value
                found_metadata['organization'] = True
                continue
            elif key == 'version' and not found_metadata['version']:
                meta['version'] = value
                found_metadata['version'] = True
                continue
            elif key == 'status' and not found_metadata['status']:
                meta['status'] = value
                found_metadata['status'] = True
                continue
            elif key == 'tags' and not found_metadata['tags']:
                meta['tags'] = value
                found_metadata['tags'] = True
                continue
        
        # Alternative metadata format check: Key: Value
        alt_metadata_match = re.match(r'^([\w\s]+)[:]\s*(.+)$', stripped)
        if alt_metadata_match and in_metadata_section:
            key = alt_metadata_match.group(1).lower().strip()
            value = alt_metadata_match.group(2).strip()
            
            if key == 'author' and not found_metadata['author']:
                meta['author'] = value
                found_metadata['author'] = True
                continue
            elif key == 'date' and not found_metadata['date']:
                meta['date'] = value
                found_metadata['date'] = True
                continue
            elif key == 'organization' and not found_metadata['organization']:
                meta['organization'] = value
                found_metadata['organization'] = True
                continue
            elif key == 'version' and not found_metadata['version']:
                meta['version'] = value
                found_metadata['version'] = True
                continue
            elif key == 'status' and not found_metadata['status']:
                meta['status'] = value
                found_metadata['status'] = True
                continue
            elif key == 'tags' and not found_metadata['tags']:
                meta['tags'] = value
                found_metadata['tags'] = True
                continue
                
        # If we encounter an empty line followed by a non-metadata line,
        # we're likely exiting the metadata section
        if not stripped:
            in_metadata_section = False
        elif not any(found_metadata.values()) and not stripped.startswith('#'):
            # If we haven't found any metadata yet and this isn't a heading,
            # we're likely not in a metadata section
            in_metadata_section = False
            
        # Add the line to our content
        new_lines.append(line)
    
    cleaned_content = '\n'.join(new_lines)
    return meta, cleaned_content

def build_cover_page(meta):
    """
    Create an HTML cover page using extracted metadata with modern design.
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
    
    # If we have a title, mark it as document-title for the footer
    title_block = f'<h1 class="cover-title document-title">{title}</h1>' if title else ""
    author_block = f'<div class="cover-author">{author}</div>' if author else ""
    
    # Add company/organization name if available
    organization = meta.get('organization', '')
    org_block = f'<div class="cover-organization">{organization}</div>' if organization else ""
    
    cover_html = f"""
    <div class="cover-page">
      {title_block}
      <div class="cover-line"></div>
      {author_block}
      {org_block}
      {date_block}
    </div>
    <div class="page-break-after"></div>
    """
    return cover_html

def separate_table_of_contents(html_content):
    """
    Extract a TOC block (if present) from the HTML and build a separate enhanced TOC page.
    """
    toc_pattern = re.compile(r'(<div class="toc">.*?</div>)', re.DOTALL)
    match = toc_pattern.search(html_content)
    if not match:
        return html_content, ""
        
    toc_html = match.group(1)
    modified_html = toc_pattern.sub('', html_content, count=1)
    
    # Add a proper title to the TOC
    toc_page = f"""
    <div class="toc-page">
      <h1>Table of Contents</h1>
      <div class="toc-title">Document Sections</div>
      {toc_html}
    </div>
    <div class="page-break-after"></div>
    """
    return modified_html, toc_page

def convert_markdown_to_pdf(input_path: Path, output_path: Path = None) -> None:
    """
    Convert the provided Markdown file to a professionally formatted PDF with
    modern typography, layout, and design.
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

        # Replace custom page-break markers with our HTML marker
        markdown_content = markdown_content.replace('[PAGEBREAK]', '<div class="page-break-after"></div>')
        markdown_content = markdown_content.replace('<!-- pagebreak -->', '<div class="page-break-after"></div>')
        
        # Add support for note, warning, tip, and info blocks
        # Format: ::: note|warning|tip|info ... :::
        def replace_callout(match):
            callout_type = match.group(1).lower()
            content = match.group(2)
            return f'<div class="{callout_type}">{content}</div>'
            
        markdown_content = re.sub(r':::\s*(note|warning|tip|info)(.*?):::', 
                                replace_callout, 
                                markdown_content, 
                                flags=re.DOTALL)

        # Convert Markdown to HTML with enhanced extensions
        md = markdown.Markdown(
            extensions=[
                'markdown.extensions.tables',
                'markdown.extensions.fenced_code',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
                'markdown.extensions.sane_lists',
                'markdown.extensions.attr_list',  # Add support for attributes
                'markdown.extensions.def_list',   # Add support for definition lists
                'markdown.extensions.footnotes',  # Add support for footnotes
                'markdown.extensions.md_in_html', # Allow markdown in HTML
                'markdown.extensions.nl2br'       # Convert newlines to <br>
            ]
        )
        html_body = md.convert(markdown_content)
        
        # Process version and status if available
        version_status_html = ""
        if 'version' in meta or 'status' in meta:
            version = meta.get('version', '')
            status = meta.get('status', '')
            
            version_html = f'<span class="doc-version">Version: {version}</span>' if version else ''
            status_html = f'<span class="doc-status">Status: {status}</span>' if status else ''
            
            if version or status:
                version_status_html = f"""
                <div class="doc-metadata">
                    {version_html}
                    {status_html}
                </div>
                """

        # Build enhanced cover page from metadata
        cover_html = build_cover_page(meta)

        # Extract and enhance table of contents if present
        remaining_html, toc_html = separate_table_of_contents(html_body)
        
        # Add automatic figure and table numbering
        figure_count = 0
        
        def number_figures(match):
            nonlocal figure_count
            figure_count += 1
            img_tag = match.group(1)
            caption = match.group(2)
            
            return f'<figure>{img_tag}<figcaption>Fig {figure_count}: {caption}</figcaption></figure>'
            
        # Add numbering to image captions (format: ![alt](src "caption"))
        remaining_html = re.sub(r'<img([^>]*)alt="([^"]*)"([^>]*)>',
                              r'<img\1alt="\2"\3><figcaption>\2</figcaption>',
                              remaining_html)

        # Combine final HTML using semantic elements with enhanced structure
        html_document = f"""
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{meta.get('title') or input_path.stem}</title>
          </head>
          <body>
            <header>
              {cover_html}
            </header>
            <nav>
              {toc_html}
              {version_status_html}
            </nav>
            <main>
              {remaining_html}
            </main>
            <footer>
              <p>
                {meta.get('organization', '')}
                {f" • {meta.get('author', '')}" if meta.get('author') else ""}
                {f" • Generated on {datetime.now().strftime('%d %B %Y')}" if meta.get('date') else ""}
              </p>
            </footer>
          </body>
        </html>
        """
        
        # Configure font handling
        font_config = FontConfiguration()
        
        # Enable better hyphenation if pyphen is available
        try:
            import pyphen
            logger.info("Using pyphen for improved hyphenation")
        except ImportError:
            logger.info("Pyphen not available, using default hyphenation")
        
        logger.info(f"Converting to PDF: {output_path}")
        HTML(string=html_document, base_url=str(input_path.parent)).write_pdf(
            output_path,
            stylesheets=[CSS(string=CUSTOM_CSS)],
            font_config=font_config,
            optimize_size=('fonts', 'images'),  # Optimize PDF size
            presentational_hints=True
        )
        logger.info(f"Successfully created PDF: {output_path}")
    except Exception as e:
        logger.error(f"Error converting markdown to PDF: {str(e)}")
        raise

def main():
    """
    Command line interface for markdown to PDF conversion.
    
    Usage: python md_pdf.py input.md [output.pdf]
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert Markdown to beautifully formatted PDF')
    parser.add_argument('input_file', type=str, help='Path to the input markdown file')
    parser.add_argument('output_file', type=str, nargs='?', help='Path to the output PDF file (optional)')
    parser.add_argument('--paper-size', type=str, default='A4',
                        choices=['A4', 'A5', 'Letter', 'Legal'],
                        help='Paper size for the PDF (default: A4)')
    parser.add_argument('--debug', action='store_true', help='Enable debug logging')
    
    args = parser.parse_args()
    
    # Configure more detailed logging if debug mode is on
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.setLevel(logging.DEBUG)
    
    input_path = Path(args.input_file)
    output_path = Path(args.output_file) if args.output_file else None
    
    try:
        if args.paper_size != 'A4':
            # Modify CSS for different paper sizes
            global CUSTOM_CSS
            CUSTOM_CSS = CUSTOM_CSS.replace('size: A4 portrait;', f'size: {args.paper_size} portrait;')
            logger.info(f"Using paper size: {args.paper_size}")
            
        convert_markdown_to_pdf(input_path, output_path)
        logger.info(f"PDF conversion successful")
    except Exception as e:
        logger.error(f"Conversion failed: {str(e)}")
        if args.debug:
            import traceback
            logger.debug(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main()