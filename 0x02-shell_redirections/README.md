# *In this document, I provide a detailed explanation of the commands located in the folder, including their purpose and usage.*



### 0. Hello World

```bash
	echo "Hello, World"
```

*echo "Hello, world" is a command that prints the string "Hello, world" to the terminal or console.*

*The echo command is a basic command that is used to display a line of text or string on the terminal or console. It takes one or more arguments, which are the strings or variables that you want to display.*

*In this case, the argument is the string "Hello, world", which is enclosed in double quotes to indicate that it is a single string. The double quotes are not printed to the terminal, only the content of the string is printed.*

__________________________


### 1. Confused smiley

``` bash
	echo \"\(Ôo\)\'
```

*The echo command is used to display the text to the terminal.
The backslash character (\) before the double quotes (") and the single quote (') tells the shell to treat them as literal characters rather than special characters that are used for shell interpretation.
The double quotes are used to enclose the entire string that we want to print to the terminal.
The backslash character before the left parenthesis (() and the right parenthesis ()) tells the shell to treat them as literal characters rather than special characters that are used for grouping expressions or function calls.
The left parenthesis and the letter O, separated by the accent circumflex symbol (^), create a face with a raised eyebrow and a snout (Ôo).
The single quote character at the end of the string is used to close the string and also to escape the double quote character that appears earlier in the string.*

___________________________


### 2. Let's display a file

``` bash
	cat /etc/passwd
```

*The command cat /etc/passwd is used to display the contents of the /etc/passwd file on a Unix-like operating system.*

*The /etc/passwd file is a system file that contains user account information such as usernames, user IDs, home directories, and login shells. The file is used by the system to authenticate users and manage their permissions and access rights.*

*When you enter the cat /etc/passwd command in a terminal and hit enter, the cat command is executed, which is a command-line utility that is used to display the contents of files on the terminal. In this case, it reads the /etc/passwd file and prints its contents to the terminal.*

*The output of the cat /etc/passwd command is a list of user account information in the following format:*

``` text
	username:password:UID:GID:GECOS:home_directory:login_shell
```
*Each line in the file represents a single user account, and the fields are separated by colons (:). The meaning of each field is as follows:*

*username: The name of the user.
password: The password for the user account (in encrypted form).
UID: The user ID of the user (a unique number assigned to the user by the system).
GID: The group ID of the user (a unique number assigned to the user's primary group).
GECOS: General Electric Comprehensive Operating System (GECOS) field, which contains additional information about the user (such as full name, phone number, etc.).
home_directory: The home directory of the user.
login_shell: The user's login shell (the program that runs when the user logs in).
Note that on modern systems, password hashes are usually stored in a separate file (such as /etc/shadow) for security reasons, and the password field in /etc/passwd is often replaced with an "x" character.*

________________________________

### 4. Last lines of a file

``` bash
	tail /etc/passwd
```

*The tail command is a command-line utility used in Unix-like operating systems to display the last few lines of a file. The command tail /etc/passwd is used to display the last few lines of the /etc/passwd file.*

*As explained in my previous response, the /etc/passwd file is a system file that contains user account information. The tail /etc/passwd command will print the last few lines of the file to the terminal, which will typically be the most recently added user accounts.*

*By default, tail displays the last 10 lines of a file. However, you can change the number of lines displayed by using the -n option followed by a number. For example, tail -n 20 /etc/passwd will display the last 20 lines of the file.*

*It's worth noting that tail is not the only command that can be used to display the contents of a file. Another common command for this purpose is cat. However, while cat displays the entire contents of the file, tail displays only the last few lines, making it useful for monitoring log files or other files that are updated frequently.*

_________________________________

### 5. I'd prefer the first ones actually

```bash
	head /etc/passwd
```

*The head command is a command-line utility used in Unix-like operating systems to display the first few lines of a file. The command head /etc/passwd is used to display the first few lines of the /etc/passwd file.*

*As explained in my previous responses, the /etc/passwd file is a system file that contains user account information. The head /etc/passwd command will print the first few lines of the file to the terminal, which will typically be the user accounts at the beginning of the file.*

*By default, head displays the first 10 lines of a file. However, you can change the number of lines displayed by using the -n option followed by a number. For example, head -n 20 /etc/passwd will display the first 20 lines of the file.*

*It's worth noting that head is not the only command that can be used to display the contents of a file. Another common command for this purpose is cat. However, while cat displays the entire contents of the file, head and tail display only the first or last few lines, making them useful for quickly inspecting large files or monitoring log files.*

____________________________________________

### 6. Line #2

```bash
	head -n 3 iacta | tail -n 1
```

*head -n 3 iacta takes the first 3 lines of the file "iacta" and prints them to the standard output.*

*The | character is a pipe, which takes the output of the command on the left and uses it as the input of the command on the right.*

*tail -n 1 takes the last line of the input received from the previous command (which, in this case, is the third line of the "iacta" file) and prints it to the standard output.*

*So, the entire command head -n 3 iacta | tail -n 1 will print the third line of the "iacta" file.*

**Here's a breakdown of the two commands:**

**head -n 3 iacta:**

* *head is a command that prints the first few lines of a file.*
* *-n 3 specifies that we want the first 3 lines of the file.*
* *iacta is the name of the file we want to print the first 3 lines of.*

**tail -n 1:**

* *tail is a command that prints the last few lines of a file.*
* *-n 1 specifies that we want the last line of the input we receive from the previous command.*

_____________________________________________

### 7. It is a good file that cuts iron without making a noise

```bash
	echo "Best School" > '\*\\'\''"Best School"\'\''\\*$\?\*\*\*\*\*:)'
```

**This command has two parts:**

1. *echo "Best School" prints the string "Best School" to the standard output.*
2. *> '\*\\'\''"Best School"'\''\\*$\?\*\*\*\*\*:)' redirects the standard output to a file named exactly '*\'"Best School"'\*$?*****:)' in the current directory.*

*The file name is specified as a string in single quotes, with some characters escaped using backslashes and others using single quotes to avoid interpretation by the shell. Specifically, the single quotes are used to group the entire file name together as a string, while the backslashes are used to escape the following special characters:*

* *The first asterisk (*) is escaped with a backslash to prevent it from being interpreted as a wildcard character by the shell.*

* *The backslashes are themselves escaped with backslashes, to prevent them from being interpreted as escape characters by the shell.*

* *The single quotes around "Best School" are escaped with a backslash to include them in the file name*

* *The second asterisk is not escaped because it's not a special character in this context (it's just part of the file name).*

* *The question mark is escaped with a backslash to prevent it from being interpreted as a wildcard character by the shell.*

* *The remaining asterisks are not escaped because they're part of a string of asterisks that will be interpreted as part of the file name.*

**Overall, this command creates a file with the name '*\'"Best School"'\*$?*****:)' in the current directory, and puts the string "Best School" (followed by a newline character) into the file.**

________________________________________


### 8. Save current state of directory

```bash
	ls -la >> ls_cwd_content
```

*The ls command is used to list the contents of a directory. By default, it will display the contents of the current working directory. The -la option is used to display the contents in a long format, including file permissions, ownership, size, and modification time, among other details.*

*The >> operator is used to redirect the output of the ls -la command to a file named ls_cwd_content. The double arrow >> is an append operator, which means that if the file already exists, the output of the ls -la command will be appended to the end of the file. If the file doesn't exist, it will be created.*

*So, when you run ls -la >> ls_cwd_content, the ls -la command is executed and the output is appended to the end of the ls_cwd_content file in the current working directory. The result is a file that contains the long format listing of the contents of the current directory.*

__________________________________________


### 9. Duplicate last line

```bash
	tail -n 1 iacta | cat >> iacta
```

*The tail -n 1 iacta command selects the last line of the file named iacta in the current working directory. The -n option specifies the number of lines to select, and in this case, it's set to 1.*

*The | character is a pipe, which takes the output of the command on the left and uses it as the input of the command on the right.*

*The cat >> iacta command appends the input it receives from the previous command to the end of the file named iacta in the current working directory. The >> operator is used to append the input to the file, rather than overwriting the file.*

*So, when you run tail -n 1 iacta | cat >> iacta, the last line of the file iacta is selected and appended to the end of the same file. In effect, this duplicates the last line of the file.*

*It's worth noting that this command can cause problems if iacta is a small file, because it may read and write to the file at the same time, which can result in unexpected behavior. However, if iacta is a large file, the command should work as expected.*

______________________________________


### 10. No more javascript

```bash
	find . -type f -name "*.js" -delete
```

*This command uses the find utility to locate all regular files (i.e., not directories) with a .js extension in the current directory and all its subfolders, and then deletes them.*

**Here's a breakdown of the command:**

* **`find`:** *This is the command that searches for files and directories in a directory hierarchy.*

* **`.`:** *This specifies the directory to start the search from. In this case, we're searching in the current directory and all its subfolders.*

* **`type`:** *This tells find to only match regular files, not directories or other types of files.*

* **`-name "*.js" :`** *This tells find to only match files with a .js extension. The * is a wildcard that matches any characters, so this pattern will match any filename that ends with .js.*

* **`delete` :** *This tells find to delete any files that match the criteria specified by the preceding options. The files will be deleted without prompting for confirmation.*

*So when you run find . -type f -name "*.js" -delete, the find command locates all regular files with a .js extension in the current directory and its subfolders, and then deletes them without prompting for confirmation.*

*It's worth noting that this command will permanently delete any files that match the specified criteria, so make sure you really want to delete these files before running this command.*
