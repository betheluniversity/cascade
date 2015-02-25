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


file_text = read(fpath('cascade/__init__.py'))

setup(
    name='cascade',
    version=grep('__version__'),
    description='Better dates and times for Python',
    long_description=open('README.rst').read(),
    url='',
    author='Eric Jameson',
    author_email="e-jameson@bethel.edu",
    license='Apache 2.0',
    packages=['cascade'],
    zip_safe=False,
    install_requires=[
        ''
    ],
    test_suite="tests",
    classifiers=[
        'Development Status :: 5 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)