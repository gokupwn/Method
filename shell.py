import socket
import os
import re
import http.client
import subprocess
import threading
from autoComplete import commands, PathComplete, CommandComplete, HistoryClear
from banner import banner
from color import *
from error import *
from symbols import *
from language import good_bye
import modules


# ----------workspace---------------#
workspace = "default"
# ----------module name-------------#
module = ""
# -------desciption of command------#
descriptions = {
    "help": "Display This Message",
    "nslookup": "Display IP address Of A Specific Domain",
    "allowedMethod":"Check Allowed Method",
    "mbuster": "Directory Brute Force",
    "banner": "Do You Want A Beautiful Banner ;)",
    "workspace": "Create And Load A New Workspace To Be Organised",
    "load": "Do You Like Metasploit !!, Okay Now We Have Method Fill Free To Create Your BashScript Module",
    "clear": "Clear Output",
    "quit": "You Don\'t Need That, You Will Not Leave Me Alone"
}


# ----------nslookup----------------#
def nslookup(domain):
    infos = socket.getaddrinfo(domain, 0, 0, 0, 0)
    return infos


# ------------format----------------#
def format(infos):
    ips = []
    for info in infos:
        ips.append(info[4][0])
    return ips


# ----check command descriptions---#
def Listcommands():
    for command in commands:
        print(usage + "{}:{} ".format(light_yellow(command), descriptions[command]))


# -----allowed method--------------#

def status_code(Response):
    statusCode = [Response.status, Response.reason]
    return statusCode


def reader(Path_urlList):
    try:
        with open(Path_urlList, "r") as urls:
            for url in urls:
                flag = re.search(r'^(http|https):', url)

                if flag.group(0) == 'https:':
                    url = re.sub(r'^(https)://', '', url)
                    allowed(url.rstrip(), 'HTTPS')

                if flag.group(0) == 'http:':
                    url = re.sub(r'^(http)://', '', url)
                    allowed(url.rstrip(), 'HTTP')

    except FileNotFoundError:
        print("[!]No Such File[!]")


#----------allowed----------------#
def allowed(url, Indicator):
    try:
        # create instance HTTP Client
        if Indicator == 'HTTP':
            ClientHTTP = http.client.HTTPConnection(url)
            ClientHTTP.request('OPTIONS', '/')
            Response = ClientHTTP.getresponse()
            allowed = Response.getheader('allow')
        elif Indicator == 'HTTPS':
            ClientHTTPS = http.client.HTTPSConnection(url)
            # use request method to check the allowed method
            ClientHTTPS.request('OPTIONS', '/')
            Response = ClientHTTPS.getresponse()
            # HTTPResponse.getheader(name, default=None)
            allowed = Response.getheader('allow')
        print(
                workFine
                + "The Following Method are allowed for"
                + red(f" {url}" + ":")
                + blue(f"{allowed}")
                + workFine
                + reset()
                )
        print(workFine+f"{Response.status}:{Response.reason} "+workFine+reset())
    except ConnectionRefusedError:
        print(error + white("Connection Resfused")+ error)


# -----the interactive shell------#
def interactive_shell():
    global workspace
    try:
        while True:
            CommandComplete()

            cmd = input(
                light_red("[Method]")
                + dark_gray("[{}{}]".format(workspace, module))
                + light_green("»")
                + reset()
            )

            if cmd != "":
                # ----------nslookup------------#
                if cmd.split()[0] == "nslookup":
                    if len(cmd.split()) == 2:
                        infos = nslookup(cmd.split()[1].rstrip())
                        ips = format(infos)
                        print(workFine + "-" * 25 +workFine)
                        for ip in ips:
                            print("  "+ip)
                        print(workFine + "-" * 25 + workFine)
                    else:
                        print(switcher(1))

                #---------allowed Method----------#
                if cmd.split()[0] == "allowedMethod":
                    if len(cmd.split()) == 2:
                        reader(cmd.split()[1])
                    else:
                        print(switcher(4))

                # --------help--------------#
                if cmd.split()[0] == "help":
                    print(usage + light_yellow("Commands: "))
                    Listcommands()

                # -------workspace------------#
                if cmd.split()[0] == "workspace":
                    if len(cmd.split()) == 2:
                        workspace = cmd.split()[1]
                        dirWorkspace = os.getcwd() + "/" + workspace
                        os.mkdir(dirWorkspace)
                        os.chdir(dirWorkspace)
                    else:
                        print(switcher(3))

                # -------load----------------#
                if cmd.split()[0] == "load":
                    PathComplete()
                    modulePath = input(
                        info + dark_gray(" Enter The Module Path ") + info
                    )
                    subprocess.run("bash {}".format(modulePath), shell=True)

                # -------mbuster---------------#
                if cmd.split()[0] == "mbuster":
                    if len(cmd.split()) == 4:
                        subprocess.run("python3 webMethod.py {} {} {}".format(cmd.split()[1], cmd.split()[2], cmd.split()[3]), shell=True)

                    else:
                        print(switcher(2))
                # ------clear----------------#
                if cmd.split()[0] == "clear":
                    os.system("clear")

                # -------quit-----------------#
                if cmd.split()[0] == "quit":
                    print(stop + " " + good_bye("english") + " " + stop)
                    exit(0)

                # ---------banner-------------#
                if cmd.split()[0] == "banner":
                    banner()

            else:
                print(usage + "Please Use " + light_green("help ") + usage)

            CommandComplete()
    # --------Keyboard Interrupt-----------#
    except KeyboardInterrupt:
        print(error + "\n Error " + error)
        print(usage + " Enter quit to quit " + usage)
