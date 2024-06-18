wrd = input("Enter a word:")
wrd = str(wrd)
rvs = wrd[::-1]
print(rvs)
if wrd == rvs:
    print("The word is a palindrome")
else:
    print("The word  is not a palindrome")
