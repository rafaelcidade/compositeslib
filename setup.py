from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='CompositesLib',
    version='0.6',
    description="A Python package for mechanics of composite materials",
    author='Rafael Cidade',
    author_email='rafaelcidade@poli.ufrj.br',
    packages=['compositeslib'],
    license="GNU General Public License v3.0",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rafaelcidade/compositeslib',
    keywords=['composites', 'mechanics'],
    classifiers=[
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
