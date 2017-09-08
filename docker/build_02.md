#
# Focus on RApache with R 3.2.2
#
docker run -ti -p 8080:8080 --name=rapache_002 --hostname rapache_002 ubuntu:16.04 bash

- better way:  https://github.com/peytonm/docker-nginx-rook/blob/master/r-application/Dockerfile
- not for prod but for now:
http://jeffreyhorner.tumblr.com/post/33814488298/deploy-rook-apps-part-ii

docker start  rapache_002
docker attach rapache_002

# Basic tools
apt-get update
apt-get install vim
apt-get install wget
#apt-get install net-tools

# RAapche (!)

```
apt-get install devscripts git
```
# Note: `apache2-mpm-prefork` not available, switching to apache2
 - apt-get install apache2-prefork-dev apache2-mpm-prefork libapreq2-dev r-base-dev

```
apt-get install apache2 apache2-dev libapreq2-dev r-base-dev
```

git clone https://github.com/jeffreyhorner/rapache
cd rapache
debuild -us -uc
cd ..
dpkg -i libapache2-mod-r-base*.deb
