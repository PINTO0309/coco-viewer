# coco-viewer
Drawing and visualizing bounding boxes and key points.

MS-COCO: https://cocodataset.org/#download

Annotation files: https://github.com/PINTO0309/coco-viewer/releases/download/annotations/annotations.tar.gz

```python
python boundingbox_viewer.py -h

usage:
boundingbox_viewer.py \
[-h] \
[-a ANNOTATION_FILE] \
[-i IMAGE_FOLDER] \
[-o OUTPUT_FOLDER] \
[-w WAIT_TIME]

COCO Bounding Boxes Visualization

options:
  -h, --help
    show this help message and exit
  -a ANNOTATION_FILE, --annotation_file ANNOTATION_FILE
    Path to the COCO annotation file (JSON)
  -i IMAGE_FOLDER, --image_folder IMAGE_FOLDER
    Path to the folder containing image files
  -o OUTPUT_FOLDER, --output_folder OUTPUT_FOLDER
    Path to the folder output image files
  -w WAIT_TIME, --wait_time WAIT_TIME
    Wait time for cv2.imshow in milliseconds (default: 0 for infinite)
```

|image|image|
|:-:|:-:|
|![0007_000000000544](https://github.com/user-attachments/assets/c0baa273-4a68-49e2-bd30-0ce8cda5483a)|![0005_000000000692](https://github.com/user-attachments/assets/54ad1f2a-578b-4dc4-af82-80bbf8dbc853)|

```python
python keypoints_viewer.py -h

usage:
keypoints_viewer.py \
[-h] \
[-a ANNOTATION_FILE] \
[-i IMAGE_FOLDER] \
[-o OUTPUT_FOLDER] \
[-w WAIT_TIME]

COCO Keypoints Visualization

options:
  -h, --help
    show this help message and exit
  -a ANNOTATION_FILE, --annotation_file ANNOTATION_FILE
    Path to the COCO annotation file (JSON)
  -i IMAGE_FOLDER, --image_folder IMAGE_FOLDER
    Path to the folder containing image files
  -o OUTPUT_FOLDER, --output_folder OUTPUT_FOLDER
    Path to the folder output image files
  -w WAIT_TIME, --wait_time WAIT_TIME
    Wait time for cv2.imshow in milliseconds (default: 0 for infinite)
```

|image|image|
|:-:|:-:|
|![0006_000000000544](https://github.com/user-attachments/assets/6e564ec6-0a0b-478b-a3e6-d160b040452a)|![0004_000000000692](https://github.com/user-attachments/assets/fd90dca8-c93d-4741-94ff-ea12117095d6)|
