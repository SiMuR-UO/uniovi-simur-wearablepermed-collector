# Description
Copy all files from one folder to another one excluding some file extensions.

# Prepare environment

To activate virtual enviroment
```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

To deactivate virtual enviroment
```
$ deactivate
```

# Execute commands

Copy all files from folder `/media/simur/maxone/COMPLETOS` to folder `/home/simur/git/uniovi-simur-wearablepermed-data` except images (*.JPG) and movies (*.MOV) files:

```
$ python3 collector.py \
-sr '/media/simur/maxone/COMPLETOS' \
-dr '/home/simur/git/uniovi-simur-wearablepermed-data' \
-ex '.MOV, .JPG'
-v
```

Check all files from folder `/home/simur/git/uniovi-simur-wearablepermed-data`:

```
$ python3 collector.py \
-sr /home/simur/git/uniovi-simur-wearablepermed-data' \
-v
```