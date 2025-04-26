#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script de instalação para AsciiArt Generator
"""

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="asciiart-generator",
    version="1.0.0",
    description="Uma ferramenta para gerar arte ASCII a partir de texto",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Troli",
    author_email="pablotroli@outlook.com",
    url="https://github.com/DevTroli/ascii-generator",
    py_modules=["asciiArt"],
    entry_points={
        "console_scripts": [
            "asciiart=asciiArt:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Text Processing",
        "Topic :: Artistic Software",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
)
