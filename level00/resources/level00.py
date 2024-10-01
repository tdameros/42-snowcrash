import logging
import subprocess

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    process = subprocess.Popen(["find", "/", "-user", "flag00"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()

    files = [str(f) for f in output.decode().split("\n") if "john" in f]

    logging.debug("Files found: %s", files)
    with open(files[0], "r") as file:
        content = file.read().strip()
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


if __name__ == "__main__":
    main()
