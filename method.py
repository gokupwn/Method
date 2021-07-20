import threading
import os
import shell
from banner import banner1


def main():
    os.system("clear")
    banner1()
    shellHandler = threading.Thread(target=shell.interactive_shell(), args=())
    shellHandler.start()


if __name__ == "__main__":
    main()
