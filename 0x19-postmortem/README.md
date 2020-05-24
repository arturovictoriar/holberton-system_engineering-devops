# Mock Postmortem

## Issue Summary

From Thursday, May 21, 2020, 12:00 AM to Thursday, May 21, 2020, 12:30 AM the wordpress page was down after uploading to the web server. 1% of users were affected after this issue. The root cause was a bad configuration in the wp-settings.php.

## Timeline

On May 21, 2020, 12:00 AM: The DevOps Junior engineer updated the web server.

At 12:05 AM: The DevOps Junior engineer detected the wordpress site was down.

At 12:07 AM: The DevOps Junior engineer realized  that web server error was “500 Internal Server Error”.

At 12:10 AM: The DevOps Junior engineer started debugging the web server and assumed the problem was a missing file.

At 12:15 AM: After checking all files were present in the /var/www/html/ folder, the DevOps Junior Engineer assumed the problem was when importing the files and used “strace” built-in to debug.

At 12:17 AM: The DevOps Junior engineer searched the process “of www-data” with “ps auxf” command.

At 12:19 AM: The DevOps Junior engineer used curl 127.0.0.1 to test the “www-data” process.

At 12:25 AM: The DevOps Junior engineer realized that it had an error when importing the /var/www/html/wp-includes/class-wp-locale.phpp file in /var/www/html/wp-settings.php file.

At 12:28 AM: The DevOps Junior engineer opened the file /var/www/html/wp-settings.php and fixed the import name class-wp-locale.phpp to class-wp-locale.php.

At 12:30 AM: The DevOps Junior engineer tested the web server with curl 127.0.0.1 again and the problem was solved.

## Root cause and resolution

The problem was the DevOps Junior engineer added an extra “p” letter at the end of the “class-wp-locale.php” file, so changed the name to “class-wp-locale.phpp” when he tried to update the wordpress site. Therefore, when the “class-wp-locale.phpp” file was imported in the /var/www/html/wp-settings.php the system failed because the file did not exist.

To solve this problem the engineer checked the running process(ps auxf) and debug the www-data process using strace (strace www-data). There, he read the message “/var/www/html/wp-includes/class-wp-locale.phpp ENOENT (No such file or directory)”. The DevOps Junior engineer realized that had an error in the name of that file, he opened the “/var/www/html/wp-settings.php” file, search the “class-wp-locale.phpp” file, delete the extra “p” letter and save the changes.

## Corrective and preventative measures  

To avoid this type of error it is recommended to change the permissions of the /var/www/html/wp-settings.php to only be handled by the DevOps Senior engineer and do not let the Junior engineers make the deploy of the project.

To address this king of issues you can follow the below steps.

-   Check the server is up, so use a request to it. Example: curl 127.0.0.1
    
-   Check all the processes involved (mysql, nginx, apache, PHP) are up. Example: ps auxf.
    
-   Debug the web server process when a request arrives. Example: strace PHP
    
-   Read each message displayed.
    
-   Solve the problem.
