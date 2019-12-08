input_file = open(r'C:\Users\Panos\Google Drive\ECE\Python Files\Advent of Code 2019\D5\input.txt','r')
prog = list(map(int, input_file.read().split(',')))


i = 0
while True:
    op = prog[i] % 100

    if op == 99:
        break

    par1_mode = prog[i] // 100 % 10
    par2_mode = prog[i] // 1000 % 10

    par1, par2, par3 = prog[i+1:i+4]

    if par1_mode == 0:
            var1 = prog[par1]
    else:
        var1 = par1
    if par2_mode == 0:
        var2 = prog[par2]
    else:
        var2 = par2

    if op == 1:
        prog[par3] = var1 + var2
        steps = 4

    elif op == 2:
        prog[par3] = var1 * var2
        steps = 4

    elif op == 3:
        prog[par1] = int(input())
        steps = 2

    elif op == 4:
        print(prog[par1])
        steps = 2

    elif op == 5:
        if var1 != 0:
            i = var2
            steps = 0
        else:
            steps = 3

    elif op == 6:
        if var1 == 0:
            i = var2
            steps = 0
        else:
            steps = 3

    elif op == 7:
        if var1 < var2:
            prog[par3] = 1
        else:
            prog[par3] = 0
        steps = 4
    elif op == 8:
        if var1 == var2:
            prog[par3] = 1
        else:
            prog[par3] = 0
        steps = 4
    i += steps