"""
Utility for organizing data files according to the repository structure.
"""

import os
import shutil
import logging
from pathlib import Path
from typing import List, Optional, Dict

from src.config.settings import (
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    GOLD_DATA_DIR
)

logger = logging.getLogger(__name__)

def organize_files(
    source_dir: Path,
    target_dir: Path,
    file_patterns: List[str] = ["*"],
    recursive: bool = False,
    create_subdirs: bool = True,
    copy_not_move: bool = True
) -> Dict[str, int]:
    """
    Organize files from a source directory to a target directory.
    
    Args:
        source_dir (Path): Source directory containing files to organize
        target_dir (Path): Target directory where files will be placed
        file_patterns (List[str], optional): List of glob patterns to match files
        recursive (bool, optional): Whether to search directories recursively
        create_subdirs (bool, optional): Whether to create subdirectories in target
        copy_not_move (bool, optional): If True, copy files; if False, move files
    
    Returns:
        Dict[str, int]: Statistics on files processed
    """
    source_dir = Path(source_dir)
    target_dir = Path(target_dir)
    
    if not source_dir.exists():
        raise FileNotFoundError(f"Source directory does not exist: {source_dir}")
    
    # Create target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)
    
    # Initialize statistics
    stats = {
        "files_found": 0,
        "files_copied": 0,
        "files_moved": 0,
        "errors": 0
    }
    
    # Process each file pattern
    for pattern in file_patterns:
        if recursive:
            # Use rglob for recursive search
            matched_files = list(source_dir.rglob(pattern))
        else:
            # Use glob for non-recursive search
            matched_files = list(source_dir.glob(pattern))
        
        stats["files_found"] += len(matched_files)
        
        # Process each matched file
        for source_file in matched_files:
            if source_file.is_file():
                try:
                    # Determine target path
                    if create_subdirs:
                        # Create same subdirectory structure in target
                        rel_path = source_file.relative_to(source_dir)
                        target_file = target_dir / rel_path
                    else:
                        # Just put all files in the target directory
                        target_file = target_dir / source_file.name
                    
                    # Create target parent directory if it doesn't exist
                    os.makedirs(target_file.parent, exist_ok=True)
                    
                    # Copy or move the file
                    if copy_not_move:
                        shutil.copy2(source_file, target_file)
                        logger.info(f"Copied: {source_file} -> {target_file}")
                        stats["files_copied"] += 1
                    else:
                        shutil.move(source_file, target_file)
                        logger.info(f"Moved: {source_file} -> {target_file}")
                        stats["files_moved"] += 1
                        
                except Exception as e:
                    logger.error(f"Error processing {source_file}: {str(e)}")
                    stats["errors"] += 1
    
    # Log summary
    total_processed = stats["files_copied"] + stats["files_moved"]
    logger.info(f"Processing complete. Found {stats['files_found']} files, "
                f"processed {total_processed}, "
                f"errors: {stats['errors']}")
    
    return stats

def organize_data_directory(
    data_root: Optional[Path] = None, 
    document_patterns: List[str] = ["*.md", "*.pdf", "*.docx"],
    financial_patterns: List[str] = ["*.xlsx", "*.csv", "*.json"],
    legal_patterns: List[str] = ["*contract*", "*agreement*", "*legal*"]
) -> Dict[str, int]:
    """
    Organize files in the data directory according to their type.
    
    Args:
        data_root (Path, optional): Root directory for data.
            Defaults to the data directory from settings.
        document_patterns (List[str], optional): Patterns for document files
        financial_patterns (List[str], optional): Patterns for financial files
        legal_patterns (List[str], optional): Patterns for legal files
    
    Returns:
        Dict[str, int]: Statistics on files processed
    """
    if data_root is None:
        data_root = Path(__file__).parent.parent.parent / "data"
    
    data_root = Path(data_root)
    old_data_dir = data_root
    
    # Check for old data directory structure
    old_documents_dir = old_data_dir / "documents"
    old_financial_dir = old_data_dir / "financial"
    old_legal_dir = old_data_dir / "legal"
    
    # Define new directory structure
    raw_documents_dir = RAW_DATA_DIR / "documents"
    raw_financial_dir = RAW_DATA_DIR / "financial"
    raw_legal_dir = RAW_DATA_DIR / "legal"
    
    # Initialize statistics
    total_stats = {
        "files_found": 0,
        "files_copied": 0,
        "files_moved": 0,
        "errors": 0
    }
    
    # Organize document files
    if old_documents_dir.exists():
        logger.info(f"Organizing document files from {old_documents_dir} to {raw_documents_dir}")
        stats = organize_files(
            source_dir=old_documents_dir,
            target_dir=raw_documents_dir,
            file_patterns=document_patterns,
            recursive=True,
            create_subdirs=True,
            copy_not_move=True
        )
        # Update total stats
        for key in total_stats:
            total_stats[key] += stats[key]
    
    # Organize financial files
    if old_financial_dir.exists():
        logger.info(f"Organizing financial files from {old_financial_dir} to {raw_financial_dir}")
        stats = organize_files(
            source_dir=old_financial_dir,
            target_dir=raw_financial_dir,
            file_patterns=financial_patterns,
            recursive=True,
            create_subdirs=True,
            copy_not_move=True
        )
        # Update total stats
        for key in total_stats:
            total_stats[key] += stats[key]
    
    # Organize legal files
    if old_legal_dir.exists():
        logger.info(f"Organizing legal files from {old_legal_dir} to {raw_legal_dir}")
        stats = organize_files(
            source_dir=old_legal_dir,
            target_dir=raw_legal_dir,
            file_patterns=legal_patterns,
            recursive=True,
            create_subdirs=True,
            copy_not_move=True
        )
        # Update total stats
        for key in total_stats:
            total_stats[key] += stats[key]
    
    # Check root directory for unorganized files
    logger.info(f"Looking for unorganized files in {data_root}")
    
    # Organize document files in root
    stats = organize_files(
        source_dir=data_root,
        target_dir=raw_documents_dir,
        file_patterns=document_patterns,
        recursive=False,
        create_subdirs=False,
        copy_not_move=True
    )
    # Update total stats
    for key in total_stats:
        total_stats[key] += stats[key]
    
    # Organize financial files in root
    stats = organize_files(
        source_dir=data_root,
        target_dir=raw_financial_dir,
        file_patterns=financial_patterns,
        recursive=False,
        create_subdirs=False,
        copy_not_move=True
    )
    # Update total stats
    for key in total_stats:
        total_stats[key] += stats[key]
    
    # Log overall summary
    logger.info(f"Data organization complete. "
                f"Total files found: {total_stats['files_found']}, "
                f"Total files copied: {total_stats['files_copied']}, "
                f"Total errors: {total_stats['errors']}")
    
    return total_stats

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # Run data organization
    organize_data_directory()