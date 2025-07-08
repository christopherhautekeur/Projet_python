from tools import files_utils

def main():
    files = files_utils.get_files_list()
    
    # Parcours les fichiers
    for file in files:
        files_utils.download(file[0], file[1])


if __name__ == "__main__":
    main()