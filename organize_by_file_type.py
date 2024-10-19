import os
import shutil

# Define folder paths
DOWNLOAD_FOLDER = '/path/to/your/folder'  # Change this to your directory path

# Dictionary to define folder names for file types
FILE_TYPE_FOLDERS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.doc', '.docx', '.pdf', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
    'Archives': ['.zip', '.tar', '.gz', '.rar', '.7z'],
    'Code': ['.py', '.cpp', '.java', '.js', '.html', '.css', '.sh', '.bat'],
    'Others': []
}

def create_folders():
    """Create folders based on file types if they don't exist."""
    for folder_name in FILE_TYPE_FOLDERS.keys():
        folder_path = os.path.join(DOWNLOAD_FOLDER, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def move_file(file_name, source_folder, target_folder):
    """Move file from source folder to target folder."""
    source = os.path.join(source_folder, file_name)
    target = os.path.join(target_folder, file_name)
    shutil.move(source, target)
    print(f'Moved: {file_name} to {target_folder}')

def organize_files():
    """Organize files into appropriate folders based on their extension."""
    for file_name in os.listdir(DOWNLOAD_FOLDER):
        file_path = os.path.join(DOWNLOAD_FOLDER, file_name)
        
        # Skip directories and hidden files
        if os.path.isdir(file_path) or file_name.startswith('.'):
            continue
        
        # Get file extension
        file_ext = os.path.splitext(file_name)[1].lower()
        
        # Find the appropriate folder
        moved = False
        for folder_name, extensions in FILE_TYPE_FOLDERS.items():
            if file_ext in extensions:
                move_file(file_name, DOWNLOAD_FOLDER, os.path.join(DOWNLOAD_FOLDER, folder_name))
                moved = True
                break
        
        # If no folder matches, move it to "Others"
        if not moved:
            move_file(file_name, DOWNLOAD_FOLDER, os.path.join(DOWNLOAD_FOLDER, 'Others'))

if __name__ == '__main__':
    create_folders()  # Create folders if they don't exist
    organize_files()  # Organize files into folders
