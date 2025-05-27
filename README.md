# Description
Uniovi Simur WearablePerMed Data Collector. Copy all files except images and movies from a dataset of files

# Execute

For example: copy all files from folder `/media/simur/maxone/COMPLETOS` to folder `/home/simur/git/uniovi-simur-wearablepermed-data` except images (*.JPG) and movies (*.MOV) files:

```
python3 main.py \
-sr '/media/simur/maxone/COMPLETOS' \
-dr '/home/simur/git/uniovi-simur-wearablepermed-data' \
-ex '.MOV, .JPG' 
```