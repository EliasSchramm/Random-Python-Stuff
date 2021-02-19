import math as m
import os


def save(f, d, s):
    file_name = "./data/" + f + "/" + str(s) + ".txt"
    os.makedirs(os.path.dirname(file_name), exist_ok=True)

    with open(file_name, "w") as file:
        for k, v in d.items():
            file.write(str(k) + ":" + str(v) + "\n")


def genSin(step_size):
    d = 0
    dic = dict()

    while (d + step_size) <= 360:
        d += step_size
        dic[d] = m.sin(d)

    save("sin", dic, step_size)


def genCos(step_size):
    d = 0
    dic = dict()

    while (d + step_size) <= 360:
        d += step_size
        dic[d] = m.cos(d)

    save("cos", dic, step_size)


def genTan(step_size):
    d = 0
    dic = dict()

    while (d + step_size) <= 360:
        d += step_size
        dic[d] = m.tan(d)

    save("tan", dic, step_size)


def iter():
    step_size = 10.0
    i = 0

    while i < 6:

        genSin(step_size)
        genCos(step_size)
        genTan(step_size)

        print("Finished calculating and saving sin, cos and tan in %s steps" % step_size)

        step_size /= 10

        if step_size == 0:
            exit(0)

        i += 1


if __name__ == '__main__':
    iter()
