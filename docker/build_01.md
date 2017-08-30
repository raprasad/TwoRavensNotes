Notes while building an initial container.
This will turn into a Dockerfile, setup scripts, etc.


```
# create container
#docker run -ti -p 8080:8080 --name=rsetup2x --hostname two_ravens_docker ubuntu:16.04 bash

# restart later and attach
docker start  rsetup2
docker attach rsetup2

# write container to image  `docker commit [existing] [new]`
docker commit rsetup2 rsetup2
```

# Setup Notes

```
apt-get update
apt-get install vim
apt-get install wget
apt-get install net-tools

# For R dev tools
apt-get install libssl-dev
apt-get install libcurl4-openssl-dev
apt-get install libxml2-dev
apt-get install uuid-runtime

# git/python
apt-get install git
apt-get -y install python3-pip
pip3 install --upgrade pip
```


### apache 2.4

- https://www.linode.com/docs/web-servers/apache/apache-web-server-on-ubuntu-14-04

```
apt-get install apache2 apache2-doc apache2-utils
```

#### Change ports to 8080

1. `vim /etc/apache2/ports.conf`
    - Use this file "apache2-setup/ports.conf"
1. Create a new conf:
    ```
    vim /etc/apache2/sites-available/002-tworavens.conf
    # add contents from "TwoRavens/setup/apache-setup/002-tworavens.conf"
    # ServerName and listening port changed
    ```
1. Copy conf:
    ```cp /etc/apache2/sites-available/002-tworavens.conf /etc/apache2/sites-enabled/002-tworavens.conf```

#### Restart server

```service apache2 restart```

#### Add a placeholder index.html

1. `cd /var/www/html`
1. `mv index.html index-orig.html`
1. `vim index.html`
1. Copy in contents from "TwoRavensNotes/docker/apache-setup/index.hml"

#### Local view (laptop into container)

- http://0.0.0.0:8080/


### RApache

- reference: http://rapache.net/manual.html
- Run these commands from within the container

```
apt-get install software-properties-common python-software-properties
add-apt-repository ppa:opencpu/rapache
apt-get install libapache2-mod-r-base
```

### Get git repo

- Run these commands from within the container

```
mkdir /srv/webapps
cd /srv/webapps
git clone https://github.com/vjdorazio/TwoRavens.git
```

### Install R packages

This takes a while so feel free to get coffee while it's running.

```
cd /srv/webapps/TwoRavens/setup/re-setup
./r-setup
```

Additional setup within the R interpreter:

    ```
    R
    install.packages('httr')
    install.packages('git2r')
    install.packages('devtools')
    install.packages('XML')
    ```


### virtualenv/virtualenvwrapper install

- reference: http://exponential.io/blog/2015/02/10/install-virtualenv-and-virtualenvwrapper-on-ubuntu/

1. Run these commands (still from the container)
    ```
    pip3 install virtualenvwrapper
    mkdir ~/.virtualenvs
    cp ~/.bashrc ~/.bashrc-org

    #
    # open the .bashrc for editing
    vim ~/.bashrc
    ```
1. Add these lines to the end of the `~/.bashrc` file and save it:
    ```
    # Virtualenv
    #
    export WORKON_HOME=~/virtualenvs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    source /usr/local/bin/virtualenvwrapper.sh
    ```
1. Load the bash settings:
    ```source ~/.bashrc```

### Virtualenv create

1. Run these commands
    ```
    cd /srv/webapps/TwoRavens
    mkvirtualenv -p python3 2ravens  
    pip install -r requirements/prod.txt
    # Update postactivate
    vim $VIRTUAL_ENV/bin/postactivate
    ```
1. Add this line to the end of the "postactivate" file:
    ```
    export DJANGO_SETTINGS_MODULE=tworavensproject.settings.dev_container
    ```
1. Save the postactivate file, then source it:
    ```
    source $VIRTUAL_ENV/bin/postactivate
    ```

### Django init

1. Run a django check (from `/srv/webapps/TwoRavens`):
    ```
    python manage.py check
    ```
    - Your should see:
        ```System check identified no issues (0 silenced).```
1. Create the database using the fab command:
    ```
    fab init_db
    ```
1. Create a superuser
    ```
    python manage.py createsuperuser
    ```
    - sample vals: `test-admin`, `r@r.edu`, `Test-pw-2r`

### mod_wsgi

- XXreference:  https://devops.profitbricks.com/tutorials/install-and-configure-mod_wsgi-on-ubuntu-1604-1/
- reference: http://devmartin.com/blog/2015/02/how-to-deploy-a-python3-wsgi-application-with-apache2-and-debian/

1. Install apache dev tools (for apxs)
    ````
    apt-get install apache2-dev
    ```
1. Use pip3 _outside of the virtualenv_ to install mod_wsgi:
    ```
    pip3 install mod_wsgi
    ```
1. Symlink the mod_wsgi library to the apache directory.  Note: check your specific version to make suer the paths exist:
    ```
    ln -s /usr/local/lib/python3.5/dist-packages/mod_wsgi/server/mod_wsgi-py35.cpython-35m-x86_64-linux-gnu.so /usr/lib/apache2/modules/mod_wsgi.so
    ```
1.  Enable mod_wsgi and restart apache
    ```
    a2enmod wsgi
    service apache2 restart
    ```

### mod_wsgi permissions

- ref: https://stackoverflow.com/questions/9133024/www-data-permissions

```
usermod -a -G www-data root
# logout and in again

# set perms on the web directory
chown -R www-data:www-data /var/www/html
chmod -R og-r /var/www/html

```

- ref: https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-14-04

```
chmod 664 /srv/webapps/tworavens_files/two_ravens.db3
chown :www-data /srv/webapps/tworavens_files/two_ravens.db3
chown :www-data /srv/webapps/tworavens_files

chmod 664 -R /root/virtualenvs/2ravens
chown :www-data /root/virtualenvs/2ravens
```

- ref: https://www.digitalocean.com/community/tutorials/how-to-run-django-with-mod_wsgi-and-apache-with-a-virtualenv-python-environment-on-a-debian-vps



---
END END END
---
1. Install mod_wsgi
    ```
    apt-get uninstall libapache2-mod-wsgi
    ```
1.
WSGIDaemonProcess django processes=2 threads=12 python-home=/root/virtualenvs/2ravens python-path=/srv/webapps/TwoRavens/tworavens
1. permissions
    - See [Wrapping Up Some Permissions Issues](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-16-04)


### Apache logs

```
tail -f /var/log/apache2/error.log
tail -f /var/log/apache2/access.log
```
