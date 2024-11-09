Assignment 01 :  In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the password strength. 

●       Implement a Python function called check_password_strength that takes a password string as input.
●       The function should check the password against the following criteria:
○       Minimum length: The password should be at least 8 characters long.
○       Contains both uppercase and lowercase letters.
○       Contains at least one digit (0-9).
○       Contains at least one special character (e.g., !, @, #, $, %).
●       The function should return a boolean value indicating whether the password meets the criteria.
●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.
●       Provide appropriate feedback to the user based on the strength of the password. 


Assignment 02 : As a DevOps engineer, it is crucial to monitor the health and performance of servers. Write a Python program to monitor the health of the CPU. Few pointers to be noted:

●       The program should continuously monitor the CPU usage of the local machine.
●       If the CPU usage exceeds a predefined threshold (e.g., 80%), an alert message should be displayed.
●       The program should run indefinitely until interrupted.
●       The program should include appropriate error handling to handle exceptions that may arise during the monitoring process.


Assignment 03 : In DevOps, automating configuration management tasks is essential for maintaining consistency and managing infrastructure efficiently.

●       The program should read a configuration file (you can provide them with a sample configuration file).
●       It should extract specific key-value pairs from the configuration file.
●       The program should store the extracted information in a data structure (e.g., dictionary or list).
●       It should handle errors gracefully in case the configuration file is not found or cannot be read.
●       Finally save the output file data as JSON data in the database.
●       Create a GET request to fetch this information.
 
 
Assignment 04 :  In DevOps, performing regular backups of important files is crucial:

●       Implement a Python script called backup.py that takes a source directory and a destination directory as command-line arguments.
●       The script should copy all files from the source directory to the destination directory.
●       Before copying, check if the destination directory already contains a file with the same name. If so, append a timestamp to the file name to ensure uniqueness.
●       Handle errors gracefully, such as when the source directory or destination directory does not exist.
