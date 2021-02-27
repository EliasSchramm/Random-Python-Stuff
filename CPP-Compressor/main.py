import math as m
import os


def save(d, f):
    file_name = "comp/" + f
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, "w") as file:
        file.write(d)


def read(f):
    with open(f, "r") as file:
        content = file.read()
    return content


def format(c):
    c = c.split("\n")
    ret = ""

    for line in c:
        # Removing comments
        if not line.startswith("//"):
            line = line.split("//")[0]

            # Removing tabs
            line = line.strip()

            # Sorting out compiler commands like #define
            if line.startswith("#"):
                line = line + "\n"

            ret += line
    return ret


if __name__ == '__main__':
    files = os.listdir()

    for file in files:
        if file.endswith(".cpp") or file.endswith(".h"):
            content = read(file)
            formated = format(content)
            save(formated, file)
            print(formated)

