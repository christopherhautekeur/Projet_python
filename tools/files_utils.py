import requests

def get_files_list() -> list:
    files = []
    with open("download.csv", "r") as f:
        while line := f.readline():
            line = line.split(",")

            if line[1].endswith('\n'):
                line[1] = line[1][:-1]

            files.append((line[0], line[1]))

    return files

def download(filename: str, url: str) -> None:
    requete = requests.get(url)

    with open(f"./files/{filename}", "wb") as f:
        f.write(requete.content)
    
