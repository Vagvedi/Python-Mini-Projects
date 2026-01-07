import os
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"]
}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            moved = False
            _, ext = os.path.splitext(filename)

            for folder, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    target_folder = os.path.join(folder_path, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, target_folder)
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(folder_path, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, other_folder)

    print("✅ Files organized successfully!")

if __name__ == "__main__":
    print("📁 FILE ORGANIZER AUTOMATION 📁")
    path = input("Enter folder path to organize: ").strip()
    organize_files(path)
