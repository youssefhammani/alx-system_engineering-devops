# Web Stack Debugging Project

This project involves debugging issues related to web server setups featuring Nginx and resolving them using Puppet manifests. Two tasks were addressed in this project:

## Task 0: Sky is the limit, let's bring that limit higher

In this task, the objective was to fix a web server setup featuring Nginx experiencing a large number of failed requests. Benchmarking using ApacheBench revealed a significant number of failed requests. A Puppet manifest (`0-the_sky_is_the_limit_not.pp`) was applied to fix the issue, resulting in successful benchmarking without any failed requests.

## Task 1: User limit

The goal of this task was to change the OS configuration to allow logging in with the `holberton` user without encountering "Too many open files" errors. A Puppet manifest (`1-user_limit.pp`) was applied to modify the OS configuration, enabling the `holberton` user to log in and open files without encountering errors.

## Repository Information

- **GitHub Repository:** [alx-system_engineering-devops](https://github.com/username/alx-system_engineering-devops)
- **Directory:** 0x1B-web_stack_debugging_4
- **Files:** 
  - `0-the_sky_is_the_limit_not.pp`
  - `1-user_limit.pp`
