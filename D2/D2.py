# prog[1] = 12
# prog[2] = 2

for noun in range(99):
    for verb in range(99):
        input_file = open(r'C:\Users\Panos\Google Drive\ECE\Python Files\Advent of Code 2019\D2\input.txt','r')
        prog = list(map(int, input_file.read().split(',')))
        prog[1] = noun
        prog[2] = verb
        for i in range(0, len(prog), 4):
            op = prog[i]
            if op == 99:
                break

            in_pos1, in_pos2, out_pos = prog[i+1:i+4]
            if op == 1:
                prog[out_pos] = prog[in_pos1] + prog[in_pos2]
            elif op == 2:
                prog[out_pos] = prog[in_pos1] * prog[in_pos2]
        if prog[0] == 19690720:
            print(100*noun + verb)

