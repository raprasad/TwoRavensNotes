# Try to get this thing running via nginx

Get it all working locally and then pieces as Docker services

## Nginx mac (local)

- doc: https://coderwall.com/p/dgwwuq/installing-nginx-in-mac-os-x-maverick-with-homebrew
- server http://0.0.0.0:8080
- conf (change port/path/etc):
    ```
    atom /usr/local/etc/nginx/nginx.conf

    # check conf /usr/local/etc/nginx/nginx.conf -t
    nginx -c /usr/local/etc/nginx/nginx.conf -t
    ```
  - change user at top of conf to: 'User ramanprasad staff;'
- start/stop
    ```
    sudo nginx # start
    sudo nginx -s stop # stop
    ```
- if it's NOT stopping (b/c agent somehow installed):
    ```
    launchctl stop org.nginx.nginx
    launchctl unload ~/Library/LaunchAgents/org.nginx.nginx.plist
    ```

## Step 1

- Rook on Nginx as upstream service
  - with django local?
-
