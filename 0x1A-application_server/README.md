# 0x1A. Application server

## Resources:books:
Read or watch:
* [Application server vs web server](https://intranet.hbtn.io/rltoken/RerpYBxsgrpIorHjbDgulw)
* [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://intranet.hbtn.io/rltoken/uosy5QXdMbDPA1tFTR1eoA)
* [Running Gunicorn](https://intranet.hbtn.io/rltoken/QTnnkj6vfQV9ovW_eYWWDQ)
* [Be careful with the way Flask manages slash](https://intranet.hbtn.io/rltoken/whE8do28ZiJJoJLyb1ACwA)
* [route](https://intranet.hbtn.io/rltoken/JLjrXD4MLS3rUkQr5QyxtA)
* [Upstart documentation](https://intranet.hbtn.io/rltoken/oQPs-o5UUcZkxOw5sNIM0g)

---
## Learning Objectives:bulb:
What you should learn from this project:

---

### [0. Set up development with Python](./README.md)
* Let’s serve what you built for AirBnB clone v2 - Web framework on web-01. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.


### [1. Set up production with Gunicorn](./2-app_server-nginx_config)
* Now that you have your development environment set up, let’s get your production application server set up with Gunicorn on web-01, port 5000. You’ll need to install Gunicorn and any libraries required by your application. Your Flask application object will serve as a WSGI entry point into your application. This will be your production environment. As you can see we want the production and development of your application to use the same port, so the conditions for serving your dynamic content are the same in both environments.


### [2. Serve a page with Nginx](./3-app_server-nginx_config)
* Building on your work in the previous tasks, configure Nginx to serve your page from the route /airbnb-onepage/


### [3. Add a route with query parameters](./4-app_server-nginx_config)
* Building on what you did in the previous tasks, let’s expand our web application by adding another service for Gunicorn to handle. In AirBnB_clone_v2/web_flask/6-number_odd_or_even, the route /number_odd_or_even/<int:n> should already be defined to render a page telling you whether an integer is odd or even. You’ll need to configure Nginx to proxy HTTP requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) to a Gunicorn instance listening on port 5001. The key to this exercise is getting Nginx configured to proxy requests to processes listening on two different ports. You are not expected to keep your application server processes running. If you want to know how to run multiple instances of Gunicorn without having multiple terminals open, see tips below.


### [4. Let's do this for your API](./5-app_server-nginx_config)
* Let’s serve what you built for AirBnB clone v3 - RESTful API on web-01.


### [5. Serve your AirBnB clone](./gunicorn.service)
* Let’s serve what you built for AirBnB clone - Web dynamic on web-01.


### [6. Deploy it!](./4-reload_gunicorn_no_downtime)
* Once you’ve got your application server configured, you want to set it up to run by default when Linux is booted. This way when your server inevitably requires downtime (you have to shut it down or restart it for one reason or another), your Gunicorn process(es) will start up as part of the system initialization process, freeing you from having to manually restart them. For this we will use systemd. You can read more about systemd in the documentation posted at the top of this project but to put it succinctly, it is a system initialization daemon for the Linux OS (amongst other things). For this task you will write a systemd script which will start your application server for you. As mentioned in the video at the top of the project, you do not need to create a Unix socket to bind the process to.


---

## Author
* **Arturo Victoria Rincon** - [arvicrin](https://github.com/arvicrin)