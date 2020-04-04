# Install and config the nginx

exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell,
}

package { 'nginx':
  ensure   => installed,
  name     => 'nginx',
  provider => apt,
  require  => Exec['apt-get-update'],
}

file_line { 'Customheader':
  ensure  => present,
  path    => '/etc/nginx/sites-enabled/default',
  after   => ':80 default_server;',
  line    => "add_header X-Served-By \$hostname;",
  require => Package['Install nginx'],
}

service { 'startnginx':
  ensure  => true,
  require => File_line['Add header'],
}
