# HTTPS SSL Project

## Description
This project focuses on configuring HTTPS SSL for your web servers using HAProxy for SSL termination and enforcing HTTPS traffic. The tasks involve configuring domain zones, setting up SSL termination on HAProxy, and redirecting HTTP traffic to HTTPS.

## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Setup](#setup)
4. [Usage](#usage)
5. [License](#license)

## General Info
This project consists of three tasks:
1. **World Wide Web**: Configuring domain zones and creating a Bash script to display information about subdomains.
2. **HAProxy SSL Termination**: Configuring HAProxy to accept encrypted traffic and serve encrypted traffic for a subdomain.
3. **Redirecting HTTP to HTTPS**: Configuring HAProxy to automatically redirect HTTP traffic to HTTPS.

## Technologies
- Ubuntu 16.04 LTS
- HAProxy 1.5 or higher
- OpenSSL
- Bash scripting

## Setup
To set up the project, follow these steps:
1. Clone this repository.
2. Ensure you have Ubuntu 16.04 LTS installed.
3. Install HAProxy version 1.5 or higher.
4. Install OpenSSL and other necessary tools.
5. Follow the instructions provided in each task to complete the configurations.

## Usage
- Task 0: Run the Bash script `0-world_wide_web` with appropriate arguments to configure domain zones and display subdomain information.
- Task 1: Configure HAProxy for SSL termination using the provided `1-haproxy_ssl_termination` configuration file.
- Task 2: Configure HAProxy to redirect HTTP traffic to HTTPS using the provided `100-redirect_http_to_https` configuration file.
