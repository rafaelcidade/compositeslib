from setuptools import setup
from distribute_setup import use_setuptools
use_setuptools()

setup(
    name='CompositesLib',
    version='0.2',
    description="A Python package for mechanics of composite materials",
    author='Rafael Cidade',
    author_email='rafaelcidade@metalmat.ufrj.br',
    packages=['compositeslib'],
    license="GNU General Public License v3.0",
    long_description=open('README.rst').read(),
    url='https://github.com/rafaelcidade/compositeslib',
    keywords = ['composites', 'mechanics'],
    classifiers = [
      "Programming Language :: Python",
      "Programming Language :: Python :: 3.6",
      "Programming Language :: Python :: 3.7",
      "Programming Language :: Python :: 3.8",
      "Programming Language :: Python :: 3.9",
      "License :: OSI Approved :: GNU General Public License (GPL)",
      "Operating System :: OS Independent",
      "Intended Audience :: Science/Research",
      "Topic :: Scientific/Engineering",
      "Development Status :: 2 - Pre-Alpha"
    ],
    install_requires=['numpy', 'matplotlib'],
    zip_safe=False,
)