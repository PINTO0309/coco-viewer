import cv2
import json
import argparse
import os
import glob
import numpy as np

def parse_args():
    parser = argparse.ArgumentParser(description="COCO Bounding Boxes Visualization")
    parser.add_argument(
        '-a',
        '--annotation_file',
        type=str,
        default='annotations/instances_train2017.json',
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

def get_random_color():
    """Generate a random color for bounding boxes."""
    return tuple([int(x) for x in np.random.randint(0, 255, 3)])

def main():
    args = parse_args()

    with open(args.annotation_file, 'r') as f:
        annotations = json.load(f)

    # Map image ID to file name
    images = {img['id']: img['file_name'] for img in annotations['images']}
    image_files = sorted(glob.glob(os.path.join(args.image_folder, '*')))

    for image_file in image_files:
        image_name = os.path.basename(image_file)
        image_id = next((img_id for img_id, file_name in images.items() if file_name == image_name), None)

        if image_id is None:
            print(f"Warning: No annotation found for {image_name}")
            continue

        # Extract bounding boxes for the current image
        bboxes = [
            anno['bbox'] for anno in annotations['annotations'] if anno['image_id'] == image_id
        ]

        if not bboxes:
            print(f"Warning: No bounding boxes found for {image_name}")
            continue

        img = cv2.imread(image_file)
        if img is None:
            print(f"Error: Could not load image {image_file}")
            continue

        for bbox in bboxes:
            x, y, w, h = bbox
            color = get_random_color()
            cv2.rectangle(img, (int(x), int(y)), (int(x + w), int(y + h)), color, 2)

        cv2.imshow('Bounding Boxes', img)
        key = cv2.waitKey(args.wait_time)
        if key == 27:  # Press 'Esc' to quit
            break

        # Save output image
        output_path = os.path.join(args.output_folder, os.path.basename(image_file))
        os.makedirs(args.output_folder, exist_ok=True)
        cv2.imwrite(output_path, img)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
