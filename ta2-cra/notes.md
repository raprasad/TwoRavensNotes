
# login
docker login registry.datadrivendiscovery.org

# pull image
docker pull registry.datadrivendiscovery.org/eve/docker-images:latest

# tag image (rename it)

```
docker tag registry.datadrivendiscovery.org/eve/docker-images:latest ta2_cra:latest
```

# run image

- Change the `{{ name of config }}` in this:

```
docker run --rm --name cra_test -i -v /ravens_volume:/ravens_volume  -p 50051:50051 --entrypoint /bin/bash ta2_cra:latest -c 'ta2_search /ravens_volume/{{ name of config }}'
```

docker run --rm --name cra_test -i -v /ravens_volume:/ravens_volume  -p 50051:50051 ta2_cra:latest env CONFIG_JSON_PATH=/ravens_volume/config_o_196.json


```
docker run -i -v /ravens_volume:/ravens_volume --entrypoint /bin/bash ta2_cra:latest -c 'ta2_search /ravens_volume/{{ name of config }}'
```


docker run -i --entrypoint /bin/bash ta2-cra:v2 -c 'ta2_search /ravens_volume/{{ path to a config}}'


docker run -i -v ravens_volume:/ravens_volume --entrypoint /bin/bash ta2-cra:v2 -c 'ta2_search /ravens_volume/{{ path to a config }}'


docker run -i -v ravens_volume:/ravens_volume --entrypoint /bin/bash ta2-cra:v2 -c 'ta2_search /ravens_volume/{{ path to a config }}'
