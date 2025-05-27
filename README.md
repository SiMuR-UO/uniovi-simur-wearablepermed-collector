# Description
Copy all files from one folder to another one excluding some file extensions.

# Execute

Copy all files from folder `/media/simur/maxone/COMPLETOS` to folder `/home/simur/git/uniovi-simur-wearablepermed-data` except images (*.JPG) and movies (*.MOV) files:

```
$ python3 copier.py \
-sr '/media/simur/maxone/COMPLETOS' \
-dr '/home/simur/git/uniovi-simur-wearablepermed-data' \
-ex '.MOV, .JPG'
-v
```