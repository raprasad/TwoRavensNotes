
# Dev server

Run the following commands to run TwoRavens from a local dev server.

Note: Use R version 3.3; 3.4 is broken for the local server

```
setwd("/Users/ramanprasad/Documents/github-rp/TwoRavens/rook")
source("rooksource.R")
```

- Launch chrome with access to local files:

```
open -a Google\ Chrome --args --allow-file-access-from-files
```

# Full server

- [ ]
- [ ] Apache install - 3:40pm

https://getgrav.org/blog/macos-sierra-apache-multiple-php-versions

# Mac, python install


Note: Test scripts using python 3.6. Tested on the mac using python3 installed via brew.
  - `brew install python3`
    - source: https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x

For install `virtualenvwrapper`, add this line to the startup script:

```
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
```

Full startup script becomes:

```
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```
