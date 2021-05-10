import os
from enum import Enum

from PIL import Image


class Gravity(Enum):
    START = 0
    CENTER = 1
    END = 2


class Direction(Enum):
    VERTICAL = "vertical",
    HORIZONTAL = "horizontal"


def is_img(path: str) -> bool:
    return os.path.isfile(path) and (path.endswith(".jpg") or path.endswith(".png"))


def merge_img(input_list: list[str], output_path: str, gravity: Gravity,
              directory: Direction, space: int):
    if directory == Direction.HORIZONTAL:
        merge_img_horizontal(input_list, output_path, gravity, space)
    else:
        merge_img_vertical(input_list, output_path, gravity, space)


def merge_img_vertical(input_list: list[str], output_path: str, gravity: Gravity, space: int):
    im_list = get_img_list(input_list)
    print(im_list)
    width = 0
    height = 0
    for img in im_list:
        # 单幅图像尺寸
        w, h = img.size
        height += h + space
        # 取最大的宽度作为拼接图的宽度
        width = max(width, w)

    # 创建空白长图
    result = Image.new('RGBA', (width, height), 0xffffff)
    # 拼接图片
    y = 0

    if gravity == Gravity.CENTER:  # 图片水平居中
        for img in im_list:
            w, h = img.size

            result.paste(img, box=(round(width / 2 - w / 2), y))
            y += h
    elif gravity == Gravity.START:  # 图片向上对其
        for img in im_list:
            w, h = img.size

            # 图片水平居中
            result.paste(img, box=(0, y))
            y += h
    else:
        for img in im_list:  # 图片向下对齐
            w, h = img.size

            # 图片水平居中
            result.paste(img, box=(round(width - w), y))
            y += h + space

    # 保存图片
    result.save(output_path)
    print("[" + ",".join(input_list) + "]" + "->" + output_path + f"({width},{height})")


def merge_img_horizontal(input_list: list[str], output_path: str, gravity: Gravity, space: int):
    im_list = get_img_list(input_list)
    print(im_list)
    width = 0
    height = 0
    for img in im_list:
        # 单幅图像尺寸
        w, h = img.size
        width += w + space
        # 取最大的宽度作为拼接图的宽度
        height = max(height, h)

    # 创建空白长图
    result = Image.new('RGBA', (width, height), 0xffffff)
    # 拼接图片
    x = 0

    if gravity == Gravity.CENTER:
        def get_y(n):
            return round(height / 2 - n / 2)
    elif gravity == Gravity.START:
        def get_y(n):
            return 0
    else:
        def get_y(n):
            return height - n

    for img in im_list:
        w, h = img.size

        # 图片水平居中
        result.paste(img, box=(x, get_y(h)))
        x += w + space

    # 保存图片
    result.save(output_path)
    print("[" + ",".join(input_list) + "]" + "->" + output_path + f"({width},{height})")


def get_img_list(file_list):
    img_path_list = []
    for item in file_list:
        if os.path.isdir(item):
            for file in os.listdir(item):
                _path = os.path.join(item, file)
                if is_img(_path):
                    img_path_list.append(_path)

        else:
            if is_img(item):
                img_path_list.append(item)
    im_list = [Image.open(i) for i in img_path_list]
    return im_list
