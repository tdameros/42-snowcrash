import logging
import os

from utils.ssh import *
from utils.flags import get_flag
from level00.resources.level00 import solve_level00
from level01.resources.level01 import solve_level01

IP = "192.168.64.4"
PORT = 4242

LEVELS = {
    0: solve_level00,
    1: solve_level01,
}


def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    paramiko_logger = logging.getLogger('paramiko')
    paramiko_logger.setLevel(logging.CRITICAL)

    while True:
        level = select_level()
        solver = LEVELS.get(level)
        ssh = ssh_connect("level00", "level00", IP, PORT)
        print(f"Solving level{level:02}...")
        solver(ssh)
        logging.info(f"Flag{level:02} found: %s", get_flag(level))
        ssh.close()
        input("Press Enter to continue...")
        print()

def select_level():

    # os.system("cls" if os.name == "nt" else "clear")
    print(" SNOWCRASH Solver ".center(50, "="))
    print()
    for level in LEVELS:
        print(f"{level}. level{level:02}".center(50, " "))
    print()
    while not (result := input("Which level do you want to solve?")).isdigit() or int(result) not in LEVELS:
        print("Invalid level")
    return int(result)



if __name__ == "__main__":
    main()
