# Reading data from text file using file = open() and file.read() methods.
file = open("data1.txt", "r")
content = file.read()
print("Content of the file:")
print(content)
file.close()
print(f'Data has been read from data1.txt successfully.')