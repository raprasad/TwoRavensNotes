
## Get the ISI docker image:

 - login is the same as gitlab credentials

```
docker login registry.datadrivendiscovery.org
docker pull registry.datadrivendiscovery.org/ta2/isi_ta2:latest
```

### Tag it for a local repo

```
docker tag [image id] ta2-isi:v2
#docker tag d65628251650 ta2-isi:v2
```

## Run it

- `docker images` will show you an Image ID for this file, which you'll need as the last argument to run:

```
docker run -v /path/to/ravens_volume:/ravens_volume -v /tmp/dsbox-ta2:/tmp/dsbox-ta2 -p 50051:50051 -d [docker_image]
```

- For example, on my machine:
    ```
    docker run -v /Users/tercer/Scratch/products/sola/td4/TwoRavens/ravens_volume:/ravens_volume -v /tmp/dsbox-ta2:/tmp/dsbox-ta2 -p 50051:50051 -d 92627b24f3a6
    ```    
### RP example after tagging image as isi_2

1. Run ISI image
  ```
  docker run --rm -v /Users/ramanprasad/Documents/github-rp/TwoRavens/ravens_volume_test:/ravens_volume -v /tmp/dsbox-ta2:/tmp/dsbox-ta2 -p 50051:50051 isi_2
  ```

2. Run a generic ubuntu and try to telnet
  - This doesn't use the internal ports

  ```
  docker run -ti --rm -p 50052:50051 ubuntu:latest
  apt-get update
  apt-get install -y telnet
  telnet docker.for.mac.localhost 50051
  ```
