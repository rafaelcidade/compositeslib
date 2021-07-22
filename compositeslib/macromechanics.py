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

#please, follow http://www.python.org/dev/peps/pep-0008/#naming-conventions

import math
import numpy as np

def t(theta_deg):
	aux = theta_deg * math.pi / 180.
	m = math.cos(aux)
	n = math.sin(aux)
	t = np.matrix( [[ math.pow(m,2), math.pow(n,2),  2*n*m ],
				   [ math.pow(n,2), math.pow(m,2), -2*n*m ],
				   [ -n*m, n*m, math.pow(m,2) - math.pow(n,2) ]],)   
	return t

def calculate_stress(laminate, load):
	load_array = np.matrix([ load.nx, load.ny, load.nxy, load.mx, load.my, load.mxy])
	laminate.strain_curvature = laminate.ABD().I * load_array.T
	
	for ply in laminate.plies:
		ply.global_strain[:,0] = laminate.strain_curvature[:3] + ply.z[0] * laminate.strain_curvature[3:]
		ply.global_strain[:,1] = laminate.strain_curvature[:3] + ply.z[1] * laminate.strain_curvature[3:]

		ply.global_stress[:,0] = ply.ql() * ply.global_strain[:,0]
		ply.global_stress[:,1] = ply.ql() * ply.global_strain[:,1]

		ply.local_stress[:,0] = t(ply.theta) * ply.global_stress[:,0]
		ply.local_stress[:,1] = t(ply.theta) * ply.global_stress[:,1]

		ply.local_strain[:,0] = (t(ply.theta).T).I * ply.global_strain[:,0]
		ply.local_strain[:,1] = (t(ply.theta).T).I * ply.global_strain[:,1]

def max_stress(ply):
	if not validate_strength(ply):
		return
	long_index = max(
		ply.local_stress[0,0] / ply.xt if ply.local_stress[0,0] > 0 else - ply.local_stress[0,0] / ply.xc,
		ply.local_stress[0,1] / ply.xt if ply.local_stress[0,1] > 0 else - ply.local_stress[0,1] / ply.xc
		)

	trans_index = max(
		ply.local_stress[1,0] / ply.yt if ply.local_stress[1,0] > 0 else - ply.local_stress[1,0] / ply.yc,
		ply.local_stress[1,1] / ply.yt if ply.local_stress[1,1] > 0 else - ply.local_stress[1,1] / ply.yc
		)

	shear_index = max(
		ply.local_stress[2,0] / ply.s if ply.local_stress[2,0] > 0 else - ply.local_stress[2,0] / ply.s,
		ply.local_stress[2,1] / ply.s if ply.local_stress[2,1] > 0 else - ply.local_stress[2,1] / ply.s
		)

	bot_index = max(
				ply.local_stress[0,0] / ply.xt if ply.local_stress[0,0] > 0 else - ply.local_stress[0,0] / ply.xc,
				ply.local_stress[1,0] / ply.yt if ply.local_stress[1,0] > 0 else - ply.local_stress[1,0] / ply.yc,
				abs(ply.local_stress[2,0]) / ply.s
				)

	top_index = max(
				ply.local_stress[0,1] / ply.xt if ply.local_stress[0,0] > 0 else - ply.local_stress[0,1] / ply.xc,
				ply.local_stress[1,1] / ply.yt if ply.local_stress[1,0] > 0 else - ply.local_stress[1,1] / ply.yc,
				abs(ply.local_stress[2,1]) / ply.s
				)

	return max(top_index,bot_index)


def max_strain(ply):
	if not validate_strength(ply):
		return
	long_index = max(
		ply.e1 * ply.local_strain[0,0] / ply.xt if ply.e1 * ply.local_strain[0,0] > 0 
		else - ply.e1 * ply.local_strain[0,0] / ply.xc,

		ply.e1 * ply.local_strain[0,1] / ply.xt if ply.e1 * ply.local_strain[0,1] > 0
				else - ply.e1 * ply.local_strain[0,1] / ply.xc
		)

	trans_index = max(
		ply.e2 * ply.local_strain[1,0] / ply.yt if ply.e2 * ply.local_strain[1,0] > 0 
		else - ply.e2 * ply.local_strain[1,0] / ply.yc,

		ply.e2 * ply.local_strain[1,1] / ply.yt if ply.e2 * ply.local_strain[1,1] > 0 
		else - ply.e2 * ply.local_strain[1,1] / ply.yc
		)

	shear_index = max(
		abs(ply.local_strain[2,0]) / ply.e12s,
		abs(ply.local_strain[2,1]) / ply.e12s
		)

	return max(long_index,trans_index,shear_index)

def max_strain_mode(ply):
	if not validate_strength(ply):
		return
	long_index = max(
		ply.e1 * ply.local_strain[0,0] / ply.xt if ply.e1 * ply.local_strain[0,0] > 0 
		else - ply.e1 * ply.local_strain[0,0] / ply.xc,

		ply.e1 * ply.local_strain[0,1] / ply.xt if ply.e1 * ply.local_strain[0,1] > 0
				else - ply.e1 * ply.local_strain[0,1] / ply.xc
		)

	trans_index = max(
		ply.e2 * ply.local_strain[1,0] / ply.yt if ply.e2 * ply.local_strain[1,0] > 0 
		else - ply.e2 * ply.local_strain[1,0] / ply.yc,

		ply.e2 * ply.local_strain[1,1] / ply.yt if ply.e2 * ply.local_strain[1,1] > 0 
		else - ply.e2 * ply.local_strain[1,1] / ply.yc
		)

	shear_index = max(
		abs(ply.local_strain[2,0]) / ply.e12s,
		abs(ply.local_strain[2,1]) / ply.e12s
		)
	if max(long_index,trans_index,shear_index) == long_index:
			return 1
	elif max(long_index,trans_index,shear_index) == trans_index:
			return 2
	elif max(long_index,trans_index,shear_index) == shear_index:
			return 3

def tsai_wu(ply):
	if not validate_strength(ply):
		return
	F11 = 1. / ( ply.xt * ply.xc )
	F22 = 1. / ( ply.yt * ply.yc )
	F1 = 1. / ply.xt - 1. / ply.xc 
	F2 = 1. / ply.yt - 1. / ply.yc
	F66 = 1. / (ply.s**2)
	F12 = - math.sqrt(F11*F22) / 2.

	return max(
		F11 * ply.local_stress[0,0]**2 + F12 * ply.local_stress[0,0] * ply.local_stress[1,0] + 
		F22 * ply.local_stress[1,0]**2	+ F66 * ply.local_stress[2,0]**2 + F1 * ply.local_stress[0,0] + 
		F2 * ply.local_stress[1,0]
		,
		F11 * ply.local_stress[0,1]**2 + F12 * ply.local_stress[0,1] * ply.local_stress[1,1] + 
		F22 * ply.local_stress[1,1]**2	+ F66 * ply.local_stress[2,1]**2 + F1 * ply.local_stress[0,1] + 
		F2 * ply.local_stress[1,1]
		)

def tsai_hill(ply):
	if not validate_strength(ply):
		return
	F1_b = 1. / ply.xt if ply.local_stress[0,0] > 0 else 1. / ply.xc
	F2_b = 1. / ply.yt if ply.local_stress[1,0] > 0 else 1. / ply.yc
	F1_t = 1. / ply.xt if ply.local_stress[0,1] > 0 else 1. / ply.xc
	F2_t = 1. / ply.yt if ply.local_stress[1,1] > 0 else 1. / ply.yc

	return max(
		(F1_b * ply.local_stress[0,0])**2 
		+ (F2_b * ply.local_stress[1,0])**2
		- (F1_b**2) * ply.local_stress[0,0] * ply.local_stress[1,0]
		+ (ply.local_stress[2,0] / ply.s)**2
		,
		(F1_b * ply.local_stress[0,1])**2 + 
		(F2_b * ply.local_stress[1,1])**2
		- (F1_b**2) * ply.local_stress[0,1] * ply.local_stress[1,1]
		+ (ply.local_stress[2,1] / ply.s)**2
		)

def hashin(ply):
	if not validate_strength(ply):
		return
	fiber_index = max(
		ply.local_stress[0,0] / ply.xt if ply.local_stress[0,0] > 0 else - ply.local_stress[0,0] / ply.xc,
		ply.local_stress[0,1] / ply.xt if ply.local_stress[0,1] > 0 else - ply.local_stress[0,1] / ply.xc
		)

	matrix_index = max(
		(ply.local_stress[1,0] / ply.yt)**2 + (ply.local_stress[2,0] / ply.s)**2
			if ply.local_stress[1,0] > 0 
			else (- ply.local_stress[1,0] / ply.yc)**2 + (ply.local_stress[2,0] / ply.s)**2,
		(ply.local_stress[1,1] / ply.yt)**2 + (ply.local_stress[2,1] / ply.s)**2 
			if ply.local_stress[1,1] > 0 
			else (- ply.local_stress[1,1] / ply.yc)**2 + (ply.local_stress[2,1] / ply.s)**2
		)
	return max(matrix_index,matrix_index)

def linde(ply):
	if not validate_strength(ply): 
		return
	ply.e1t = ply.xt / ply.e1
	ply.e1c = ply.xc / ply.e1
	ply.e2t = ply.yt / ply.e2
	ply.e2c = ply.yc / ply.e2
	if ply.e12s == None:
		ply.e12s = ply.s / ply.g12
	fiber_index = max(
				(1/ply.e1t)*math.sqrt(abs((ply.e1t/ply.e1c)*ply.local_strain[0,0]**2 + (ply.e1t - ply.e1t**2/ply.e1c)*ply.local_strain[0,0])),
				(1/ply.e1t)*math.sqrt(abs((ply.e1t/ply.e1c)*ply.local_strain[0,1]**2 + (ply.e1t - ply.e1t**2/ply.e1c)*ply.local_strain[0,1]))
				)
	matrix_index = max(
				(1/ply.e2t)*math.sqrt(abs((ply.e2t/ply.e2c)*ply.local_strain[1,0]**2 + (ply.e2t - ply.e2t**2/ply.e2c)*ply.local_strain[1,0]
									  + ((ply.e2t/ply.e12s)**2)*ply.local_strain[2,0]**2)),
				(1/ply.e2t)*math.sqrt(abs((ply.e2t/ply.e2c)*ply.local_strain[1,1]**2 + (ply.e2t - ply.e2t**2/ply.e2c)*ply.local_strain[1,1]
									  + ((ply.e2t/ply.e12s)**2)*ply.local_strain[2,1]**2))
				)
	return max(fiber_index,matrix_index)

def validate_strength(ply):
	return not (ply.xt == None or ply.xc == None or ply.yt == None or ply.yc == None or ply.s == None)