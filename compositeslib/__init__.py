# CompositesLib: A Python Package for Composite Materials
#
# Copyright (C) 2021 Rafael Cidade
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

import platform
import sys

from classes import *
from micromechanics import *
from macromechanics import *
from output import *
from plot import *

__author__ = 'Rafael Cidade'
__copyright__ = 'Copyright (C) 2021 Rafael Cidade'
__version__ = '0.2'

if not (3, 6) <= sys.version_info[:2]:
    raise Exception("You are using " + platform.python_version() +
                    "CompositesLib is compatible with python 3.6 or later")

try:
    import numpy as np
except ImportError:
    raise ImportError(
        'CompositesLib requires numpy. Checkout http://numpy.scipy.org/')

__all__ = ['classes', 'micromechanics', 'macromechanics', 'output', 'plot']
