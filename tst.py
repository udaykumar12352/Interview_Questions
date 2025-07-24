def extract(exp):
    # Extracts unique variables (characters) from the expression
    seq = []
    for i in exp:
        if i not in seq and i.isalpha():  # only letters
            seq.append(i)
    return seq

li = []
a = int(input("Enter the number of operations: "))
for i in range(a):
    line = input("Enter the expression: ").strip()
    a,b=line.split("=")
    li.append([a,b])
                   

lhs = []
rhs = []
op = []

for i in li:
    lhs.append(i[0])
    rhs.append(i[1])

for i in range(len(li)):
    curr_lhs = lhs[i]
    curr_rhs = rhs[i]
    vars_in_rhs = extract(curr_rhs)
    reused = False

    # Look backwards to find a matching rhs with no reassignment
    for j in range(i-1, -1, -1):
        if rhs[j] == curr_rhs:
            prev_lhs = lhs[j]
            reassigned = False
            for k in range(j+1, i):
                if lhs[k] in vars_in_rhs:
                    reassigned = True
                    break

            if not reassigned:
                op.append((curr_lhs, prev_lhs))
                reused = True
                break

    if not reused:
        op.append((curr_lhs, curr_rhs))

print(op)
