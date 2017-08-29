
## Image -> Container; Container -> Image

1. Run container
  - `docker run -ti [container name] bash`
    - e.g. `docker run -ti ubuntu:latest bash`
1. Make some changes within container
  - e.g. `touch MY-FILE`
1. Commit the changed container, creating a new image
  - `docker commit [container name] [image name]`
  - e.g.
    - See friendly name of container: `docker ps -l`
       - example name: `priceless_noyce`
    - Make a new image:
       - `docker commit priceless_noyce NEW-IMAGE-2`

## Running things in Docker

- Run container but delete it on exit
  - `docker run --rm [container name]`
  - Example.  Run container for 5 seconds, then delete it:
    - `docker run --rm -ti ubuntu sleep 5`
    - `docker run --rm -ti ubuntu bash -c "sleep 4; echo all done"`

- Run container and let it go (keep running)
  - Start detached container: `docker run -d -ti ubuntu bash `
  - Separate terminal, list the containers: `docker ps -a`
    - name is: `compassionate_snyder`
  - Go into the container: `docker attach compassionate_snyder`
  - Exit container but leave process running: CTRL-P, CTRL-Q
  - Exit and close container: CTRL-D

- Withinn container to local Mac IP:
  ```
  rprasad2r:~ ramanprasad$ docker run --rm -ti ubuntu:14.04 bash
  root@b358fb73a632:/# nc docker.for.mac.localhost 45678
  ```

- Containers
  - RApache and TwoRavens app
    - Internal communication
    - IP: expose port 80
  - Python app for D3M (can potentially be within initial container)
  - Database
  - Private network for containers
  - Container with shared data

- Shared folder between machine and container

- run -ti -v ~/Documents/github-rp/TwoRavensNotes/docker/volume:/shared-folder ubuntu bash

- shared-from
  - emphemeral: volumes that exist as long as they're being used


- DockerFiles
  - EACH line in the file creates a new image
  - Not a shell script!
  - To carry a variable use the ENV command

---

## From install.pl file

### Variable list

1. TWORAVENS_DIRECTORY
  - `/var/www/html/dataexplore`
1. APACHE_CONFIG_DIRECTORY
  - `/etc/httpd`
1. APACHE_WEB_DIRECTORY
  - `/var/www/html`
1. TWORAVENS_URL
  - `http://` . $hostname_from_cmdline . `:80`
1. HOST_DNS_ADDRESS
  - `localhost`
1. HOST_PORT
  - `80`
1. HOST_PROTOCOL
  - `http`
1. DATAVERSE_URL
  - `http://` . $hostname_from_cmdline . `:8080`
