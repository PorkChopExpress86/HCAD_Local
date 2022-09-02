import requests
import wget

from clean_dirs import remove_files


def download_files_wget():
    # remove the current files zip files
    remove_files(r"zipped_data/*")

    # File list of zip files to download
    file_list = ["Real_acct_owner.zip", "Real_building_land.zip"]

    # Download the files in the list
    for file in file_list:
        year = "2022"
        url = f"https://download.hcad.org/data/CAMA/{year}/{file}"
        print(f"\tDownloading {file} for {year}...")
        wget.download(url=url, out='zipped_data', )


def download_files_requests():
    # remove the current files zip files
    remove_files(r"zipped_data/*")

    # File list of zip files to download
    file_list = ["Real_acct_owner.zip", "Real_building_land.zip"]

    # Download the files in the list
    for file in file_list:
        year = "2022"
        url = f"https://download.hcad.org/data/CAMA/{year}/{file}"
        print(f"\tDownloading {file} for {year}...")
        data = requests.get(url, allow_redirects=True)

        with open(f"zipped_data/{file}", "wb") as f:
            f.write(data.content)
