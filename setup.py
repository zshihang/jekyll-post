from distutils.core import setup

setup(
    name='jekyll-post',
    license="MIT",
    version='0.1.0',
    description='Create a post for Jekyll',
    author='Shihang Zhang',
    author_email='zhshihang@gmail.com',
    url='https://github.com/sac7e/jekyll-post',
    packages=['jekyll-post'],
    long_description=open('README.rst').read(),
    install_requires=[
        "pyflakes 1.2",
    ],
)
