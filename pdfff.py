from fpdf import FPDF
import unicodedata

class PDF(FPDF):
    def header(self):
        # Set font
        self.set_font('Arial', 'B', 14)
        # Title
        self.cell(0, 10, 'MCA Lab Manual (CAMS-3P01) - Weekly Questions', 0, 1, 'C')
        self.ln(5)
    
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Select Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
    
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)
    
    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 7, body)
        self.ln()

def clean_text(text):
    """Clean text to handle Unicode characters"""
    # Replace common problematic Unicode characters
    replacements = {
        '\u2019': "'",  # Right single quotation mark
        '\u2018': "'",  # Left single quotation mark
        '\u201c': '"',  # Left double quotation mark
        '\u201d': '"',  # Right double quotation mark
        '\u2013': '-',  # En dash
        '\u2014': '--', # Em dash
        '\u2026': '...', # Ellipsis
        '\u2022': '*',  # Bullet point
        '\u25b6': '>',  # Black right-pointing triangle
        '\u014d': 'o',  # o with macron
        '\u016b': 'u',  # u with macron
        '\u0101': 'a',  # a with macron
        '\u012b': 'i',  # i with macron
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    # Remove any other non-ASCII characters
    text = text.encode('ascii', 'replace').decode('ascii')
    return text

def create_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # All weekly questions
    weeks_content = {
        'WEEK #1': [
            "1. Write a program to find the product of two user-supplied integers and if the product is equal to or lower than 5000, then return the sum of the two numbers.",
            "2. Write a program to print the sum of the first 10 numbers.",
            "3. Write a program to iterate through a supplied list of 20 numbers and print only those numbers which are divisible by 5.",
            "4. Write a program to check if the given number is a palindrome.",
            "5. Write a program to calculate the cube of all numbers from 1 to a given number."
        ],
        'WEEK #2': [
            "1. Write a program to extract each digit from an integer in reverse order.",
            "2. Write a program to count the total number of digits in a number using a while loop.",
            "3. Write a program to display all prime numbers within a range.",
            "4. Write a program to use a loop to find the factorial of a given number.",
            "5. Write a program to find the sum of the digits of a supplied integer."
        ],
        'WEEK #3': [
            "1. Write a program to print the following pattern using the for loop:\n   5 4 3 2 1\n   4 3 2 1\n   3 2 1\n   2 1\n   1",
            "2. Write a program to print the following star pattern using the for loop:\n   *\n   **\n   ***\n   ****\n   *****\n   ****\n   ***\n   **\n   *",
            "3. Write a program to print characters from a string which are present at even index numbers.",
            "4. Write a program to accept a string from the user and display characters that are present at even index numbers.",
            "5. Write a program to remove characters from a string starting from the nth position to the last and return a new string. Example: remove_chars('aligarh', 3) should output 'ali'."
        ],
        'WEEK #4': [
            "1. Write a program to create a function cal_sum_sub() that accepts two variables and calculates addition and subtraction. Also, it must return both addition and subtraction in a single return call.",
            "2. Write a function to return True if the first and last number of a given list are the same. If the numbers are different, return False.",
            "3. Given a list of numbers, write a program to turn every item of the list into its square.",
            "4. Given two Python lists, write a program to iterate both lists simultaneously and display items from list 1 in original order and items from list 2 in reverse order.",
            "5. Write a program to count the number of occurrences of item 50 in the tuple tp1=(50, 10, 60, 70, 50)."
        ],
        'WEEK #5': [
            "1. Write a program to generate a 6-digit random secure OTP.",
            "2. Write a program to pick a random character from a user-supplied string.",
            "3. Write a program to generate a random password that meets the following conditions:\n   a. Password length must be 10 characters long.\n   b. It must contain at least 2 uppercase letters, 1 digit, and 1 special symbol.",
            "4. Given two lists of numbers, write a program to create a new list containing odd numbers from the first list and even numbers from the second list.",
            "5. Write a program to create a numpy array and return an array of odd rows and even columns from the numpy array.",
            "6. Write a program to create a numpy array and sort it as per the following cases:\n   a. Case 1: Sort the array by the second row.\n   b. Case 2: Sort the array by the second column."
        ],
        'WEEK #6': [
            "1. Write a Python program that inputs two tuples and creates a third that contains all elements of the first followed by all elements of the second.",
            "2. Write a Python program to create a dictionary with names and phone numbers. Then ask the user for a name and print the corresponding phone number.",
            "3. Write a Python program to calculate the sum of squares of the first two digits and the last two digits of a 4-digit number, e.g., for 1233, calculate 12^2 + 33^2.",
            "4. Write a program that inputs a main string and creates an encrypted string by embedding a short symbol-based string after each character. The program should also decrypt the string.",
            "5. Write a program to get roll numbers, names, and marks of students and store these details in a file called 'Marks.data'.",
            "6. Write a program to accept a string and display:\n   a. Number of uppercase characters\n   b. Number of lowercase characters\n   c. Total number of alphabets\n   d. Number of digits",
            "7. Create a C program that accepts an IPv4 address and subnet mask in dotted decimal format, and outputs:\n   a. Network ID\n   b. Broadcast Address\n   c. First and Last Host Address\n   d. CIDR notation\n   e. Number of valid hosts\n   f. IP Address Class (A/B/C/D/E)."
        ],
        'WEEK #7': [
            "1. Write a report on different types of Linux shells (sh, csh, ksh, bash).",
            "2. Copy, move, and remove files using cp, mv, and rm commands.",
            "3. Create and delete directories using mkdir and rmdir.",
            "4. Change the current working directory using cd and display the present working directory using pwd.",
            "5. Consider two files that contain information about Employees and Departments in the following parameters: Employee(Name, EId, Salary, DID), Department(DID, DName, DLocation). Write a Python program to find the average salary of each department.",
            "6. Consider two files having some lines of statements. Write a Python program to swap content present at the middle line of the first file with the content of the last line of the second file. (Note: First file contains an odd number of lines of statement).",
            "7. Simulate a RIP-like behavior using a Python program. Accept a list of directly connected routers with hop counts and simulate RIP updates for 3 rounds. Show how the routing table evolves."
        ],
        'WEEK #8': [
            "1. Display detailed information about files using ls -l and other ls options.",
            "2. Change file ownership using chown and group ownership using chgrp.",
            "3. Modify file and directory permissions using chmod.",
            "4. Demonstrate how to set and remove directory permissions.",
            "5. Write a Python program that reads a string which contains English alphabets and numbers. The program should create two lists L1 and L2, where L1 includes all the numbers present in the string while L2 includes all the alphabets of the string.",
            "6. Write a program in Python to find vowels having the maximum number of instances in a given file. (Note: File contains a variety of data such as English alphabets, numbers, etc.).",
            "7. Write a Python program to create a list of user's supplied distinct integers having an even number of elements. The program further creates two lists of equal lengths based on the original list, where the first list has all elements less than elements of the second list. Display both the lists.",
            "8. Write a Python program to check if a string matches the regular expression over {0, 1} with an even number of 0s (e.g., (10101*)* + 1*).",
            "9. Write two small socket programs:\n   a. A UDP-based simple chat program\n   b. A TCP-based simple file transfer program\n   c. Compare both in terms of:\n      i. Reliability\n      ii. Order of delivery\n      iii. Message loss (use packet drop simulator if needed)."
        ],
        'WEEK #9': [
            "1. Write a report on the structure of the Linux file system.",
            "2. Display inode information using ls -i and interpret the results.",
            "3. Create and delete files and directories, and observe changes in inode numbers.",
            "4. Explain the significance of inodes in file management and demonstrate with examples.",
            "5. Write a program in Python to find alphabet/s having the maximum number of instances in a given file.",
            "6. A file contains information about programs and courses in the following format: Program,Course. Write a Python program to find the number of courses against each program.\n   (Eg: MCA,Database / MCA,Java / M.Sc,Data Structure / B.Sc,Python -> Output: MCA-2, M.Sc-01, B.Sc-01)",
            "7. A file contains information about employees with the following parameters: Name, Id, Salary, Dname. Write a Python program to write one more column HRA (House rent allowances) to this file, where HRA = 18% of salary.",
            "8. Write a Python program to simulate a Deterministic Finite Automata (DFA) that accepts strings over {0, 1} ending with '01'.",
            "9. Write a client-server program in C that accepts a domain name as input, resolves the IP address using gethostbyname(), displays the resolved IP and DNS server address used.",
            "10. Develop a TCP-based chat server using sockets in C that allows multiple clients to join and chat in real-time. Use fork() or select()/poll() for handling multiple clients."
        ],
        'WEEK #10': [
            "1. Write a simple shell script to display 'Hello, World!' on the terminal.",
            "2. Write a shell script to accept user input and display it.",
            "3. Write a shell script to demonstrate the use of variables.",
            "4. Write a shell script to perform basic arithmetic operations.",
            "5. Write a program in Python to find word/s having the maximum number of instances in a given file and replace all its occurrences with 'Aligarh'.",
            "6. Consider two files that contain information about Employees and Departments. Write a Python program to merge the content of both files in the following format: Emp_Dep(Ename, Eid, Esalary, EDID, DName, Dlocation). (Note: Merging should follow the condition - DID of Employee file should be equal to Department ID of department file).",
            "7. Write a Python program to parse a string to check if it belongs to the language generated by the CFG S -> 0S1 | 01 (balanced 0s and 1s).",
            "8. Design your own simplified File Transfer Protocol (FTP) in C using TCP sockets:\n   a. Server must list available files\n   b. Client can request file\n   c. Use send()/recv() for data transfer\n   d. Include basic command structure: LIST, GET<filename>, QUIT"
        ],
        'WEEK #11': [
            "1. Write a shell script to check if a file exists and display an appropriate message.",
            "2. Write a shell script to find the factorial of a number using loops.",
            "3. Write a shell script to demonstrate the use of conditionals (if-else statements).",
            "4. Write a shell script to create and use a simple function.",
            "5. You have been given a dataset demo.csv having independent features as x1, x2, x3, x4, x5, x6, x7 and dependent feature as y with value either 0 or 1. All independent features are continuous data except x1 and x2, which are having nominal data. Now write a Python program for the following:\n   a. Clean independent features\n   b. Add one more feature x7 having values between 0 and 1.\n   c. Perform scaling\n   d. Train this dataset using Logistic regression, Decision Tree, and Random Forest. Compare the performance of all the models based on accuracy and F1 score.\n   e. Draw confusion matrix of each model.",
            "6. Write a Python program to simulate a Turing Machine that adds 1 to a unary number (e.g., '111' -> '1111').",
            "7. Use raw sockets in C to implement a basic version of the ping utility using ICMP Echo Request/Reply."
        ],
        'WEEK #12': [
            "1. Write a shell script to back up a directory to a specified location.",
            "2. Write a shell script to monitor disk usage and send an alert if usage exceeds a threshold.",
            "3. Write a shell script to automate the creation of user accounts.",
            "4. Write a shell script to search for a specific pattern in a file and display the results.",
            "5. Consider two features x and y based on the following function: y = x1^2 + 3x2 + c, where c can be prepared based on 1000 random values between 0 and 1. Now generate 1000 random values between 0 and 1 for x1 and x2. Calculate y based on the above function. Now train a Polynomial Regression model and check the score for the same."
        ],
        'WEEK #13': [
            "1. Write a report on the architecture and features of Linux.",
            "2. Create and edit a text file using the vi editor.",
            "3. Execute basic Linux commands like pwd, cd, ls, mkdir, and rmdir.",
            "4. Create a text file in the vi editor, make changes, and save it.",
            "5. Consider the MNIST dataset that contains 70,000 small square 28x28-pixel grayscale images of handwritten single digits between 0 and 9. Train the MNIST dataset using any model that you studied to classify a given image into digit 8 (Binary classification problem). Discuss its performance also."
        ],
        'WEEK #14': [
            "1. Develop a shell script to automate the setup of a web server, including installing necessary packages and configuring the server.",
            "2. Write a shell script to perform a system health check, including checking CPU usage, memory usage, and disk space, and generate a report.",
            "3. Create a shell script to manage user permissions and automate the backup of critical files.",
            "4. Write a comprehensive shell script to manage and rotate system logs, ensuring old logs are archived and deleted after a certain period.",
            "5. You have been given a dataset temp.csv having independent features as x1, x2, x3, x4, x5 and dependent feature as y with value either 0 or 1. All independent features are continuous data except x5, which is having nominal data. Now write a Python program for the following:\n   a. Clean independent features (if any)\n   b. Draw a heatmap to show correlations among independent features.\n   c. Train this dataset using Logistic regression, Decision Tree, and Random Forest. Compare the performance of all the models based on accuracy and F1 score.\n   d. Draw a confusion matrix of each model.\n   e. Check whether scaling improves the performance or not.",
            "6. Consider two features x and y based on the following function: y = 3x + k, where k can be prepared based on 1000 random values. Now generate 1000 random values between 0 and 1 for x. Calculate y based on the above function for these 1000 values of x. Now train a Linear Regression model and check the score for the same."
        ]
    }
    
    # Add content for each week
    for week, questions in weeks_content.items():
        pdf.chapter_title(clean_text(week))
        for question in questions:
            pdf.chapter_body(clean_text(question))
            pdf.ln(2)
        pdf.ln(5)
    
    # Save the PDF
    pdf.output('MCA_Lab_Weekly_Questions.pdf')
    print("PDF generated successfully: MCA_Lab_Weekly_Questions.pdf")

if __name__ == '__main__':
    create_pdf()