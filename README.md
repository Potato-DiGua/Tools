![下载](https://img.shields.io/github/downloads/Potato-DiGua/Tools/total) ![Release](https://img.shields.io/github/v/release/Potato-DiGua/Tools)
# Tools
- pdf合并
- 图片合并

```
usage: tool.exe [-h] {pdf,img} ...

常用工具

positional arguments:
  {pdf,img}
    pdf       pdf合并
    img       图片合并

optional arguments:
  -h, --help  show this help message and exit
```
```
usage: tool.exe img [-h] -i INPUT [INPUT ...] [-d {horizontal,vertical}] [-o OUTPUT] [-g {left,center,right}]
                           [-s SPACE]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT [INPUT ...], --input INPUT [INPUT ...]
                        图片或图片所在文件夹的路径
  -d {horizontal,vertical}, --direction {horizontal,vertical}
                        图片合并方向
  -o OUTPUT, --output OUTPUT
                        合成图片的输出路径
  -g {left,center,right}, --gravity {left,center,right}
                        图片的水平方向
  -s SPACE, --space SPACE
                        图片的间距
```
```
usage: tool.exe pdf [-h] -i INPUT [INPUT ...] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT [INPUT ...], --input INPUT [INPUT ...]
                        pdf的路径
  -o OUTPUT, --output OUTPUT
                        合成pdf的输出路径
```
