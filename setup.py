import os

try:
    from setuptools import setup
except:
    from distutils.core import setup


with open('README.rst') as f:
    README = f.read()

setup(
    name = 'jekyll-post',
    license = "MIT",
    version = '0.1.0',
    description = 'Create a post for Jekyll',
    author = 'Shihang Zhang',
    author_email = 'zhshihang@gmail.com',
    url = 'https://github.com/sac7e/jekyll_post',
    packages = ['jekyll_post'],
    long_description = README,
    entry_points = {
        'console_scripts': [
            'jekyll-post=jekyll_post.jekyll_post:main',
        ],
    },
    install_requires=[
        "pytz >= 2012f",
        "tzlocal >= 0.0",
    ],
    classifiers = [
        "Environment :: Console",
        "Intended Audience :: Developers",
        'Topic :: Utilities',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords = 'cli',
)
