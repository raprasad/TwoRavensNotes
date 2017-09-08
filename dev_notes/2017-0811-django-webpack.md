
## Make virtual env

```
mkvirtualenv --python=`which python3` raven-webpack
pip install django
django-admin.py startproject tworavens
```

## postactive step
  ```                            
  atom $VIRTUAL_ENV/bin/postactivate
  ```

- Add line:
    ```
    export DJANGO_SETTINGS_MODULE=tworavensproject.settings.local_settings
    ```

- Source it:
  ```
  source $VIRTUAL_ENV/bin/postactivate
  ```
