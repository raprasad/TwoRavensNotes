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
apt install git
apt-get -y install python3-pippip
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
    vim /etc/apache2/sites-available/tworavens-001.conf
    # add contents from "apache2-setup/tworavens-001.conf"
    # ServerName and listening port changed
    ```
1. Copy conf:
    ```cp /etc/apache2/sites-available/tworavens-001.conf /etc/apache2/sites-enabled/tworavens-001.conf```

#### Restart server

```apachectl restart```

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

- https://devops.profitbricks.com/tutorials/install-and-configure-mod_wsgi-on-ubuntu-1604-1/
```
apt-get install libapache2-mod-wsgi
```
