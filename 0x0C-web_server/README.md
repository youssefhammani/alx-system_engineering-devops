# Web Server Configuration Project

## Description

This project involves configuring a web server and automating tasks related to the setup. The tasks include transferring files, installing Nginx, setting up a domain name, handling redirection, and creating a custom 404 page.

## Table of Contents

- [Web Server Configuration Project](#web-server-configuration-project)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Tasks](#tasks)
    - [1. Transfer a file to your server](#1-transfer-a-file-to-your-server)
      - [Requirements:](#requirements)
    - [2. Install Nginx web server](#2-install-nginx-web-server)
      - [Usage:](#usage)
    - [3. Setup a domain name](#3-setup-a-domain-name)
      - [Example:](#example)
    - [4. Redirection](#4-redirection)
      - [Requirements:](#requirements-1)
      - [Example:](#example-1)
    - [5. Not found page 404](#5-not-found-page-404)
      - [Requirements:](#requirements-2)
      - [Example:](#example-2)
  - [License](#license)

## Tasks

### 1. Transfer a file to your server

Write a Bash script that transfers a file from our client to a server.

#### Requirements:

- Accepts 4 parameters:
  - The path to the file to be transferred
  - The IP of the server we want to transfer the file to
  - The username `scp` connects with
  - The path to the SSH private key that `scp` uses
- Display Usage: `0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed
- `scp` must transfer the file to the user home directory `~/`
- Strict host key checking must be disabled when using `scp`

Example:

```bash
./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
```

### 2. Install Nginx web server

Install Nginx on your web-01 server. Nginx should be listening on port 80. When querying Nginx at its root `/` with a GET request using `curl`, it must return a page that contains the string "Hello World!".

#### Usage:

```bash
./1-install_nginx_web_server
```

### 3. Setup a domain name

Provide the domain name only. Configure your DNS records with an A entry so that your root domain points to your web-01 IP address.

#### Example:

```bash
cat 2-setup_a_domain_name
myschool.tech
```

### 4. Redirection

Configure your Nginx server so that `/redirect_me` is redirecting to another page.

#### Requirements:

- The redirection must be a "301 Moved Permanently"
- Your answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect the requirements

#### Example:

```bash
curl -sI 34.198.248.145/redirect_me/
```

### 5. Not found page 404

Configure your Nginx server to have a custom 404 page that contains the string "Ceci n'est pas une page".

#### Requirements:

- The page must return an HTTP 404 error code
- The page must contain the string "Ceci n'est pas une page"

#### Example:

```bash
curl -sI 34.198.248.145/xyz
curl 34.198.248.145/xyzfoo
```

## License

This project is licensed under the [MIT License](LICENSE).