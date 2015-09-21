import codecs
import os
import re
from setuptools import setup, find_packages


with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                              'teco', '__init__.py'), 'r', 'utf-8') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'\r?$",
                             fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')


def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()


setup(
    name='teco',
    version=version,
    description=('The tool that finds N most frequently occurring terms.'),
    long_description=read('README.md'),
    author='Alexey Lisovoy',
    author_email='lisovoy.a.s@gmail.com',
    url='https://github.com/AlexLisovoy/teco.git',
    license='MIT',
    packages=find_packages()
)
