from color import *
from symbols import *

errorList = {
    1: "\t" + usage
    + white("usage: ")
    + light_yellow("nslookup <Domain> ")
    + usage
    + "\n"
    + "\t" + info
    + white("Example: ")
    + light_green("nslookup www.example.com ")
    + info
    + "\n",
    2: "\t" + usage
    + white("usage: ")
    + light_yellow("mbuster <url> <urlList> <port>")
    + usage
    + "\n"
    + "\t" + info
    + white("Example: ")
    + light_green("mbuster wwww.example.com  dir.txt  443")
    + info
    + "\n",
    3: "\t" + usage
    + white("usage: ")
    + light_yellow("workspace <WorkspaceName>")
    + usage
    + "\n"
    + "\t" + info
    + white("Example: ")
    + light_green("workspace testworkspace")
    + info
    + "\n",
    4: "\t" + usage
    + white("usage: ")
    + light_yellow("allowedMethod <urlsList>")
    + usage
    + "\n"
    + "\t" + info
    + white("Example: ")
    + light_green("allowedMethod urlList.txt")
    + info
    + "\n",
    5: "\t" + usage
    + white("usage: ")
    + light_yellow("deepScraper <linkTreeUrl>")
    + usage
}


def switcher(case):
    return errorList[case]
