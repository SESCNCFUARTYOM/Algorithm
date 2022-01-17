def calc(prog, val):
    acc = val
    for i in prog:
        if i == '1':
            acc += 3
        elif i == '2':
            acc *= 2
    return acc
def build(start, stop):
    for i in "*12":
        for j in "*12":
            for k in "*12":
                for l in "*12":
                    for m in "*12":
                        for d in "*12":
                            program = "".join([i, j, k, l, m, d])
                            result = calc(program, start)
                            if result == stop:
                                return program.replace("*", "")
    return None

if __name__ == "__main__":
    program = build(2,31)
    if program is None:
        print("False")
    else:
        print(f'Программа {program}')