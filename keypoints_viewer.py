import cv2
import json
import argparse
import os
import glob
import matplotlib.cm as cm
import numpy as np

def parse_args():
    parser = argparse.ArgumentParser(description="COCO Keypoints Visualization")
    parser.add_argument(
        '-a',
        '--annotation_file',
        type=str,
        default='annotations/person_keypoints_train2017.json',
        help="Path to the COCO annotation file (JSON)",
    )
    parser.add_argument(
        '-i',
        '--image_folder',
        type=str,
        default='images',
        help="Path to the folder containing image files",
    )
    parser.add_argument(
        '-o',
        '--output_folder',
        type=str,
        default='output',
        help="Path to the folder output image files",
    )
    parser.add_argument(
        '-w',
        '--wait_time',
        type=int,
        default=0,
        help="Wait time for cv2.imshow in milliseconds (default: 0 for infinite)",
    )
    return parser.parse_args()

def get_keypoint_colors(num_keypoints):
    colors = cm.get_cmap('tab20', num_keypoints)
    return [(int(c[0]*255), int(c[1]*255), int(c[2]*255)) for c in colors(np.linspace(0, 1, num_keypoints))]

def main():
    args = parse_args()

    with open(args.annotation_file, 'r') as f:
        annotations = json.load(f)

    images = {img['id']: img['file_name'] for img in annotations['images']}
    num_keypoints = len(annotations['categories'][0]['keypoints'])
    keypoint_colors = get_keypoint_colors(num_keypoints)
    image_files = sorted(glob.glob(os.path.join(args.image_folder, '*')))

    for image_file in image_files:
        image_name = os.path.basename(image_file)
        image_id = next((img_id for img_id, file_name in images.items() if file_name == image_name), None)

        if image_id is None:
            print(f"Warning: No annotation found for {image_name}")
            continue

        keypoints_list = [
            anno['keypoints'] for anno in annotations['annotations'] if anno['image_id'] == image_id
        ]

        if not keypoints_list:
            print(f"Warning: No keypoints found for {image_name}")
            continue

        img = cv2.imread(image_file)
        if img is None:
            print(f"Error: Could not load image {image_file}")
            continue

        for keypoints in keypoints_list:
            for i in range(0, len(keypoints), 3):
                x, y, v = keypoints[i:i+3]
                color = keypoint_colors[i // 3]
                if v > 0:
                    cv2.circle(img, (int(x), int(y)), 4, color, -1)

        cv2.imshow('Keypoints', img)
        key = cv2.waitKey(args.wait_time)
        if key == 27:
            break

        output_path = os.path.join(args.output_folder, os.path.basename(image_file))
        os.makedirs(args.output_folder, exist_ok=True)
        cv2.imwrite(output_path, img)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
