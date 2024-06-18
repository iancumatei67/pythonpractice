if __name__ == '__main__':
    birthdays = {
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        'Donald Trump': '06/14/1946',
        'Rowan Atkinson': '01/6/1955'}

    print("Welcome to the dictionary. We know the birthdays of:\n ")
    for name in birthdays:
        print(name)

    print("Who's birthday do you want to know ?\n ")
    name = input()
    if name in birthdays:
        print(f"{name}'s birthday is {birthdays[name]}")
    else:
        print(f"Sadly we dont have {name}'s birthday")

     
    
