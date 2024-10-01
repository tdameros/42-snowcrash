
def get_flag(level: int):
    path = f"level{level:02}/flag"
    with open(path, "r") as f:
        return f.read().strip()