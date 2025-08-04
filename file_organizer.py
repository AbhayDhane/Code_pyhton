import os
import shutil

# Define file type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css"],
}

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print("❌ Invalid folder path!")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()

            found = False
            for folder_name, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    target_folder = os.path.join(folder_path, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    found = True
                    break

            if not found:
                other_folder = os.path.join(folder_path, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))

    print("✅ Files organized successfully!")

# Example usage
if __name__ == "__main__":
    folder = input("Enter full path of folder to organize: ").strip()
    organize_files(folder)
