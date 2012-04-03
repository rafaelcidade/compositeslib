from setuptools import setup

setup(
    name='CompositesLib',
    version='0.1',
    description="Mechanics of Composite Materials Package",
    author='Rafael Cidade',
    author_email='rafaelcidade@metalmat.ufrj.br',
    packages=['compositeslib'],
    license=open('LICENSE.txt').read(),
   # long_description=open('README.rst').read(),
    url='https://github.com/ndevenish/simplehistogram',
    keywords = ['histogram'],
    classifiers = [
      "Programming Language :: Python",
      "Programming Language :: Python :: 2.6",
      "License :: OSI Approved :: GNU General Public License (GPL)",
      "Operating System :: OS Independent",
      "Intended Audience :: Science/Research",
      "Topic :: Scientific/Engineering :: Mechanical Engineering",
      "Development Status :: 2 - Pre-Alpha",
    ],
    install_requires=['numpy', 'matplotlib'],
    zip_safe=False,
)