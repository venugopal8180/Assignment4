'''
    Task 1: Read a File and Handle Errors 
    Problem Statement:  Write a Python program that:
    1.   Opens and reads a text file named sample.txt.
    2.   Prints its content line by line.
    3.   Handles errors gracefully if the file does not exist.

'''

try:                               #excute the try block code if not have any errors.
    file_name ="sample.txt"        #file path is given into file_name variable.
    file = open(file_name,'rt')    #for reading operation file used 'rt' mode.
    line1 = file.readline()        #it reads the first line content of the file.
    line2 = file.readline()        #it reads the second line content of the file.
    print("Reading file content:")
    print(f"line 1:{line1}")       #printing the line 1 content.
    print(f"line 2:{line2}")       #printing the line 2 content.
    file.close()                   #closing the file after performing the read operation.
except FileNotFoundError:          #if given file not exists then FileNotFoundError will raise so to handle that below statement is printed 
    print(f"The file \'{file_name}\' was not found.")
