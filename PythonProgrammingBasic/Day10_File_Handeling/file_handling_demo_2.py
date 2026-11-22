# Reading data from text file.
with open("data.txt", "r") as file:
    content = file.read()
    print("Content of the file:")
    print(content)
    file.close()
print(f'Data has been read from data.txt successfully.')