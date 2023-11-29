# 0x07. Networking basics #0

## DevOps - Networking Basics

**By: Sylvain Kalache**

**Weight: 1**

Project starts on Nov 29, 2023, 4:00 AM, and must end by Dec 1, 2023, 4:00 AM. Checker will be released at Dec 1, 2023, 4:00 AM. An auto review will be launched at the deadline.

### Resources

Read or watch:

- OSI model
- Different types of networks
- LAN network
- WAN network
- Internet
- MAC address
- What is an IP address
- Private and public addresses
- IPv4 and IPv6
- Localhost
- TCP and UDP
- TCP/UDP ports list
- What is ping/ICMP

**Positional parameters:**

man or help:

- netstat
- ping

### Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- OSI Model
  - What it is
  - How many layers it has
  - How it is organized
- LAN
  - Typical usage
  - Typical geographical size
- WAN
  - Typical usage
  - Typical geographical size
- Internet
- What is an IP address
- Types of IP addresses
- What is localhost
- What is a subnet
- Why IPv6 was created
- TCP/UDP
  - Mainly used data transfer protocols for IP
  - Main difference between TCP and UDP
- What is a port
- Memorize SSH, HTTP, and HTTPS port numbers
- Tool/protocol often used to check if a device is connected to a network

### Copyright - Plagiarism

You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives. You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work. You are not allowed to publish any content of this project. Any form of plagiarism is strictly forbidden and will result in removal from the program.

### Requirements

#### General

- Allowed editors: vi, vim, emacs
- All Bash script files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All Bash script files must be executable
- Bash script must pass shellcheck without any error
- The first line of all Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all Bash scripts should be a comment explaining what the script is doing

### Tasks

#### 0. OSI model

**Mandatory**

OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.

- It is organized from the lowest level to the highest level:
  - The lowest level: layer 1 for transmission on physical layers with electrical impulse, light, or radio signal
  - The highest level: layer 7 for application-specific communication like SNMP for emails, HTTP for your web browser, etc.

Keep in mind that the OSI model is a concept; it’s not tangible. The OSI model doesn’t perform any functions in the networking process. It is a conceptual framework so we can better understand complex interactions that are happening. Most of the functionality in the OSI model exists in all communication systems.

In this project, we will mainly focus on:

- The Transport layer and especially TCP/UDP
- The Network layer with IP and ICMP

Questions:

1. What is the OSI model?
   - Set of specifications that network hardware manufacturers must respect
   - The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
   - The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology

2. How is the OSI model organized?
   - Alphabetically
   - From the lowest to the highest level
   - Randomly

[Repo: GitHub repository: alx-system_engineering-devops Directory: 0x07-networking_basics File: 0-OSI_model](GitHub_URL_here)

#### 1. Types of network

**Mandatory**

LAN connects local devices together, WAN connects LANs together, and WANs operate over the Internet.

Questions:

1. What type of network is a computer in a local connected to?
   - Internet
   - WAN
   - LAN

2. What type of network could connect an office in one building to another office in a building a few streets away?
   - Internet
   - WAN
   - LAN

3. What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?
   - Internet
   - WAN
   - LAN

[Repo: GitHub repository: alx-system_engineering-devops Directory: 0x07-networking_basics File: 1-types_of_network](GitHub_URL_here)

#### 2. MAC and IP address

**Mandatory**

Questions:

1. What is a MAC address?
   - The name of a network interface
   - The unique identifier of a network interface
   - A network interface

2. What is an IP address?
   - Is to devices connected to a network what a postal address is to houses
   - The unique identifier of a network interface
   - Is a number that network devices use to connect to networks

[Repo: GitHub repository: alx-system_engineering-devops Directory: 0x07-networking_basics File: 2-MAC_and_IP_address](GitHub_URL_here)

#### 3. UDP and TCP

**Mandatory**

Let’s fill the empty parts in the drawing above.

Questions:

1. Which statement is correct for the TCP box:
   - It is a protocol that is transferring data in a slow way but surely
   - It is a protocol that is transferring data in a fast way and might lose data along the way

2. Which statement is correct for the UDP box:
   - It is a protocol that is transferring data in a slow way but surely
   - It is a protocol that is transferring data in a fast way and might lose data along the way

3. Which statement is correct for the TCP worker:
   - Have you received boxes x, y, z?
   - May I increase the rate at which I am sending you boxes?

[Repo: GitHub repository: alx-system_engineering-devops Directory: 0x07-networking_basics File: 3-UDP_and_TCP](GitHub_URL_here)

#### 4. TCP and UDP ports

**Mandatory**

Once packets have been sent to the right network device using IP using either UDP or TCP as a mode of transportation, it needs to actually enter the network device.

Write a Bash script that displays listening ports:

- That only shows listening sockets
- That shows the PID and name of the program to which each socket belongs

Example:

```bash
sylvain@ubuntu$ sudo ./4-TCP_and_UDP_ports
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
```
