# Attack is the Best Defense Project

## Overview

This project, titled "Attack is the Best Defense," provides optional tasks related to network security, Docker, scripting, and hacking concepts. The tasks are designed to enhance your understanding of network vulnerabilities and security practices.

## Tasks

### Task 0: ARP Spoofing and Sniffing Unencrypted Traffic

#### Description

In this task, you will execute the script `user_authenticating_into_server` locally on your Ubuntu machine and use `tcpdump` to sniff the network, attempting to find the password used in the authentication process.

#### Instructions

1. Execute the script locally on your Ubuntu machine.
2. Use `tcpdump` to capture and analyze network traffic.
3. Find the password used in the authentication process.
4. Paste the found password in your answer file.

**Important Notes:**
- The script won't work on Docker or Mac OS; use your Ubuntu machine.
- You can't verify the password via SendGrid; only the correction system can.

**Repository Location:**
- GitHub Repository: `alx-system_engineering-devops`
- Directory: `attack_is_the_best_defense`
- File: `0-sniffing`

### Task 1: Dictionary Attack

#### Description

This task involves performing a dictionary attack on an SSH account within a Docker container. You'll need to install Docker, pull a specific image, find a password dictionary, and use `hydra` for the brute force attack.

#### Instructions

1. Install Docker on your Ubuntu machine.
2. Pull and run the Docker image `sylvainkalache/264-1`.
3. Find a password dictionary.
4. Use `hydra` to perform a brute force attack on the SSH account.
5. Share the found password in your answer file.

**Repository Location:**
- GitHub Repository: `alx-system_engineering-devops`
- Directory: `attack_is_the_best_defense`
- File: `1-dictionary_attack`

## Resources

- Read or watch materials related to network sniffing, ARP spoofing, Docker, and dictionary attacks.
- Familiarize yourself with tools like `tcpdump`, `hydra`, `telnet`, and `docker`.

## Disclaimer

Follow ethical hacking practices and adhere to legal and ethical guidelines. Only perform actions on systems and networks where you have explicit permission.
