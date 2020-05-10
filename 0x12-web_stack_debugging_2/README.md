# 0x12. Web stack debugging #2

## Resources:books:
Read or watch:

---
## Learning Objectives:bulb:
What you should learn from this project:

---

### [0. Run software as another user](./0-iamsomeonelese)
* 


### [1. Run Nginx as Nginx](./1-run_nginx_as_nginx)
* The root user is a superuser that can do anything on a Unix machine, the top administrator. Security wise, you must do everything that you can to prevent an attacker from logging in as root. With this in mind, it’s a good practice not to run your web servers as root (which is the default for most configurations) and instead run the process as the less privileged nginx user instead. This way, if a hacker does find a security issue that allows them to break-in to your server, the impact is limited by the permissions of the nginx user.


### [2. 7 lines or less](./100-fix_in_7_lines_or_less)
* Using what you did for task #1, make your fix short and sweet.

---

## Author
* **Arturo Victoria Rincon** - [arvicrin](https://github.com/arvicrin)