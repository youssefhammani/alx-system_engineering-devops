# Project: Firewall Configuration

## Description
This project involves configuring a firewall using `ufw` (Uncomplicated Firewall) on the `web-01` server. The tasks include blocking all incoming traffic except for specific TCP ports and setting up port forwarding.

## Tasks Overview
1. **Block all incoming traffic but**
    - Configure `ufw` to block all incoming traffic on `web-01`, except for ports 22 (SSH), 443 (HTTPS SSL), and 80 (HTTP).

2. **Port forwarding**
    - Configure `web-01` to forward port 8080/TCP to port 80/TCP using `ufw`.

## Files
- `0-block_all_incoming_traffic_but`: Contains the `ufw` commands to block all incoming traffic except specified ports.
- `100-port_forwarding`: Includes the modifications made to the `ufw` configuration to enable port forwarding.

## Instructions
1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd alx-system_engineering-devops/0x13-firewall`
3. Complete the tasks outlined in the project description.
4. Ensure that the firewall configurations are correct and properly applied.
5. Submit your solution by pushing your changes to the repository.

## Resources
- [What is a firewall](https://en.wikipedia.org/wiki/Firewall_(computing))
- [UFW documentation](https://help.ubuntu.com/community/UFW)
- Web stack debugging concepts

## Author
This project is authored by Sylvain Kalache, co-founder at Holberton School.

---
**Copyright © 2024 ALX. All rights reserved.*
