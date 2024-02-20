import gdown
import os
import zipfile


def download_and_extract_zip(gdrive_url, output_folder):
    """
    Download a zip file from Google Drive using the file's sharing link and extract it.

    :param gdrive_url: The sharing link of the file on Google Drive
    :param output_folder: The local folder where the contents of the zip file will be extracted
    """
    folder_id = gdrive_url.split("/d/")[1].split("/view")[0]
    template = "https://drive.google.com/uc?id="
    # Download the zip file
    zip_file_path = os.path.join(output_folder, folder_id)
    gdown.download(url=template + folder_id, output=zip_file_path, quiet=False, fuzzy=True)


if __name__ == "__main__":
    with open('links.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    for link in lines:
        download_and_extract_zip(link, "tdatas/")
