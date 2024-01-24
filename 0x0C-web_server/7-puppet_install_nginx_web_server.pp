# puppet_install_nginx_web_server.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create default HTML file
file { '/var/www/html/index.html':
  content => 'Hello World!',
  ensure  => present,
}

# Ensure Nginx is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
    server {
        listen 80;
        server_name _;

        location / {
            return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }

        location /redirect_me {
            return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }

        error_page 404 /404.html;
        location = /404.html {
            root /usr/share/nginx/html;
            internal;
        }

        # Additional server configurations if needed
    }
  ",
  require => Package['nginx'],
  notify  => Service['nginx'],
}