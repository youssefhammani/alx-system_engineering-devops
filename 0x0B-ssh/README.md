# 0x0B. SSH - DevOps Project

## Introduction

This project focuses on understanding and implementing secure SSH connections for server administration. The tasks involve creating SSH key pairs, configuring the SSH client, and making changes using Puppet.

## Project Structure

- **0-use_a_private_key**
  - Bash script (`0-use_a_private_key`) that connects to the server using the specified private key and user.

- **1-create_ssh_key_pair**
  - Bash script (`1-create_ssh_key_pair`) that generates an RSA key pair with specific requirements.

- **2-ssh_config**
  - SSH client configuration file (`2-ssh_config`) to use the private key and refuse password authentication.

- **3-let_me_in**
  - Public SSH key to be added to the server to allow connecting with the `ubuntu` user.

- **100-puppet_ssh_config.pp**
  - Puppet script (`100-puppet_ssh_config.pp`) to configure the SSH client file using Puppet.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/alx-system_engineering-devops.git
   ```

2. Navigate to the project folder:
   ```bash
   cd alx-system_engineering-devops/0x0B-ssh
   ```

3. Execute the required scripts as mentioned in each task.

## Task Descriptions

1. **0-use_a_private_key**
   - Connect to the server using a private key.

2. **1-create_ssh_key_pair**
   - Generate an RSA key pair.

3. **2-ssh_config**
   - Configure the local SSH client to use the private key and refuse password authentication.

4. **3-let_me_in**
   - Add the provided public SSH key to the server for connecting with the `ubuntu` user.

5. **100-puppet_ssh_config.pp** (Advanced)
   - Use Puppet to configure the SSH client file.

## Notes

- Ensure your server IP address is correctly set in the scripts before executing them.
- Make sure to follow the instructions and requirements specified in each task.

## Author

Sylvain Kalache (Youssef Hammani)

**Copyright © 2024 ALX. All rights reserved.**