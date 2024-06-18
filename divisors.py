def find_divisors(input):    
    input= int(input("Write the number for which you want to see all the divisors: "))
    number = list(range(1, input+1))
    divisors=[]
    for num in number:
        if input % num == 0:
            divisors.append(num)

    print(divisors)

find_divisors(input)