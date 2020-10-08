from setuptools import setup
from hoi3tools import __version__

with open("README.md", encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="hoi3tools",
    version=__version__,
    author="Daniel Zakharov",
    author_email="daniel734@bk.ru",
    description="hoi3tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="hoi3 game",
    url="https://github.com/jDan735/hoi3tools",
    license="MIT",
    packages=["hoi3tools"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3",
    entry_points={
        "console_scripts": [
            "hoi3tools=hoi3tools.h3t:main",
            "h3t=hoi3tools.h3t:main"
        ]
    }
)
