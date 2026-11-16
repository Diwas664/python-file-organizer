from pathlib import Path
import shutil

folder_path = Path(__file__).parent

images_folder = folder_path / "Images"
images_folder.mkdir(exist_ok = True)

pdfs_folder = folder_path / "PDFs"
pdfs_folder.mkdir(exist_ok=True)

csvs_folder = folder_path / "CSVs"
csvs_folder.mkdir(exist_ok=True)

for path_file in folder_path.iterdir():
    if path_file.is_file():
        if path_file.suffix == ".jpg" or path_file.suffix == ".png":
            shutil.move(path_file,images_folder/path_file.name)
            print(f"Moved {path_file.name} to Images")

        elif path_file.suffix == ".pdf":
            shutil.move(path_file,pdfs_folder/path_file.name)
            print(f"Moved {path_file.name} to PDFs")

        elif path_file.suffix == ".csv":
            shutil.move(path_file, csvs_folder / path_file.name)
            print(f"Moved {path_file.name} to CSVs")