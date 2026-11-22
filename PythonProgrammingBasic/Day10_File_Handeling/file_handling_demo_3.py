# Writing data to a txt file using file = open() and file.write() methods.
file = open("data1.txt", "w")
file.write("Hello, this is a sample text file.\n")
file.write("This file is created for demonstration purposes.\n")    
file.write("You can write multiple lines of text into this file.\n")
file.close()
print(f'Data has been written to data1.txt successfully.')