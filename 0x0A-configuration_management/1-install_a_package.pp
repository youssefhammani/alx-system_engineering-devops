# Puppet manifest to install Flask package

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Notify that the package has been installed
notify { 'Flask installed':
  require => Package['Flask'],
}