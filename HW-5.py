def calc(prog, val):
    acc = val
    for i in prog:
        if i == '1':
            acc += 2
        elif i == '2':
            acc *= 3
    return acc

def build(start, stop):
    for i in '*12':
        for j in '*12':
            for k in '*12':
                for l in '*12':
                    for m in '*12':
                        program = "".join([i, j, k, l, m])
                        result = calc(program, start)
                        if result == stop:
                            return program.replace("*", "")
    return None

if __name__ == "__main__":
    program = build(1,31)
    if program is None:
        print("False")
    else:
        print(f'Программа {program}')