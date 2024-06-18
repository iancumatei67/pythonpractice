def element_search(a, b):
    for element in a:
        if element == b:
            return True
    return False


if __name__=="__main__":  
    list = [1, 2, 3, 5, 8, 13, 21, 55, 89]
    number = 0
    while number not in list:
        number = int (input("Enter a number: "))
    print(element_search(list, number))

    