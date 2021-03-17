from color import *
from symbols import *

errorList = {
    1: usage
    + white("usage: ")
    + light_yellow("nslookup <Domain> ")
    + usage
    + "\n"
    + info
    + white("Example: ")
    + light_green("nslookup www.example.com ")
    + info
    + "\n",
    2: usage
    + white("usage: ")
    + light_yellow("mbuster <url> <urlList> <port>")
    + usage
    + "\n"
    + info
    + white("Example: ")
    + light_green("mbuster wwww.example.com  dir.txt  443")
    + info
    + "\n",
    3: usage
    + white("usage: ")
    + light_yellow("workspace <WorkspaceName>")
    + usage
    + "\n"
    + info
    + white("Example: ")
    + light_green("workspace testworkspace")
    + info
    + "\n",
    4: usage
    + white("usage: ")
    + light_yellow("allowedMethod <urlsList>")
    + usage
    + "\n"
    + info
    + white("Example ")
    + light_green("allowedMethod urlList.txt")
    +info
    +"\n"
}


def switcher(case):
    return errorList[case]
