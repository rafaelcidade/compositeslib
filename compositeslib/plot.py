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

import matplotlib.pyplot as plt
from classes import *

def plot_stress(laminate):
	stress_array = [[],[],[],[],[],[]]
	z_array = []
	layers = [-laminate.height/2.]
	for ply in laminate.plies:
		layers.append(ply.z[1])
		z_array.extend([ ply.z[0] , ply.z[1] ])
		for i in range(3):
			stress_array[i].extend([ round(ply.global_stress[i,0],2) , round(ply.global_stress[i,1],2) ])
			stress_array[i+3].extend([ round(ply.local_stress[i,0],2) , round(ply.local_stress[i,1],2) ])
		
	
	fig = plt.figure(facecolor="white")
	fig.subplots_adjust(hspace=0.7, wspace=0.3)
	left_column = [1,3,5]
	right_column = [2,4,6]
	title_array = [r"$\sigma_x$ (MPa)",r"$\sigma_y$ (MPa)",r"$\tau_{xy}$ (MPa)",
	r"$\sigma_1$ (MPa)",r"$\sigma_2$ (MPa)",r"$\tau{12}$ (MPa)"]
	
	for i in range(3):
		fig.add_subplot(3,2,left_column[i], title=title_array[i])
		#plt.plot(stress_array[i],z_array,color='blue')
		plt.fill_betweenx(z_array, 0, stress_array[i], color='blue', edgecolor='black', antialiased=True)
		plt.yticks(layers)
		plt.grid(True)
		plt.grid(True, axis="y",linestyle="-")
		fig.add_subplot(3,2,right_column[i], title=title_array[i+3])
		#plt.plot(stress_array[i+3],z_array,color='red')
		plt.fill_betweenx(z_array, 0, stress_array[i+3], color='red', edgecolor='black', antialiased=True)
		plt.yticks(layers)
		plt.grid(True)
		plt.grid(True, axis="y",linestyle="-")
	plt.show()

def plot_strain(laminate):
	strain_array = [[],[],[],[],[],[]]
	z_array = []
	layers = [-laminate.height/2.]
	for ply in laminate.plies:
		layers.append(ply.z[1])
		z_array.extend([ ply.z[0] , ply.z[1] ])
		for i in range(3):
			strain_array[i].extend([ ply.global_strain[i,0]*100, ply.global_strain[i,1]*100 ])
			strain_array[i+3].extend([ ply.local_strain[i,0]*100 , ply.local_strain[i,1]*100 ])

	fig2 = plt.figure(facecolor="white")
	fig2.subplots_adjust(hspace=0.7, wspace=0.3)
	left_column = [1,3,5]
	right_column = [2,4,6]
	title_array = [r"$\epsilon_x$ (%)",r"$\epsilon_y$ (%)",r"$\gamma_{xy}$ (%)",
	r"$\epsilon_1$ (%)",r"$\epsilon_2$ (%)",r"$\gamma{12}$ (%)"]
	
	for i in range(3):
		fig2.add_subplot(3,2,left_column[i], title=title_array[i])
		#plt.plot(strain_array[i],z_array,color='blue')
		plt.fill_betweenx(z_array, 0, strain_array[i], color='blue', edgecolor='black', antialiased=True)
		plt.yticks(layers)
		plt.grid(True)
		plt.grid(True, axis="y",linestyle="-")
		fig2.add_subplot(3,2,right_column[i], title=title_array[i+3])
		#plt.plot(strain_array[i+3],z_array,color='red')
		plt.fill_betweenx(z_array, 0, strain_array[i+3], color='red', edgecolor='black', antialiased=True)
		plt.yticks(layers)
		plt.grid(True)
		plt.grid(True, axis="y",linestyle="-")
	plt.show()

def plot_max_stress(ply):
	fig = plt.figure(facecolor="white")
	# Sigma1 x Sigma2
	fig.add_subplot(2,2,1)
	plt.xlabel(r'$\sigma_1$(MPa)')
	plt.ylabel(r'$\sigma_2$(MPa)')
	plt.grid(True)
	plt.plot(ply.local_stress[0,0],ply.local_stress[1,0], 'o')
	plt.plot(ply.local_stress[0,1],ply.local_stress[1,1], 'o')
	plt.legend(('Bottom', 'Top'), loc=0, numpoints=1)
	plt.plot([-ply.xc , ply.xt, ply.xt, -ply.xc, -ply.xc]
		,[ply.yt, ply.yt, -ply.yc, -ply.yc, ply.yt], color='red')
	# plot black line on axis
	plt.plot([-ply.xc + -ply.xc / 2, ply.xt + ply.xt / 2],[0,0], color='black')
	plt.plot([0,0],[-ply.yc + -ply.yc / 2, ply.yt + ply.yt / 2], color='black')
	# Set axis limits
	plt.xlim(-ply.xc + -ply.xc / 2, ply.xt + ply.xt / 2)
	plt.ylim(-ply.yc + -ply.yc / 2, ply.yt + ply.yt / 2)
	
	# Tau12 x Sigma2
	fig.add_subplot(2,2,2)
	plt.xlabel(r'$\tau_{12}$(MPa)')
	plt.ylabel(r'$\sigma_2$(MPa)')
	plt.grid(True)
	plt.plot(ply.local_stress[2,0],ply.local_stress[1,0], 'o')
	plt.plot(ply.local_stress[2,1],ply.local_stress[1,1], 'o')
	plt.legend(('Bottom', 'Top'), loc=0, numpoints=1)
	plt.plot([-ply.s , ply.s, ply.s, -ply.s, -ply.s]
		,[ply.yt, ply.yt, -ply.yc, -ply.yc, ply.yt], color='red')
	# plot black line on axis
	plt.plot([-ply.s + -ply.s / 2, ply.s + ply.s / 2],[0,0], color='black')
	plt.plot([0,0],[-ply.yc + -ply.yc / 2, ply.yt + ply.yt / 2], color='black')
	# Set axis limits
	plt.xlim(-ply.s + -ply.s / 2, ply.s + ply.s / 2)
	plt.ylim(-ply.yc + -ply.yc / 2, ply.yt + ply.yt / 2)

	# Tau12 x Sigma1
	fig.add_subplot(2,2,3)
	plt.xlabel(r'$\sigma_1$(MPa)')
	plt.ylabel(r'$\tau_{12}$(MPa)')
	plt.grid(True)
	plt.plot(ply.local_stress[0,0],ply.local_stress[2,0], 'o')
	plt.plot(ply.local_stress[0,1],ply.local_stress[2,1], 'o')
	plt.legend(('Bottom', 'Top'), loc=0, numpoints=1)
	plt.plot([ply.xt, ply.xt, -ply.xc, -ply.xc, ply.xt]
		,[-ply.s , ply.s, ply.s, -ply.s, -ply.s], color='red')
	# plot black line on axis
	plt.plot([0,0], [-ply.s + -ply.s / 2, ply.s + ply.s / 2],color='black')
	plt.plot([-ply.xc + -ply.xc / 2, ply.xt + ply.xt / 2], [0,0],color='black')
	# Set axis limits
	plt.xlim(-ply.xc + -ply.xc / 2, ply.xt + ply.xt / 2)
	plt.ylim(-ply.s + -ply.s / 2, ply.s + ply.s / 2)

	plt.show()