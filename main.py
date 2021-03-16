import argparse
from tools import PdfTools
from tools import ImgTools


def pdf(args):
    PdfTools.merge_pdf(args.input, args.output)


def img(args):
    gravity: ImgTools.Gravity

    if args.gravity == "left":
        gravity = ImgTools.Gravity.LEFT
    elif args.gravity == "right":
        gravity = ImgTools.Gravity.RIGHT
    else:
        gravity = ImgTools.Gravity.CENTER
    ImgTools.merge_img(args.input, args.output, gravity)


if __name__ == '__main__':
    description = "常用工具"

    parser = argparse.ArgumentParser(description=description)

    subparsers = parser.add_subparsers()
    parser_pdf = subparsers.add_parser("pdf", help="pdf合并")
    parser_pdf.add_argument('-i', '--input', help="pdf的路径", nargs='+', required=True)
    parser_pdf.add_argument('-o', '--output', help="合成pdf的输出路径", default="merge.pdf")
    parser_pdf.set_defaults(func=pdf)

    # 图片合并
    parser_img = subparsers.add_parser("img", help="图片合并")
    parser_img.add_argument('-i', '--input', help="图片或图片所在文件夹的路径", nargs='+', required=True)
    parser_img.add_argument('-o', '--output', help="合成图片的输出路径", default="./merge.png")
    parser_img.add_argument('-g', '--gravity', choices=["left", "center", "right"], help="图片的水平方向", default="center")
    parser_img.set_defaults(func=img)

    arg = parser.parse_args()
    arg.func(arg)
