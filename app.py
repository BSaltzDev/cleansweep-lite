from pathlib import Path
import shutil

FILE_CATEGORIES = {
    ".pdf": "PDFs",
    ".doc": "Word Documents",
    ".docx": "Word Documents",
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".csv": "Spreadsheets",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".txt": "Text Files",
    ".md": "Text Files",
    ".ppt": "Presentations",
    ".pptx": "Presentations",
}


def get_category(file_path):
    extension = file_path.suffix.lower()
    return FILE_CATEGORIES.get(extension, "Other Files")


def get_unique_destination(destination_file):
    counter = 1
    new_destination = destination_file

    while new_destination.exists():
        stem = destination_file.stem
        suffix = destination_file.suffix
        new_name = f"{stem}_{counter}{suffix}"
        new_destination = destination_file.parent / new_name
        counter += 1

    return new_destination


def preview_files(target_folder):
    print(f"\nPreviewing folder: {target_folder}\n")

    found_files = False

    for item in target_folder.iterdir():
        if item.is_file():
            found_files = True
            category = get_category(item)
            destination = target_folder / category / item.name
            destination = get_unique_destination(destination)
            print(f"Would move: {item.name}  ->  {destination}")

    if not found_files:
        print("No loose files found in the top level of this folder.")


def organize_files(target_folder):
    print(f"\nOrganizing folder: {target_folder}\n")

    found_files = False

    for item in target_folder.iterdir():
        if item.is_file():
            found_files = True
            category = get_category(item)
            destination_folder = target_folder / category
            destination_folder.mkdir(exist_ok=True)

            destination_file = destination_folder / item.name
            destination_file = get_unique_destination(destination_file)

            shutil.move(str(item), str(destination_file))

            print(f"Moved: {item.name}  ->  {destination_file}")

    if not found_files:
        print("No loose files found in the top level of this folder.")
    else:
        print("\nOrganization complete.")


def main():
    print("CleanSweep Lite")
    print("----------------")
    print("1 - Preview only")
    print("2 - Organize files")

    mode = input("\nEnter 1 or 2: ").strip()
    folder_path = input("Enter the folder path: ").strip()
    target_folder = Path(folder_path)

    if not target_folder.exists():
        print("\nThat folder does not exist.")
    elif not target_folder.is_dir():
        print("\nThat path is not a folder.")
    elif mode == "1":
        preview_files(target_folder)
    elif mode == "2":
        organize_files(target_folder)
    else:
        print("\nInvalid selection. Please run the program again and enter 1 or 2.")


main()