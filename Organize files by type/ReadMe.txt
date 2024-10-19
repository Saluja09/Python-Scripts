Here’s a **README** file for the script, explaining its usage, purpose, and configuration:

### README for Organize Files Script

---

# Organize Files by Type - Python Script

This Python script automates the process of organizing files in a given directory by their file type (extension). It moves files into appropriate subfolders (e.g., Images, Documents, Audio, etc.), based on their extensions, decluttering your directory.

## Features
- Organizes files by file type (e.g., `.jpg`, `.txt`, `.mp3`, `.pdf`, etc.).
- Automatically creates folders for each file type.
- Moves files into appropriate folders.
- Skips directories and hidden files (files that start with a dot `.`).
- Handles unsupported file types by moving them into an "Others" folder.

## File Type Categories
The script organizes files into the following categories:
- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`
- **Documents**: `.doc`, `.docx`, `.pdf`, `.txt`, `.ppt`, `.pptx`, `.xls`, `.xlsx`
- **Audio**: `.mp3`, `.wav`, `.flac`, `.aac`
- **Videos**: `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`
- **Archives**: `.zip`, `.tar`, `.gz`, `.rar`, `.7z`
- **Code**: `.py`, `.cpp`, `.java`, `.js`, `.html`, `.css`, `.sh`, `.bat`
- **Others**: Files with extensions that don't fall into the above categories.

## Prerequisites
- Python 3.x installed on your system.
- Basic knowledge of running Python scripts.

## How to Use

### 1. Clone or Download the Script
You can download the script or clone this repository to your local machine.

```bash
git clone https://github.com/yourusername/organize-files-script.git
cd organize-files-script
```

### 2. Set the Directory Path
Open the Python script `organize_files.py` and update the `DOWNLOAD_FOLDER` variable to point to the directory you want to organize.

```python
DOWNLOAD_FOLDER = '/path/to/your/folder'  # Change this to your directory path
```

### 3. Run the Script
After setting the directory, run the script using Python.

```bash
python organize_files.py
```

### 4. Organized Output
Once the script completes, your directory will be organized into subfolders based on file types. For example:

Before:

```
Downloads/
    - vacation.jpg
    - report.docx
    - song.mp3
    - script.py
    - archive.zip
    - unknownfile.dat
```

After:

```
Downloads/
    Images/
        - vacation.jpg
    Documents/
        - report.docx
    Audio/
        - song.mp3
    Code/
        - script.py
    Archives/
        - archive.zip
    Others/
        - unknownfile.dat
```

## Customizing File Categories
You can add, remove, or modify the file categories and their extensions in the script. Modify the `FILE_TYPE_FOLDERS` dictionary inside the script to suit your needs:

```python
FILE_TYPE_FOLDERS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.doc', '.pdf', '.txt'],
    # Add or modify categories as needed
}
```

## Troubleshooting
- **Files not moving**: Ensure the `DOWNLOAD_FOLDER` path is correct and the script has the necessary permissions to read and move files.
- **Handling large directories**: If you have a large directory with many files, the script should handle it efficiently. However, for very large directories, consider running the script with elevated permissions (`sudo` on Linux/Mac).

## Contributing
Feel free to fork this repository, make changes, and submit a pull request if you have any improvements or additional features to suggest!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
If you encounter any issues or have suggestions, please contact me at [youremail@example.com].

---

This README provides an overview of the script, how to set it up, and additional customizations that can be made.