'''
    Task 2: Write and Append Data to a File
 
    Problem Statement: Write a Python program that:
    1.   Takes user input and writes it to a file named output.txt.
    2.   Appends additional data to the same file.
    3.   Reads and displays the final content of the file.
 
'''

#Writing content to a output.txt file
with open("output.txt",'wt') as output_write:
    content1 = input("Enter text to write to the file: ")
    output_write.write(content1)
    print("Data successfully written to output.txt.")

#Appending the additional content to the output.txt file
with open("output.txt",'at') as output_append:
    content2 = input("Enter the additional text to append: ")
    output_append.write(content2)
    print("Data Successfully appended.")

#Reading the final content of the output.txt file
with open("output.txt",'rt') as output_read:
    print("Final content of the output.txt:\n")
    readlines = output_read.readlines()
    for lines in readlines:
        print(lines.rstrip("\n"))