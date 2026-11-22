# Appending data to a text file
file = open("data1.txt", "a")
file.write("\nThis is an additional line of text.\n")
file.close()
print(f'Data has been appended to data1.txt successfully.')