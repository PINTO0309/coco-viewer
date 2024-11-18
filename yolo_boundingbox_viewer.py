import cv2
import os

# ファイルパスの設定
annotation_file = "000000000544.txt"
image_file = "images/000000000544.jpg"
output_file = "output/000000000544_yolo.jpg"

# カラーマッピング (クラスごとに異なる色を割り当て)
colors = [
    (255, 0, 0),   # 赤
    (0, 255, 0),   # 緑
    (0, 0, 255),   # 青
    (255, 255, 0), # シアン
    (255, 0, 255), # マゼンタ
    (0, 255, 255)  # イエロー
]

# YOLOアノテーションを読み込んで描画
def draw_annotations(image_path, annotation_path, output_path):
    # 画像の読み込み
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Cannot load image {image_path}")
        return

    h, w, _ = image.shape  # 画像の幅と高さを取得

    # アノテーションの読み込み
    with open(annotation_path, "r") as file:
        lines = file.readlines()

    for line in lines:
        parts = line.strip().split()
        class_id = int(parts[0])
        center_x, center_y, box_width, box_height = map(float, parts[1:])

        # 元画像のサイズにスケール変換
        center_x *= w
        center_y *= h
        box_width *= w
        box_height *= h

        # バウンディングボックスの座標計算
        x1 = int(center_x - box_width / 2)
        y1 = int(center_y - box_height / 2)
        x2 = int(center_x + box_width / 2)
        y2 = int(center_y + box_height / 2)

        # 色をクラスIDに基づいて選択
        color = colors[class_id % len(colors)]

        # バウンディングボックスの描画
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 1)

    # 出力ディレクトリがない場合は作成
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 画像の保存
    cv2.imwrite(output_path, image)
    print(f"Annotated image saved to {output_path}")

# 実行
draw_annotations(image_file, annotation_file, output_file)
