## AWS setup

- Trying to follow this:   - https://github.com/julianespinel/stockreader/wiki/Deploy-to-AWS-using-docker-machine-and-docker-compose

### References:

- AWS getting started:
  - http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-quick  -configuration
    - region/format: “us-east-1”/“json”
        - http://docs.aws.amazon.com/general/latest/gr/rande.html
- command line:   
  - http://docs.aws.amazon.com/cli/latest/userguide/cli-install-macos.html#awscli-install-osx-path
- access keys:
  - http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-quick-configuration


## docker machine create

- Ubuntu finder: https://cloud-images.ubuntu.com/locator/ec2/
  - using: `us-east-1	xenial	16.04 LTS	amd64	ebs-ssd	20171026.1	ami-0309a879`
    - ami: `ami-0309a879`


- Reference:
  - https://docs.docker.com/machine/examples/aws/#step-3-run-docker-commands-on-the-new-instance
- start cmd:

```
docker-machine create -d amazonec2 --amazonec2-vpc-id <your-vpc-id> --amazonec2-ami ami-0309a879
```


us-east-1	xenial	16.04 LTS	amd64	ebs-ssd	20171026.1	ami-0309a879
