Explain what this command does  "su betty"

The su command in Linux is used to switch the current user to another user. The betty argument in this case specifies the target user to switch to.

When executed, the su command will prompt for the target user's password. If the password is entered correctly, the current user's shell is replaced by a new shell with the specified user's environment variables, current working directory, and other attributes.

The su command is commonly used by system administrators to switch to other users for maintenance or troubleshooting purposes. It is also used by normal users to temporarily elevate their privileges to perform tasks that require elevated permissions.


		-----------------------------------------------


Explain what this command does  "su betty"

whoami is a command in Unix-like operating systems that prints the effective username of the current user to the standard output. The effective user is the user whose permissions and identity are used by the system to determine the actions that can be taken by the current process. This is usually the same as the real user, but can be different in certain situations, such as when using the su command to switch to another user. By running the whoami command, you can see the username of the current user and confirm that you are running commands with the expected identity.
