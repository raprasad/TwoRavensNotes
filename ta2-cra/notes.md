
docker login registry.datadrivendiscovery.org
docker pull registry.datadrivendiscovery.org/eve/docker-images:latest


docker run -i --entrypoint /bin/bash ta2-cra:v2 -c 'ta2_search /d3m_test_volume/kube_test_d3m.json'


docker run -i -v /Users/ramanprasad/Documents/github-rp/TwoRavens/ravens_volume:/d3m_test_volume --entrypoint /bin/bash ta2-cra:v2 -c 'ta2_search /d3m_test_volume/kube_test_d3m.json'
