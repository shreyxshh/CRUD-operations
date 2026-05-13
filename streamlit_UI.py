import streamlit as st
from pathlib import Path
import os

st.set_page_config(page_title="File CRUD Manager", page_icon="📁", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #0f0f1a; }
    .main-title { color: #00d4aa; font-family: 'Courier New', monospace; font-size: 2rem; font-weight: bold; }
    .section-header { color: #a0c4ff; font-family: 'Courier New', monospace; }
    .success-box { background: #0d3320; border-left: 4px solid #00d4aa; padding: 10px 16px; border-radius: 4px; color: #00d4aa; font-family: monospace; }
    .error-box   { background: #3a0d0d; border-left: 4px solid #e74c3c; padding: 10px 16px; border-radius: 4px; color: #e74c3c; font-family: monospace; }
    .info-box    { background: #0d1f3a; border-left: 4px solid #a0c4ff; padding: 10px 16px; border-radius: 4px; color: #a0c4ff; font-family: monospace; }
    .file-item   { color: #ccc; font-family: monospace; padding: 2px 0; }
    div[data-testid="stSelectbox"] label { color: #a0c4ff !important; }
    div[data-testid="stTextInput"]  label { color: #a0c4ff !important; }
    div[data-testid="stTextArea"]   label { color: #a0c4ff !important; }
    div[data-testid="stRadio"]      label { color: #a0c4ff !important; }
</style>
""", unsafe_allow_html=True)


# ── Helpers ──────────────────────────────────────────────────────────────────

def get_all_items():
    p = Path(".")
    return sorted([str(i) for i in p.rglob("*") if str(i) != "."])

def show_success(msg): st.markdown(f'<div class="success-box">✓ &nbsp;{msg}</div>', unsafe_allow_html=True)
def show_error(msg):   st.markdown(f'<div class="error-box">✗ &nbsp;{msg}</div>', unsafe_allow_html=True)
def show_info(msg):    st.markdown(f'<div class="info-box">ℹ &nbsp;{msg}</div>', unsafe_allow_html=True)


# ── Layout ────────────────────────────────────────────────────────────────────

st.markdown('<p class="main-title">📁 File CRUD Manager</p>', unsafe_allow_html=True)
st.markdown("---")

left_col, right_col = st.columns([1, 2])

# ── Left: Explorer ────────────────────────────────────────────────────────────
with left_col:
    st.markdown('<p class="section-header">🗂 Explorer</p>', unsafe_allow_html=True)
    items = get_all_items()
    if items:
        for item in items:
            icon = "📁" if Path(item).is_dir() else "📄"
            st.markdown(f'<div class="file-item">{icon} {item}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="file-item" style="color:#555">( empty )</div>', unsafe_allow_html=True)

    st.markdown("")
    if st.button("⟳ Refresh Explorer", use_container_width=True):
        st.rerun()

# ── Right: Operations ─────────────────────────────────────────────────────────
with right_col:
    st.markdown('<p class="section-header">⚙ Operations</p>', unsafe_allow_html=True)

    operation = st.selectbox(
        "Select Operation",
        [
            "📄 Create File",
            "👁 Read File",
            "✏️ Update File (Overwrite)",
            "➕ Update File (Append)",
            "🗑 Delete File",
            "🔤 Rename File",
            "📁 Create Folder",
            "🗂 Remove Folder",
            "📋 List All Files & Folders",
        ],
    )

    st.markdown("")

    # ── CREATE FILE ──────────────────────────────────────────────────────────
    if operation == "📄 Create File":
        file_name = st.text_input("File Name", placeholder="e.g. notes.txt")
        content   = st.text_area("File Content", placeholder="Type content here…", height=120)
        if st.button("Create File", use_container_width=True):
            if not file_name:
                show_error("Please enter a file name.")
            else:
                p = Path(file_name)
                if p.exists():
                    show_error(f'"{file_name}" already exists!')
                else:
                    try:
                        with open(file_name, "w") as f:
                            f.write(content)
                        show_success(f'File "{file_name}" created successfully.')
                        st.rerun()
                    except Exception as e:
                        show_error(str(e))

    # ── READ FILE ────────────────────────────────────────────────────────────
    elif operation == "👁 Read File":
        file_name = st.text_input("File Name", placeholder="e.g. notes.txt")
        if st.button("Read File", use_container_width=True):
            if not file_name:
                show_error("Please enter a file name.")
            else:
                p = Path(file_name)
                if not p.exists():
                    show_error(f'"{file_name}" not found.')
                elif p.is_dir():
                    show_error(f'"{file_name}" is a folder, not a file.')
                else:
                    try:
                        with open(file_name, "r") as f:
                            text = f.read()
                        show_info(f'Contents of "{file_name}":')
                        st.code(text, language="text")
                    except Exception as e:
                        show_error(str(e))

    # ── UPDATE FILE (OVERWRITE) ───────────────────────────────────────────────
    elif operation == "✏️ Update File (Overwrite)":
        file_name = st.text_input("File Name", placeholder="e.g. notes.txt")
        new_content = st.text_area("New Content (replaces existing)", height=120)
        if st.button("Overwrite File", use_container_width=True):
            if not file_name:
                show_error("Please enter a file name.")
            else:
                p = Path(file_name)
                if not p.exists():
                    show_error(f'"{file_name}" not found.')
                else:
                    try:
                        with open(file_name, "w") as f:
                            f.write(new_content)
                        show_success(f'"{file_name}" overwritten successfully.')
                    except Exception as e:
                        show_error(str(e))

    # ── UPDATE FILE (APPEND) ─────────────────────────────────────────────────
    elif operation == "➕ Update File (Append)":
        file_name = st.text_input("File Name", placeholder="e.g. notes.txt")
        extra_content = st.text_area("Content to Append", height=120)
        if st.button("Append to File", use_container_width=True):
            if not file_name:
                show_error("Please enter a file name.")
            else:
                p = Path(file_name)
                if not p.exists():
                    show_error(f'"{file_name}" not found.')
                else:
                    try:
                        with open(file_name, "a") as f:
                            f.write(extra_content)
                        show_success(f'Content appended to "{file_name}" successfully.')
                    except Exception as e:
                        show_error(str(e))

    # ── DELETE FILE ───────────────────────────────────────────────────────────
    elif operation == "🗑 Delete File":
        file_name = st.text_input("File Name to Delete", placeholder="e.g. notes.txt")
        confirm   = st.checkbox("Yes, I want to permanently delete this file.")
        if st.button("Delete File", use_container_width=True):
            if not file_name:
                show_error("Please enter a file name.")
            elif not confirm:
                show_error("Please confirm deletion by checking the box.")
            else:
                p = Path(file_name)
                if not p.exists():
                    show_error(f'"{file_name}" not found.')
                elif p.is_dir():
                    show_error(f'"{file_name}" is a folder. Use Remove Folder instead.')
                else:
                    try:
                        os.remove(p)
                        show_success(f'"{file_name}" deleted successfully.')
                        st.rerun()
                    except Exception as e:
                        show_error(str(e))

    # ── RENAME FILE ───────────────────────────────────────────────────────────
    elif operation == "🔤 Rename File":
        file_name = st.text_input("Current File Name", placeholder="e.g. old_name.txt")
        new_name  = st.text_input("New File Name",     placeholder="e.g. new_name.txt")
        if st.button("Rename File", use_container_width=True):
            if not file_name or not new_name:
                show_error("Please fill in both fields.")
            else:
                p = Path(file_name)
                if not p.exists():
                    show_error(f'"{file_name}" not found.')
                elif Path(new_name).exists():
                    show_error(f'"{new_name}" already exists.')
                else:
                    try:
                        p.rename(new_name)
                        show_success(f'Renamed "{file_name}" → "{new_name}".')
                        st.rerun()
                    except Exception as e:
                        show_error(str(e))

    # ── CREATE FOLDER ─────────────────────────────────────────────────────────
    elif operation == "📁 Create Folder":
        folder_name = st.text_input("Folder Name", placeholder="e.g. my_folder")
        if st.button("Create Folder", use_container_width=True):
            if not folder_name:
                show_error("Please enter a folder name.")
            else:
                p = Path(folder_name)
                if p.exists():
                    show_error(f'"{folder_name}" already exists.')
                else:
                    try:
                        p.mkdir()
                        show_success(f'Folder "{folder_name}" created successfully.')
                        st.rerun()
                    except Exception as e:
                        show_error(str(e))

    # ── REMOVE FOLDER ─────────────────────────────────────────────────────────
    elif operation == "🗂 Remove Folder":
        folder_name = st.text_input("Folder Name to Remove", placeholder="e.g. my_folder")
        confirm     = st.checkbox("Yes, I want to permanently remove this folder.")
        if st.button("Remove Folder", use_container_width=True):
            if not folder_name:
                show_error("Please enter a folder name.")
            elif not confirm:
                show_error("Please confirm removal by checking the box.")
            else:
                p = Path(folder_name)
                if not p.exists():
                    show_error(f'"{folder_name}" not found.')
                elif not p.is_dir():
                    show_error(f'"{folder_name}" is a file, not a folder.')
                else:
                    try:
                        p.rmdir()
                        show_success(f'Folder "{folder_name}" removed.')
                        st.rerun()
                    except OSError:
                        show_error(f'"{folder_name}" is not empty. Remove contents first.')
                    except Exception as e:
                        show_error(str(e))

    # ── LIST ALL ──────────────────────────────────────────────────────────────
    elif operation == "📋 List All Files & Folders":
        all_items = get_all_items()
        if all_items:
            show_info(f"Found {len(all_items)} item(s):")
            for idx, item in enumerate(all_items, 1):
                icon = "📁" if Path(item).is_dir() else "📄"
                st.markdown(f'<div class="file-item">{idx}. {icon} {item}</div>',
                            unsafe_allow_html=True)
        else:
            show_info("No files or folders found in the current directory.")