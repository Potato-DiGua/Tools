from enum import Enum

from PIL import Image


class Gravity(Enum):
    LEFT = 0
    CENTER = 1
    RIGHT = 2


def merge_img(img_list: list[str], output_path: str, gravity: Gravity = Gravity.CENTER):
    im_list = [Image.open(i) for i in img_list if i.endswith(".jpg") or i.endswith(".png")]

    width = 0
    height = 0
    for img in im_list:
        # 单幅图像尺寸
        w, h = img.size
        height += h
        # 取最大的宽度作为拼接图的宽度
        width = max(width, w)
    print(width)
    print(height)

    # 创建空白长图
    result = Image.new('RGBA', (width, height), 0xffffff)
    # 拼接图片
    height = 0

    if gravity == Gravity.CENTER:
        def get_x(n):
            return round(width / 2 - n / 2)
    elif gravity == Gravity.LEFT:
        def get_x(n):
            return 0
    else:
        def get_x(n):
            return width - n

    for img in im_list:
        w, h = img.size

        # 图片水平居中
        result.paste(img, box=(get_x(w), height))
        height += h

    # 保存图片
    result.save(output_path)
    print("[" + ",".join(img_list) + "]" + "->" + output_path)
