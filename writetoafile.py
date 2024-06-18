filename = input("File to save to: ")
text = input ("Choose what to write in the file: ")
with open(filename, 'w') as open_file:
    open_file.write(text)
with open(filename, 'r') as open_file:
    line = open_file.readline()
    print(line)