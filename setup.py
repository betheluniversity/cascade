from setuptools import find_packages
import os.path
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval


file_text = read(fpath('bu_cascade/__init__.py'))

setup(
    name='bu_cascade',
    version=1.98998,
    description='Cascade Server web services integration',
    long_description='',
    url='https://github.com/betheluniversity/cascade/',
    download_url='',
    author='Eric Jameson',
    author_email="e-jameson@bethel.edu",
    license='Apache 2.0',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'suds'
    ],
    test_suite="",
    classifiers=[]
)