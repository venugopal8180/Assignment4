# Assignment 4 
Task 1: Read a File and Handle Errors

#Concept of task 1:
This program demonstrates basic file handling and exception handling in Python.
It attempts to open a text file named **sample.txt**, read its contents, and display the lines.
If the file does not exist, the program handles the error gracefully using a `try-except` block.

# Program Functionality
The program performs the following steps:
1. Defines the file name `sample.txt`.
2. Opens the file in **read mode (`rt`)**.
3. Reads the file content using `readline()`.
4. Prints the first two lines of the file.
5. Closes the file after reading.
6. If the file does not exist, the program catches the **FileNotFoundError** and displays an appropriate message.

## Requirements
* Python 3 installed on the system
* A text file named **sample.txt** in the same directory as the program
  
## How to Run the Program
1. Place the Python file and **sample.txt** in the same folder.
2. Open a terminal or command prompt in that folder.
3. Run the program using:

```
python filename.py
```
Replace `filename.py` with the actual name of the Python script.

---
## Example Output
If the file exists:

```
Reading file content:
line 1: Hello World
line 2: Welcome to Python
```
If the file does not exist:
```
The file 'sample.txt' was not found.
```
## Concepts Used
* File Handling (`open`, `readline`, `close`)
* Exception Handling (`try`, `except`)
* `FileNotFoundError`
* String formatting using `f-strings`
* 
#Learning Outcome From Task 1
This task helps understand how to safely work with files in Python and how to prevent program crashes by handling errors properly.

Task 2: Write and Append Data to a File

#concept of task 2
This program demonstrates file operations in Python including **writing, appending, and reading data from a file**. 
The program interacts with the user to store text in a file and then displays the final content.

## Program Functionality
The program performs the following operations:
1. **Write Data to a File**
   * Takes input from the user.
   * Writes the input to a file named **output.txt** using write mode (`wt`).
   * If the file does not exist, it is automatically created.
2. **Append Additional Data**
   * Takes another input from the user.
   * Appends the new content to the same file using append mode (`at`).
3. **Read Final Content**
   * Opens the file in read mode (`rt`).
   * Reads all lines using `readlines()`.
   * Displays the final content of the file line by line.
     
# Example Execution
Example interaction with the program:

Enter text to write to the file: Hello Python
Data successfully written to output.txt.
Enter the additional text to append: Learning File Handling
Data Successfully appended.
Final content of the output.txt:
Hello PythonLearning File Handling

# Concepts Used
* File Handling in Python
* `with open()` statement
* File modes:
  * `wt` – write text
  * `at` – append text
  * `rt` – read text
* User input using `input()`
* Reading lines using `readlines()`
* Looping through file content

# Learning Outcome
Through this task, the following Python concepts are practiced:
* Writing data to files
* Appending new data without deleting existing content
* Reading and displaying file content
* Using `with open()` for automatic file closing


