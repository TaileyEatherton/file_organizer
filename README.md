# 📁 File Organizer Script

A Python-based utility to organize files into categorized folders based on file type or keywords in the file name. Great for quickly cleaning up messy directories.

---
## ▶️ Usage

```bash
$ python3 file_organizer.py
```

## 🚀 Features

- ✅ Automatically organizes files into folders like `Pictures`, `Documents`, `Videos`, etc.
- ✅ Supports moving files by specific extension (e.g. `.txt`, `.pdf`).
- ✅ Allows custom folder creation and moves files based on filename keyword.
- ✅ Cross-platform support using `pathlib`.

---

## 🛠️ Supported File Types

| Category       | Extensions |
|----------------|------------|
| **Pictures**       | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp` |
| **Documents**      | `.pdf`, `.docx`, `.doc`, `.txt`, `.md`, `.odt`, `.rtf` |
| **Videos**         | `.mp4`, `.mov`, `.avi`, `.mkv`, `.webm` |
| **Audio**          | `.mp3`, `.wav`, `.flac`, `.aac` |
| **Compressed**     | `.zip`, `.tar`, `.gz`, `.7z`, `.rar` |
| **Executables**    | `.exe`, `.dll`, `.app`, `.iso`, `.dep`, `.rpm` |
| **Data & Code**    | `.tsv`, `.ods`, `.xls`, `.xlsx`, `.xml`, `.csv`, `.py`, `.json`, `.html`, `.css`, `.sh`, `.bat`, `.js`, `.ini`, `.toml`, `.yaml` |

---

## 📂 How It Works
NOTE: This Script will take the files in the CURRENT directory and move them to folders in the HOME directory.
When you run the script, you’ll be prompted to choose one of the following options:

### 1. **Organize All Files**
Moves all supported files in the current directory to categorized folders in your home directory.

### 2. **Move Files by Extension**
Prompts you to enter a file extension and moves only those files to their appropriate folders.

### 3. **Organize by Keyword**
Prompts for a custom folder name and a keyword, then moves any file containing the keyword into the custom folder.

### 4. **Exit**
Quits the program.

---

