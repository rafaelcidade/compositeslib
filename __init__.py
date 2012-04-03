# CompositesLib: A Python Package for Composite Materials
# 
# Copyright (C) 2012 Rafael Cidade
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#  
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import sys

__author__ = 'Rafael Cidade'
__copyright__ = 'Copyright (C) 2012 Rafael Cidade'
__version__ = '0.1'

if not (2,6) <= sys.version_info[:2] <= (2,7):
    raise Exception("You are using " + platform.python_version() +
                    "CompositesLib is compatible with python 2.6 and 2.7")

try:
    import numpy as np
except ImportError:
    raise ImportError('CompositesLib requires numpy. Checkout http://numpy.scipy.org/')

__all__ = ['micromechanics']

from micromechanics import *    
#!/usr/bin/python2.7
# compositelib: A python library for composite materials.

import numpy as np
import matplotlib
import pylab