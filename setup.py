import os
import re

import setuptools

# 供github actions使用
VERSION = os.getenv("GITHUB_REF")
if VERSION is not None:
    VERSION = VERSION[VERSION.rfind('v'):]

# p = subprocess.Popen('git tag -l --contains', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# result = p.stdout.readlines()
# if len(result) == 0:
#     raise RuntimeError("当前提交没有tag")
# else:
#     # print("tag数量为：" + str(len(result)))
#     VERSION = str(result[0], encoding="utf-8").strip("\n ")

if not re.match(r"^v[0-9]+\.[0-9]+\.[0-9]+$", VERSION):
    raise RuntimeError("tag格式不合法，例：v1.0.0")
else:
    VERSION = VERSION[VERSION.rfind('v') + 1:]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

install_requires = ['Pillow', 'PyPDF2']

setuptools.setup(
    name="custools",  # Replace with your own username
    version=VERSION,
    author="Potato-DiGua",
    author_email="86543402@qq.com",
    description="A commonly used simple tools!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Potato-DiGua/Tools",
    project_urls={
        "Bug Tracker": "https://github.com/Potato-DiGua/Tools/issues",
    },
    license='MIT',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=install_requires,
    entry_points={'console_scripts': [
        'custools = tools.entrypoints.main:main']}
)
