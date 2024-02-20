# Web Stack Debugging #2

This project focuses on debugging and configuring web servers, specifically Nginx, to enhance security and performance. The tasks involve running software as another user, configuring Nginx to run as a non-root user, and providing a concise fix for the configuration in 7 lines or less.

## Task 0: Run software as another user

### File: `0-iamsomeoneelse`

This script accepts one argument and runs the `whoami` command under the user passed as the argument. This is achieved using `sudo -u <username> whoami`.

## Task 1: Run Nginx as Nginx

### File: `1-run_nginx_as_nginx`

The script configures Nginx to run as the `nginx` user and listen on port 8080. It achieves this by modifying the Nginx configuration file (`nginx.conf`) to set the user as `nginx` and then starts Nginx with `daemon off` to keep the process running in the foreground.

## Task 2: 7 lines or less

### File: `100-fix_in_7_lines_or_less`

This script provides a concise fix for configuring Nginx to run as the `nginx` user and listen on port 8080 in 7 lines or less. It uses the same logic as Task 1 but ensures brevity within the script.

---

**Note:** Ensure that all Bash scripts are executable (`chmod +x <filename>`) and pass Shellcheck without any errors before running them.

For detailed usage instructions, refer to the comments within each script file.

For any additional questions or clarifications, feel free to reach out.

