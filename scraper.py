import requests
import threading
from symbols import error
import re
from  json import loads
from color import *


class DeepScraper ():
    def __init__(self, LINKTREEURL):
        # Link Tree URL To Be Scraped
        self.LINKTREEURL = LINKTREEURL
        self.MEDIAS      = [ 'Twitter', 'Facebook', 'Instagram', 'Github', 'Telegram', 'Linkedin', 'Snapchat' ]

        # Rgex Expression Used For Username Scraping
        self.REGEXTWITTER  = r'(?:https?:)?\/\/(?:[A-z]+\.)?twitter\.com\/@?(?!home|share|privacy|tos)(?P<username>[A-z0-9_]+)\/?'
        self.REGEXFACEBOOK = r'(?:https?:)?\/\/(?:www\.)?(?:facebook|fb)\.com\/(?P<profile>(?![A-z]+\.php)(?!marketplace|gaming|watch|me|messages|help|search|groups)[A-z0-9_\-\.]+)\/?'
        self.REGEXINSTAGRM = r'(?:https?:)?\/\/(?:www\.)?(?:instagram\.com|instagr\.am)\/(?P<username>[A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)'
        self.REGEXGITHUB   = r'(?:https?:)?\/\/(?:www\.)?github\.com\/(?P<login>[A-z0-9_-]+)\/?'
        self.REGEXTELEGRAM = r'(?:https?:)?\/\/(?:t(?:elegram)?\.me|telegram\.org)\/(?P<username>[a-z0-9\_]{5,32})\/?'
        self.REGEXLINKEDIN = r'(?:https?:)?\/\/(?:[\w]+\.)?linkedin\.com\/in\/(?P<permalink>[\w\-\_À-ÿ%]+)\/?'
        self.REGEXSNAPCHAT = r'(?:https?:)?\/\/(?:www\.)?stackexchange\.com\/users\/(?P<id>[0-9]+)\/(?P<username>[A-z0-9-_.]+)\/?'


        # Username Lists
        self.usernameTwitter   = []
        self.usernameInstagram = []
        self.usernameFacebook  = []
        self.usernameGithub    = []
        self.usernameTelegram  = []
        self.usernameLinkedin  = []
        self.usernameSnapchat  = []

        # HTML Content
        self.response = requests.get(self.LINKTREEURL)
        

    def twitter_username(self):
        try:
            self.usernameTwitter = self.remove_duplicate(re.findall(self.REGEXTWITTER, self.response.text))
        except:
            pass

    def instagram_username(self):
        try:
            self.usernameInstagram = self.remove_duplicate(re.findall(self.REGEXINSTAGRM, self.response.text))
        except:
            pass
    
    def facebook_username(self):
        try:
            self.usernameFacebook = self.remove_duplicate(re.findall(self.REGEXFACEBOOK, self.response.text))
        except:
            pass
    
    def github_username(self):
        try:
            self.usernameGithub = self.remove_duplicate(re.findall(self.REGEXGITHUB, self.response.text))
        except:
            pass

    def telegram_username(self):
        try:
            self.usernameTelegram = self.remove_duplicate(re.findall(self.REGEXTELEGRAM, self.response.text))
        except:
            pass
    
    def linkedin_username(self):
        try:
            self.usernameLinkedin = self.remove_duplicate(re.findall(self.REGEXLINKEDIN, self.response.text))
        except:
            pass

    def snapchat_username(self):
        try:
            self.usernameSnapchat = self.remove_duplicate(re.findall(self.REGEXSNAPCHAT, self.response.text))
        except:
            pass
    
    def remove_duplicate(self, List):
        toReturn = []
        [toReturn.append(x) for x in List if x not in toReturn]
        return toReturn
    
    def prettyPrint(self):
        # self.MEDIAS      = [ 'Twitter', 'Facebook', 'Instagram', 'Github', 'Telegram', 'Linkedin', 'Snapchat' ]
        self.usernameTwitter   = self.remove_duplicate(self.usernameTwitter)
        self.usernameFacebook  = self.remove_duplicate(self.usernameFacebook)
        self.usernameInstagram = self.remove_duplicate(self.usernameInstagram)
        self.usernameGithub    = self.remove_duplicate(self.usernameGithub)
        self.usernameTelegram  = self.remove_duplicate(self.usernameTelegram)
        self.usernameLinkedin  = self.remove_duplicate(self.usernameLinkedin)
        self.usernameSnapchat  = self.remove_duplicate(self.usernameSnapchat)

        print('\t' + light_blue('Twitter: ')  + '\n\n\t\t' + '\n'.join(self.usernameTwitter) + '\n')
        print('\t' + blue('Facebook: ') + '\n\n\t\t' + '\n'.join(self.usernameFacebook ) + '\n')
        print('\t' + red('Instagram: ')  + '\n\n\t\t' + '\n'.join(self.usernameInstagram ) + '\n')
        print('\t' + light_gray('Github: ')  + '\n\n\t\t' + '\n'.join(self.usernameGithub ) + '\n')
        print('\t' + light_blue('Telegram: ')  + '\n\n\t\t' + '\n'.join(self.usernameTelegram ) + '\n')
        print('\t' + light_blue('LinkedIn: ')  + '\n\n\t\t' + '\n'.join(self.usernameLinkedin ) + '\n' )
        print('\t' + light_yellow('SnapChat: ')  + '\n\n\t\t' + '\n'.join(self.usernameSnapchat) + '\n')

    def check_all(self):
        self.twitter_username()
        self.facebook_username()
        self.instagram_username()
        self.github_username()
        self.telegram_username()
        self.linkedin_username()
        self.snapchat_username()

    def username_list(self):
        self.check_all()
        usernameList =  self.usernameTwitter + self.usernameFacebook + self.usernameInstagram + self.usernameGithub + self.usernameTelegram + self.usernameLinkedin + self.usernameSnapchat
        with open("username_list.txt", 'a') as FILE:
            for username in usernameList:
                FILE.write(username+'\n')

# "https://linktr.ee/HassanAlAchek"
