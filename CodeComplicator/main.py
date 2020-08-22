import itertools

global POS, LETTERS, LIST, FUN_DIC, VER_DIC

FUN_DIC = {}
LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW_"
POS = 0


def getNextName():
    global POS
    i = 0
    for comb in LIST:
        if (i == POS):
            name = ""
            for x in comb:
                name += x
            return name
        i += 1
    POS += 1
    return ""


def complicatePython(inputfile, outputfile):
    f = open(inputfile, "r")
    fileContent = f.read()
    f.close()

    lines = fileContent.split("\n")

    f = open(outputfile, "a")
    f.truncate(0)

    for line in lines:
        if "def " in line and "):" in line:
            fun_name = line.split("def ")[1].split("(")[0]
            if not fun_name == "print":
                newName = getNextName()
                FUN_DIC[fun_name] = newName

                line = line.replace(fun_name, newName)

        else:
            for k, v in FUN_DIC.items():
                if k in line:
                    if line.split(k)[1].startswith("(") and not "print" in line:
                        line = line.replace(k, v)

        if not line.replace("\n", "").replace(" ", "") == "":
            f.write(line + "\n")

    f.close()


if __name__ == "__main__":
    LIST = itertools.combinations(LETTERS, 5)

    complicatePython("test/main.py", "test/out.py")
