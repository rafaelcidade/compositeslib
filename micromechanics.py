# author: Rafael Cidade <rafaelcidade@metalmat.ufrj.br>
# compositeslib - A python Library for composite materials

#please, follow http://www.python.org/dev/peps/pep-0008/#naming-conventions

import numpy as np
import pylab

def mixtures(fiber, matrix, fiber_volume):
	return fiber * fiber_volume + matrix * (1 - fiber_volume)

def inverse_mixtures(fiber, matrix, fiber_volume):
	return (fiber * matrix) / (matrix * fiber_volume + fiber * (1 - fiber_volume))
#not implemented yet
def halpin_tsai(fiber, matrix, fiber_volume):
	return (fiber * matrix) / (matrix * fiber_volume + fiber * (1 - fiber_volume))
#not implemented yet
def hopkings_chamis(fiber, matrix, fiber_volume):
	return (fiber * matrix) / (matrix * fiber_volume + fiber * (1 - fiber_volume))