with open('primes.txt', 'r') as open_file:
    line = open_file.read()
    a = line.splitlines()
    print("The first list is:\n ", a)

with open('happy.txt', 'r') as open_file2:
    line2 = open_file2.read()
    b = line2.splitlines()
    print("The second list is:\n ", b)

common_list = []

for i in a:
    if i in b:
        if i in common_list:
            continue
        else:
            common_list.append(i)


print("The numbers that are in both lists are:\n", common_list)

