import setuptools

VERSION = "0.0.1"

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

install_requires = ['Pillow', 'PyPDF2']

setuptools.setup(
    name="pdtools",  # Replace with your own username
    version=VERSION,
    author="Potato-DiGua",
    author_email="86543402@qq.com",
    description="A Commonly used simple pdtools!",
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
        'pdtools = pdtools.entrypoints.main:main']}
)
