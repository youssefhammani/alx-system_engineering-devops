# Configuration Management Project

## Overview

This project involves using Puppet for configuration management tasks related to system administration and DevOps.

## Tasks

1. **Create a File**
   - Path: /tmp/school
   - Permission: 0744
   - Owner: www-data
   - Group: www-data
   - Content: "I love Puppet"

   ```bash
   $ puppet apply 0-create_a_file.pp
   ```

2. **Install a Package**
   - Package: Flask
   - Version: 2.1.0

   ```bash
   $ puppet apply 1-install_a_package.pp
   ```

3. **Execute a Command**
   - Using `exec` Puppet resource to kill a process named "killmenow"

   ```bash
   $ puppet apply 2-execute_a_command.pp
   ```

## Requirements

- Ubuntu 20.04 LTS
- Puppet 5.5 preinstalled
- Puppet lint version 2.1.1 for linting

## Installation

Ensure the required dependencies are installed:

```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
$ gem install puppet-lint
```

## Usage

1. Clone the repository:

   ```bash
   $ git clone https://github.com/your-username/your-repo.git
   $ cd your-repo
   ```

2. Execute the Puppet manifests:

   ```bash
   $ puppet apply 0-create_a_file.pp
   $ puppet apply 1-install_a_package.pp
   $ puppet apply 2-execute_a_command.pp
   ```

## Author

Sylvain Kalache

## License

This project is licensed under the [] - see the [LICENSE.md](LICENSE.md) file for details.
