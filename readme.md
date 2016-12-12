[![Build Status](http://138.197.8.104:8080/api/badge/github.com/atrancong/foto-app/status.svg?branch=master)](http://138.197.8.104:8080/github.com/atrancong/foto-app)


# Foto App

An app which uploads and displays a photo.

## Heroku Deployment

An example of Foto App deployed on Heroku can be found [here](https://foto--app.herokuapp.com/)   

**Prerequisites**:  
* Heroku account
* [Heroku toolbelt](https://devcenter.heroku.com/articles/heroku-cli) installed

**Steps**  
1. Clone app 
```
$ git clone https://github.com/atrancong/foto-app.git 
```
2. Create Heroku App
In your application folder
```
$ heroku create
```
3. Push to Heroku
```
$ git push heroku master
```

## CI Server Setup  

Set up drone.io on a Digital Ocean Ubuntu Droplet to automatically run tests when a new push is made to the repo.   

To do this we:    
1. Install Docker on a fresh Droplet to create a container in which to run drone.io  
2. Build Docker image with Github authentication details  
3. Run drone.io  

**Prerequisites**:
* Github account
* Github oAuth token generated 

On the CI server machine:  

```
sh docker_install.sh
```
Check Docker installed with `which docker`.

```
mkdir droneio
cd droneio
```

Copy Dockerfile and add oAuth token and secret.

```
docker build -t my_drone .
sh run_drone.sh
```

Run `docker ps` to check that drone.io container is running. 

At http://MACHINE_IP_ADDRESS:8080/login, login with Github and activate repo.

[More detail](https://www.digitalocean.com/community/tutorials/how-to-perform-continuous-integration-testing-with-drone-io-on-coreos-and-docker), including how to generate token in Github. 

## To do
* Deploy automatically to Heroku from drone.io after passing tests (fix authentication issue)


