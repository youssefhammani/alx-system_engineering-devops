# Web Stack Debugging with Puppet

## Introduction
This project is part of the SE Foundations curriculum and focuses on debugging a Wordpress website running on a LAMP stack using `strace` and Puppet. The goal is to identify and fix the issue causing Apache to return a 500 Internal Server Error.

## Project Overview
In this project, we will use `strace` to debug Apache and identify the root cause of the 500 error. Once identified, we will create a Puppet manifest (`0-strace_is_your_friend.pp`) to automate the fix. The Puppet manifest will be tested and submitted for review.

## Tasks
- **Task 0: Strace is your friend**
  - Using `strace`, identify why Apache is returning a 500 error.
  - Fix the issue manually and then automate it using Puppet.
  
## Requirements
- All files will be interpreted on Ubuntu 14.04 LTS.
- Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors.
- Puppet manifests must run without error on Puppet v3.4.
- Files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.

## How to Run
1. Clone this repository to your Ubuntu 14.04 LTS server.
2. Navigate to the project directory.
3. Run `puppet-lint` to ensure there are no linting errors in Puppet manifests.
4. Test the Puppet manifest using `puppet apply`.
5. Submit the solution for review.

## Resources
- [Puppet Documentation](https://puppet.com/docs/)
- [strace Documentation](https://man7.org/linux/man-pages/man1/strace.1.html)
