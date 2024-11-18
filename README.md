# coco-viewer
Drawing and visualizing bounding boxes and key points.

MS-COCO: https://cocodataset.org/#download

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