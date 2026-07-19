"""
===========================================
Utility Functions
===========================================
Reusable helper functions used across the
Portfolio AI project.
Author: Shobhit
"""
from pathlib import Path
from typing import Dict
import hashlib
# ==========================================
# Category
# ==========================================
def get_category(filepath: str) -> str:
    """
    Extract the folder name.
    Example:
    --------
    data/projects/autismscope.txt
    Returns
    -------
    projects
    """
    path = Path(filepath)
    if path.parent.name == "data":
        return "general"
    return path.parent.name
# ==========================================
# Filename
# ==========================================
def get_filename(filepath: str) -> str:
    """
    Returns only the filename.
    Example
    -------
    data/projects/autismscope.txt
    Returns
    autismscope.txt
    """
    return Path(filepath).name
# ==========================================
# File Extension
# ==========================================
def get_extension(filepath: str) -> str:
    """
    Returns file extension.
    Example
    resume.pdf
    returns
    .pdf
    """
    return Path(filepath).suffix.lower()
# ==========================================
# Unique Document ID
# ==========================================
def generate_document_id(filepath: str) -> str:
    """
    Generate a unique ID using SHA256.
    Useful for logging, caching,
    tracking retrieved documents.
    """
    return hashlib.sha256(
        filepath.encode()
    ).hexdigest()
# ==========================================
# Source Information
# ==========================================
def build_source_metadata(file_path):
    path = Path(file_path)
    filename = path.name
    category = path.parent.name
    title = path.stem.replace("_", " ").title()
    return {
        "title": title,
        "category": category.title(),
        "filename": filename,
        "source": str(path)
    }
# ==========================================
# Pretty Print Sources
# ==========================================
def format_source(metadata: Dict) -> str:
    """
    Nicely formats metadata.
    Example
    [projects]
    autismscope.txt
    """
    return (
        f"[{metadata['category']}] "
        f"{metadata['filename']}"
    )
# ==========================================
# Validate Dataset Folder
# ==========================================
def validate_dataset(path: str) -> bool:
    """
    Check whether dataset exists.
    Raises
    ------
    FileNotFoundError
    """
    dataset = Path(path)
    if not dataset.exists():
        raise FileNotFoundError(
            f"Dataset not found:\n{dataset}"
        )
    return True
# ==========================================
# Count Files
# ==========================================
def count_files(path: str) -> int:
    """
    Counts every file recursively.
    Example
    data/
    returns
    42
    """
    dataset = Path(path)
    return len(list(dataset.rglob("*.*")))
# ==========================================
# Human Readable Size
# ==========================================
def human_size(size: int) -> str:
    """
    Convert bytes to KB/MB.
    Example
    2048
    returns
    2.00 KB
    """
    units = ["B", "KB", "MB", "GB"]
    index = 0
    while size >= 1024 and index < len(units)-1:
        size /= 1024
        index += 1
    return f"{size:.2f} {units[index]}"