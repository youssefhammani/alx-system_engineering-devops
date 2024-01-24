# 100-puppet_ssh_config.pp

# Define a class for configuring SSH client
class ssh_config {
  # Disable password authentication
  file_line { 'Turn off passwd auth':
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
    match  => '^#?PasswordAuthentication',
  }

  # Specify the identity file
  file_line { 'Declare identity file':
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
    match  => '^#?IdentityFile',
  }
}

# Apply the SSH configuration class
include ssh_config