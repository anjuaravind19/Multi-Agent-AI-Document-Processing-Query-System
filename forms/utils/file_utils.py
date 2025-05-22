"""import os

UPLOAD_DIR = "uploads"

def save_uploaded_file(uploaded_file, prefix="file"):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    filename = f"{prefix}_{uploaded_file.name}"
    filepath = os.path.join(UPLOAD_DIR, filename)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return filepath
"""

import os
from pathlib import Path

UPLOAD_DIR = Path(__file__).resolve().parent.parent.parent / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

def save_uploaded_file(uploaded_file, prefix):
    file_path = UPLOAD_DIR / f"{prefix}_{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return str(file_path)