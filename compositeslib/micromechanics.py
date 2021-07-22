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

#please, follow http://www.python.org/dev/peps/pep-0008/#naming-conventions

import math
import numpy as np

def mixtures(fiber, matrix, fiber_volume):
	return fiber * fiber_volume + matrix * (1 - fiber_volume)

def inverse_mixtures(fiber, matrix, fiber_volume):
	return (fiber * matrix) / (matrix * fiber_volume + fiber * (1 - fiber_volume))

def halpin_tsai(fiber, matrix, fiber_volume, xi):
	eta = ((fiber / matrix) - 1) / ((fiber / matrix) + xi)
	return matrix * (1 + eta * xi * fiber_volume) / (1 - eta * fiber_volume)

def hopkins_chamis(fiber, matrix, fiber_volume):
	sqr_vf = math.sqrt(fiber_volume)
	return matrix * ((1 - sqr_vf) + (sqr_vf) / ( 1 - sqr_vf * (1 - matrix / fiber) ))
