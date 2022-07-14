
line = input().split()
#The variable x
x = line[0]
#The expected result
k = int(line[1])

equation = input().split()
result = 0

next_operation = None
for p in equation:
    if p in ['+', '-']:
        next_operation = p
        continue
    i = p.find('**')
    temp = 0
    if i != -1:
        operand_1 = p[0:i]
        operand_2 = p[i+2:]
        if operand_1 == 'x':
            operand_1 = int(x)
            operand_2 = int(operand_2)
            temp = operand_1**operand_2
        else:
            j = operand_1.find('*')
            if j != -1:
                operand_1_1 = p[0:j]
                operand_1_2 = p[j+1:i]
            if operand_1_1 == 'x':
                operand_1_1 = x
            elif operand_1_2 == 'x':
                operand_1_2 = x
            temp = int(operand_1_1)*int(operand_1_2)**int(operand_2)

    if p == 'x':
        temp = int(x)
    elif p.isdigit():
        temp = int(p)

    if next_operation == None:
        result = temp
    elif next_operation == '+':
        result += temp
    elif next_operation == '-':
        result -= temp




print(True if result == k else False)