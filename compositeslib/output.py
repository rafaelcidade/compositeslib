# -*- coding: utf-8 -*-
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

import numpy as np
from classes import *

def print_stress(laminate):
	print("".ljust(10) + "σx".rjust(9) + "σy".rjust(9) + "τxy".rjust(9) + "|".rjust(4) + \
	"σ1".rjust(9) + "σ2".rjust(9) + "τ12".rjust(9))
	for ply in laminate.plies:
		print("Ply #" + str(laminate.plies.index(ply) + 1).ljust(2))
		bottom_stress = ""
		top_stress = ""
		for stress in ply.global_stress[:,0]:
			bottom_stress += str(round(stress[0,0],2)).rjust(8)
		for stress in ply.global_stress[:,1]:
			top_stress += str(round(stress[0,0],2)).rjust(8)
		
		bottom_stress += "|".rjust(4)
		top_stress += "|".rjust(4)
		
		for stress in ply.local_stress[:,0]:
			bottom_stress += str(round(stress[0,0],2)).rjust(8)
		for stress in ply.local_stress[:,1]:
			top_stress += str(round(stress[0,0],2)).rjust(8)
		
		print("Bottom".ljust(10) + bottom_stress)
		print("Top".ljust(10) + top_stress)

def print_strain(laminate):
	print("".ljust(10) + "εx".rjust(9) + "εy".rjust(9) + "γxy".rjust(9) + "|".rjust(4) + \
	"ε1".rjust(9) + "ε2".rjust(9) + "γ12".rjust(9))
	for ply in laminate.plies:
		print("Ply #" + str(laminate.plies.index(ply) + 1).ljust(2))
		bottom_strain = ""
		top_strain = ""
		for strain in ply.global_strain[:,0]:
			bottom_strain += str(round(strain[0,0],3)).rjust(8)
		for strain in ply.global_strain[:,1]:
			top_strain += str(round(strain[0,0],3)).rjust(8)
		
		bottom_strain += "|".rjust(4)
		top_strain += "|".rjust(4)
		
		for strain in ply.local_strain[:,0]:
			bottom_strain += str(round(strain[0,0],3)).rjust(8)
		for strain in ply.local_strain[:,1]:
			top_strain += str(round(strain[0,0],3)).rjust(8)
		
		print("Bottom".ljust(10) + bottom_strain)
		print("Top".ljust(10) + top_strain)

def print_ABD(laminate):
	aux = np.matrix([[0. for row in range(6)] for col in range(6)])
	for i in range(6):
		for j in range(6):
			aux[i,j] = round(laminate.ABD()[i,j],3)
	print(aux)

def print_A(laminate):
	aux = np.matrix([[0. for row in range(3)] for col in range(3)])
	for i in range(3):
		for j in range(3):
			aux[i,j] = round(laminate.ABD()[i,j],3)
	print(aux)

def print_B(laminate):
	aux = np.matrix([[0. for row in range(3)] for col in range(3)])
	for i in range(3):
		for j in range(3):
			aux[i,j] = round(laminate.ABD()[i+3,j],3)
	print(aux)

def print_D(laminate):
	aux = np.matrix([[0. for row in range(3)] for col in range(3)])
	for i in range(3):
		for j in range(3):
			aux[i,j] = round(laminate.ABD()[i+3,j+3],3)
	print(aux)