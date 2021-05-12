import os
from enum import Enum
from typing import List

from PIL import Image, ImageFilter


class Gravity(Enum):
    START = "start"
    CENTER = "center"
    END = "end"


class Direction(Enum):
    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"


def is_img(path: str) -> bool:
    return os.path.isfile(path) and (path.endswith(".jpg") or path.endswith(".png"))


def merge_img(input_list: List[str], output_path: str, gravity: Gravity,
              directory: Direction, space: int, limit_width: int, limit_height: int, sharp: bool):
    if directory == Direction.HORIZONTAL:
        width, height, result = merge_img_horizontal(input_list, gravity, space)
    else:
        width, height, result = merge_img_vertical(input_list, gravity, space)

    # 缩放
    if limit_width is not None or limit_height is not None:
        if limit_width is not None and limit_height is not None:
            result = result.resize((limit_width, limit_height))
        elif limit_width is not None:
            result = result.resize((limit_width, round(limit_width / result.width * result.height)))
        elif limit_height is not None:
            result = result.resize((round(limit_height / result.height * result.width), limit_height))
        # 锐化
        if sharp:
            result = result.filter(ImageFilter.SHARPEN)

    # 保存图片
    result.save(output_path)
    w, h = result.size

    print("[" + ", ".join([os.path.abspath(i) for i in input_list]) + "]" + " -> " + os.path.abspath(
        output_path) + f" ({w},{h})")


def merge_img_vertical(input_list: List[str], gravity: Gravity, space: int) -> (int, int, Image):
    im_list = get_img_list(input_list)
    # print(im_list)
    width = 0
    height = 0
    for img in im_list:
        # 单幅图像尺寸
        w, h = img.size
        height += h
        # 取最大的宽度作为拼接图的宽度
        width = max(width, w)
    height += (len(im_list) - 1) * space

    # 创建空白长图
    result = Image.new('RGB', (width, height), 0xffffff)
    # 拼接图片
    y = 0

    if gravity == Gravity.CENTER:  # 图片水平居中
        def get_x(n):
            return round(width / 2 - n / 2)
    elif gravity == Gravity.START:  # 图片向左对齐
        def get_x(n):
            return 0
    else:  # 图片向右对齐
        def get_x(n):
            return width - n

    for img in im_list:
        w, h = img.size

        result.paste(img, box=(get_x(w), y))
        y += h + space

    return width, height, result


def merge_img_horizontal(input_list: List[str], gravity: Gravity, space: int) -> (int, int, Image):
    im_list = get_img_list(input_list)
    # print(im_list)
    width = 0
    height = 0
    for img in im_list:
        # 单幅图像尺寸
        w, h = img.size
        width += w
        # 取最大的宽度作为拼接图的宽度
        height = max(height, h)
    width += (len(im_list) - 1) * space

    # 创建空白长图
    result = Image.new('RGB', (width, height), 0xffffff)
    # 拼接图片
    x = 0

    if gravity == Gravity.CENTER:  # 图片垂直居中
        def get_y(n):
            return round(height / 2 - n / 2)
    elif gravity == Gravity.START:  # 图片向上对齐
        def get_y(n):
            return 0
    else:  # 图片向下对齐
        def get_y(n):
            return height - n

    for img in im_list:
        w, h = img.size

        # 图片水平居中
        result.paste(img, box=(x, get_y(h)))
        x += w + space

    return width, height, result


def get_img_list(file_list) -> [Image]:
    return [Image.open(i) for i in get_img_path_list(file_list)]


def get_img_path_list(file_list):
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
    return img_path_list
