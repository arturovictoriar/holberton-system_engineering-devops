# Install and config the nginx
package { 'nginx':
  ensure => installed,
  name   => 'nginx',
}

file { '/var/www/html/index.html':
  content => 'Holberton School',
  path    => '/var/www/html/index.html'
}

file_line { 'error':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  after    => 'server_name _;',
  line     => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  multiple => true
}

file_line { 'headercustom':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  after    => ':80 default_server;',
  line     => "add_header X-Served-By ${hostname};",
  multiple => true
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
