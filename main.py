import os

file_path = "pathtotextfile"

with open(file_path, "r") as file:
    for line_number, line in enumerate(file, start=1):
        line = line.strip()

        folder_name = f"{line}_{line_number}"
        os.makedirs(folder_name, exist_ok=True)

        cover_folder = os.path.join(folder_name, "cover")
        os.makedirs(cover_folder, exist_ok=True)

        songs_folder = os.path.join(folder_name, "songs")
        os.makedirs(songs_folder, exist_ok=True)

        print(f"Created folder: {folder_name}")
        print(f"Created subfolders: {cover_folder}, {songs_folder}")