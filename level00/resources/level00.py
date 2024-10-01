import logging
import subprocess

from utils.ssh import ssh_command


def solve_level00(ssh_instance):
    logging.debug("Finding files owned by flag00")
    output = ssh_command(ssh_instance, "find / -user flag00")

    files = [str(f) for f in output.split("\n") if "john" in f]

    logging.debug("Files found: %s", files)
    content = ssh_command(ssh_instance, f"cat {files[0]}").strip()
    logging.debug("Content (%s): %s", files[0], content)

    logging.debug("Trying to decode the content with cesar cipher")
    for i in range(1, 26):
        logging.debug("Result (%02d): %s", i, cesar_cipher(content, i))
    logging.info("Flag00 password found: %s", cesar_cipher(content, 11))


def cesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result
