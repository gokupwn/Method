import threading
import os
import shell
from banner import banner1
# import socket
# import http.client
# import re
# import argparse
# from color import *
# from symbols import *


# urlList = ""
# outputFile = "result.txt"
# visible = True
# silent = False
# interactive = False
# intOnly = False


# def get_options():
#     global urlList
#     global visible
#     global outputFile
#     global silent
#     global interactive
#     global intOnly
#     parser = argparse.ArgumentParser()

#     parser.add_argument(
#         "-v", "--verbose", help="increase output verbosity", action="store_true"
#     )
#     parser.add_argument("-l", "--list", help="list of urls", type=str)
#     parser.add_argument("-o", "--output", help="output file", type=str)
#     parser.add_argument(
#         "-db", "--disablebanner", help="disable banner", action="store_true"
#     )
#     parser.add_argument("-s", "--silent", help="silent mode", action="store_true")
#     parser.add_argument(
#         "-i", "--interactive", help="interactive lookup", action="store_true"
#     )
#     parser.add_argument(
#         "-io", "--interactiveOnly", help="interactive only mode", action="store_true"
#     )
#     args = parser.parse_args()

#     if args.list:
#         urlList = args.list

#     if args.disablebanner:
#         visible = False

#     if args.silent:
#         silent = True

#     if args.interactive:
#         interactive = True

#     if args.interactiveOnly:
#         interactive = True
#         intONly = True

#     if args.output:
#         outputFile = args.output


# def status_code(Response):
#     statusCode = [Response.status, Response.reason]
#     return statusCode


# def read_list(urlList):
#     try:
#         with open(urlList, "r") as urls:
#             for url in urls:
#                 flag = re.search(r'^(http|https):', url)

#                 if flag.group(0) == 'https:':
#                     url = re.sub(r'^(https)://', '', url)
#                     allowed_method(url.rstrip(), 'HTTPS')

#                 elif flag.group(0) == 'http:':
#                     url = re.sub(r'^(http)://', '', url)
#                     allowed_method(url.rstrip(), 'HTTP')

#     except FileNotFoundError:
#         print("")
#         #print("[!]No Such File[!]")


# def write_file(outputFile, statusCode, url, allowed):
#     with open(outputFile, "a") as output:
#         output.write("+" + "-" * 50 + "+\n")
#         toWrite = (
#             url + ": " + str(statusCode[0]) + ": " + statusCode[1] + ": " + str(allowed)
#         )
#         leng = 50 - len(toWrite)
#         output.write("|" + toWrite + " " * leng + "|\n")
#         output.write("+" + "-" * 50 + "+\n")


# def allowed_method(url, httpIndicator):
#     try:
#         # create instance HTTP Client
#         if httpIndicator == 'HTTP':
#             ClientHTTP = http.client.HTTPConnection(url)
#             ClientHTTP.request('OPTIONS', '/')
#             Response = ClientHTTP.getresponse()
#             allowed = Response.getheader('allow')
#         elif httpIndicator == 'HTTPS':
#             ClientHTTPS = http.client.HTTPSConnection(url)
#             # use request method to check the allowed method
#             ClientHTTPS.request('OPTIONS', '/')
#             Response = ClientHTTPS.getresponse()
#             # HTTPResponse.getheader(name, default=None)
#             allowed = Response.getheader('allow')
#         statusCode = status_code(Response)

#         #------Disable Output Of allowed method------# 
#         if not silent:
#             print(
#                 workFine
#                 + "The Following Method are allowed for"
#                 + red(f" {url}" + ":")
#                 + blue(f"{allowed}")
#                 + workFine
#                 + reset()
#             )
#             print(workFine+f"[+]{Response.status}:{Response.reason}"+workFine+reset())
#         write_file(outputFile, statusCode, url, allowed)

#     except:
#         print(error + light_red("Connection Failed")+ error)


def main():
    # get_options()

    # if visible:
    os.system("clear")
    banner1()

    # if not intOnly:
    #     readHandler = threading.Thread(target=read_list, args=(urlList,))
    #     readHandler.start()

    # if interactive:
    shellHandler = threading.Thread(target=shell.interactive_shell(), args=())
    shellHandler.start()


if __name__ == "__main__":
    main()
