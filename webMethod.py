import requests
from color import *
from symbols import info, workFine
import sys

def requester(url, dirList, port):
    ind = input(info+blue("https")+"/"+light_red("http")+info)
    with open(dirList, 'r') as dirs:
        for d in dirs:
            request = requests.get(f'{ind}://{url}:{port}/{d.strip()}')
            print(f"[{request.url}]:[{request.status_code}]")
def main():
    print(workFine+f"{sys.argv[1]}:{sys.argv[2]}"+workFine)
    requester(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__=='__main__':
    main()
