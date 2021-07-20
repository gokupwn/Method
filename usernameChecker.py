#--------------------------------------------------#
#    You Can Use Your Own Url List 
#    List That Comes With This Tool
#    Is A Simple One
#--------------------------------------------------#

from json import load
import requests 
from color import *


class UsernameChecker():
    def __init__(self, USERNAME):
        self.USERNAME   = USERNAME
        self.URLFILE    = 'url_store.json' 
    
    def print_out(self, url):
        print(light_red("[") + light_gray(">") + light_blue("]: "), end='')
        print(light_green(url))
    
    def check_username(self):
        with open(self.URLFILE, 'r') as urlsFile:
            raw_data = load(urlsFile)
            for data in raw_data:
                # print(data["url"].format(self.USERNAME))
                response = requests.get(data["url"].format(self.USERNAME))
                if response.status_code == 200:
                    self.print_out(data["url"].format(self.USERNAME))