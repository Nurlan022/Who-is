import zipfile
import os 
import requests

def download_file(url):
    loc = os.getcwd()
    r = requests.get(f"{url}", allow_redirects=True)
    open(f'{loc}\\01.zip', 'wb').write(r.content)


def Unzip():
    target ='01.zip'    
    handle = zipfile.ZipFile(target)
    handle.extractall(f"{os.getcwd()}\\UNpacked")
    handle.close()
    os.remove(f'{os.getcwd()}\\01.zip')