# Kill a process call "killmenow"
exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => shell,
}
