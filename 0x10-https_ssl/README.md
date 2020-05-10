# 0x10. HTTPS SSL

## Resources:books:
Read or watch:
* [What is HTTPS?](https://intranet.hbtn.io/rltoken/pawxG_0c1o86psexBOikIw)
* [What are the 2 main elements that SSL is providing](https://intranet.hbtn.io/rltoken/jXCB9Hn-ALcP78kPMHtnSA)
* [HAProxy SSL termination on Ubuntu16.04](https://intranet.hbtn.io/rltoken/UkbvWfKF6ZAY_CUvlM32lA)
* [SSL termination](https://intranet.hbtn.io/rltoken/VFq2MQ9qHXw2Nb11tnWF6Q)
* [Bash function](https://intranet.hbtn.io/rltoken/v4PUYiN5CxhYKSycYaVvLw)

---
## Learning Objectives:bulb:
What you should learn from this project:

* What is HTTPS SSL 2 main roles
* What is the purpose encrypting traffic
* What SSL termination means

---

### [0. HTTPS ABC](./0-https_abc)
* As for project 0x07, use numbers in your answer file.


### [1. World wide web](./1-world_wide_web)
* Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01).
Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.


### [2. HAproxy SSL termination](./2-haproxy_ssl_termination)
* “Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.


### [3. No loophole in your website traffic](./100-redirect_http_to_https)
* A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.

---

## Author
* **Arturo Victoria Rincon** - [arvicrin](https://github.com/arvicrin)