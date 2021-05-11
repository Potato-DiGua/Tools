import argparse

from .. import PdfTools, ImgTools


def pdf(args):
    PdfTools.merge_pdf(args.input, args.output)


def img(args):
    ImgTools.merge_img(args.input, args.output, ImgTools.Gravity(args.gravity), ImgTools.Direction(args.direction),
                       args.space, args.width, args.height, args.sharp)


def main():
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
    parser_img.add_argument('-d', '--direction', help="图片合并方向", choices=["horizontal", "vertical"], default="vertical")
    parser_img.add_argument('-o', '--output', help="合成图片的输出路径", default="./merge.png")
    parser_img.add_argument('-g', '--gravity', choices=[ImgTools.Gravity.START.value, ImgTools.Gravity.CENTER.value,
                                                        ImgTools.Gravity.END.value], help="图片的水平方向", default="center")
    parser_img.add_argument('-s', '--space', type=int, help="图片的间距", default=0)
    parser_img.add_argument('-w', "--width", type=int, help="合成图片的宽度")
    parser_img.add_argument("--height", type=int, help="合成图片的高度")
    parser_img.add_argument('--sharp', action='store_true', help="锐化", default=False)
    parser_img.set_defaults(func=img)

    arg = parser.parse_args()
    arg.func(arg)
