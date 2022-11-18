### Egyptian multiplication: 25 pt

# example output:
# 
# Factor A: 19
# Factor B: 23
# =========================
# X    1   23
# X    2   46
#      4   92
#      8  184
# X   16  368
# =========================
# 1 + 2 + 16 = 19
# 23 + 46 + 368 = 437
# =========================
# 19 * 23 = 437
# 


from math import log

# no error check required
a = int(input("Factor A: "))
b = int(input("Factor B: "))

# keep original input for printout later
in_a, in_b = a, b

if a > b:
    a, b = b, a

maxbinary = int(log(a, 2))

# using reverse order, since we start with the biggest binary
reverse_table = reversed([(2**n, b * 2**n) for n in range(maxbinary+1)])

# manual list build
# 
# table = []
# n = 1
# while n <= a:
#    table.append((n, b)) 
#    n *= 2
#    b *= 2
# reverse_table = reversed(table)

# output strings
output = []
# marked numbers (for use in the + lines later)
a_list, b_list = [], []

# pick out the Xs
for bin, bfact in reverse_table:
    if bin <= a:
        tag = 'X'
        a -= bin
        a_list.append(bin)
        b_list.append(bfact)
    else:
        tag = ' '
    output.append(f'{tag} {bin:4d} {bfact:4d}')

# reverse all lists back to increasing
for l in (a_list, b_list, output):
    l[:] = reversed(l)
    
divider = "=" * 25

print(divider)

print('\n'.join(output))

print(divider)

print(' + '.join(map(str, a_list)), '=', sum(a_list))
print(' + '.join(map(str, b_list)), '=', sum(b_list))

print(divider)

print(f'{in_a} * {in_b} = {in_a * in_b}')

#############
