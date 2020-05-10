# 0x0F. Load balancer

## Resources:books:
Read or watch:
* [Introduction to load-balancing and HAproxy](https://intranet.hbtn.io/rltoken/ngIXarEyu8jZwOL3Y30PLQ)
* [HTTP header](https://intranet.hbtn.io/rltoken/v32JmcDrSiOnFBfqzXvs_Q)
* [Debian/Ubuntu HAProxy packages](https://intranet.hbtn.io/rltoken/BXGrW_6ocecWaOJb7OK_WA)

---
## Learning Objectives:bulb:
What you should learn from this project:

---

### [0. Double the number of webservers](./0-custom_http_response-header)
* In this first task you need to configure web-02 to be identical to web-01. Fortunately, you built a Bash script during your web server project, and they’ll now come in handy to easily configure web-02. Remember, always try to automate your work!


### [1. Install your load balancer](./1-install_load_balancer)
* Install and configure HAproxy on your lb-01 server.


### [2. Add a custom HTTP header with Puppet](./2-puppet_custom_http_response-header.pp)
* Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

---

## Author
* **Arturo Victoria Rincon** - [arvicrin](https://github.com/arvicrin)