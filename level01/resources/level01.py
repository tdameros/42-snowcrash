import logging
import subprocess

from utils.ssh import ssh_command

def solve_level01(ssh_instance):
    logging.debug("Finding flag01 /etc/passwd hash")
    output = ssh_command(ssh_instance, "cat /etc/passwd")
    with open("level01/resources/passwd", "w") as f:
        f.write(output)
    flag01_passwd = [line for line in output.split("\n") if "flag01" in line][0]
    logging.debug("Flag01 passwd: \n%s", flag01_passwd)
    flag01_passwd_cracked = subprocess.run(["john", "--show", "level01/resources/passwd"], capture_output=True).stdout.decode("utf-8").split()[0]
    logging.debug("Cracking hash with john")
    logging.debug("Flag01 cracked passwd: \n%s", flag01_passwd_cracked)
    logging.info("Flag01 password found: %s", flag01_passwd_cracked.split(":")[1])




    # logging.debug("John output: %s", output)