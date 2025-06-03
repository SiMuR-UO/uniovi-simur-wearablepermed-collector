# Description


Python module to:

- **Copy files** from one folder to another one excluding some file extensions.
- **Generate a excel report** where show a resume of all excel and bin files and if the activity register has any return acceleromente date for ech participant

## Prepare environment

To activate virtual enviroment:

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

To deactivate virtual enviroment
```
$ deactivate
```

 ## Python Module Description

1. To copy all files from folder `/media/simur/maxone/COMPLETOS` to folder `/home/simur/git/uniovi-simur-wearablepermed-data` including telemetry (*.BIN) and activity reports (*.xlsx) files execute this command

    ```
    $ python3 collector.py \
    -sr '/media/simur/maxone/COMPLETOS' \
    -dr '/home/simur/git/uniovi-simur-wearablepermed-data' \
    -in '.BIN, .xlsx' \
    -v
    ```

2. To check all files from folder `/home/simur/git/uniovi-simur-wearablepermed-data`:

    ```
    $ python3 checker.py \
    -sr '/home/simur/git/uniovi-simur-wearablepermed-data' \
    -df '/home/simur/git/uniovi-simur-wearablepermed-data/resume.csv' \
    -v
    ```