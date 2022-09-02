from download_files import download_files_wget, download_files_requests
from unzip_files import unzip_files
from insert_into_db import load_data

if __name__ == '__main__':

    print("Downloading files...")
    #download_files_wget()
    #download_files_requests()

    print("Unzipping files...")
    #unzip_files()

    print("Loading data in to database...")
    load_data()

    print("Done!")
