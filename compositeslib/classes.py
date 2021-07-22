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

# please, follow http://www.python.org/dev/peps/pep-0008/#naming-conventions

import copy
import numpy as np
from micromechanics import *
from macromechanics import *


class ply:

    z = [0., 0.]  # [bottom, top]
    thickness = 0.

    def __init__(
            self,
            e1,
            e2,
            g12,
            nu12,
            thickness,
            xt=None,
            xc=None,
            yt=None,
            yc=None,
            s=None,
            e1t=None,
            e1c=None,
            e2t=None,
            e2c=None,
            e12s=None,
            woven=None):
        self.e1 = e1
        self.e2 = e2
        self.g12 = g12
        self.nu12 = nu12
        self.thickness = thickness
        self.xt = xt
        self.xc = xc
        self.yt = yt
        self.yc = yc
        self.s = s
        self.e1t = e1t
        self.e1c = e1c
        self.e2t = e2t
        self.e2c = e2c
        self.e12s = e12s
        self.density = None
        self.woven = woven
        if woven is None:
            self.woven = False

        self.theta = 0.

    # [matrix<0> = bottom face value , matrix<1> = top face value]
        self.local_stress = np.matrix(
            [[0. for col in range(2)] for row in range(3)])
        self.local_strain = np.matrix(
            [[0. for col in range(2)] for row in range(3)])
        self.global_stress = np.matrix(
            [[0. for col in range(2)] for row in range(3)])
        self.global_strain = np.matrix(
            [[0. for col in range(2)] for row in range(3)])

    def q(self):
        e1 = self.e1
        e2 = self.e2
        g12 = self.g12
        nu12 = self.nu12
        nu21 = self.nu12 * e2 / e1
        return np.matrix([[e1 / (1 - nu12 * nu21),
                           nu12 * e2 / (1 - nu12 * nu21),
                           0.],
                          [nu21 * e1 / (1 - nu12 * nu21),
                           e2 / (1 - nu12 * nu21),
                           0.],
                          [0.,
                           0.,
                           g12]])

    def ql(self):
        if not self.woven:
            return t(self.theta).I * self.q() * t(self.theta).I.T
        # Sets zero to shear-extension coupling elements
        else:
            q_l = t(self.theta).I * self.q() * t(self.theta).I.T
            q_l[0, 2] = q_l[1, 2] = q_l[2, 0] = q_l[2, 1] = 0
            return q_l


class laminate():
    def __init__(self, input_plies):
        self.plies = []
        self.height = 0.
        self.strain_curvature = np.matrix([0. for row in range(6)])
        if input_plies is None:
            print("Missing plies. Please, set [(ply, angle), ... ]")
            return
        for plies in input_plies:
            ply = copy.deepcopy(plies[0])
            ply.z = plies[0].z[:]  # shallow copy of z using slice operator
            ply.local_stress = copy.copy(plies[0].local_stress)
            ply.local_strain = copy.copy(plies[0].local_strain)
            ply.global_stress = copy.copy(plies[0].global_stress)
            ply.global_strain = copy.copy(plies[0].global_strain)
            ply.theta = plies[1]
            self.height += ply.thickness
            self.plies.append(ply)

        thickness_beneath = 0.
        for ply in self.plies:
            ply.z[0] = - self.height / 2. + thickness_beneath
            ply.z[1] = ply.z[0] + ply.thickness
            thickness_beneath += ply.thickness

        self.C = self.ABD()[0:3, 0:3] / self.height
        self.S = self.C.I
        self.rho = (2 * self.S[0, 1] + self.S[2, 2]) / \
            (2 * math.sqrt(self.S[0, 0] * self.S[1, 1]))

    def ABD(self):
        abd = np.matrix([[0. for row in range(6)] for col in range(6)])

        for ply in self.plies:
            abd[0:3, 0:3] += ply.ql() * (ply.z[1] - ply.z[0])
            abd[3:6, 0:3] += ply.ql() * (ply.z[1]**2 - ply.z[0]**2) / 2.
            abd[0:3, 3:6] += ply.ql() * (ply.z[1]**2 - ply.z[0]**2) / 2.
            abd[3:6, 3:6] += ply.ql() * (ply.z[1]**3 - ply.z[0]**3) / 3.
        return abd


class load(object):
    def __init__(self, nx=None, ny=None, nxy=None, mx=None, my=None, mxy=None):
        self.nx = (0 if nx is None else nx)
        self.ny = (0 if ny is None else ny)
        self.nxy = (0 if nxy is None else nxy)
        self.mx = (0 if mx is None else mx)
        self.my = (0 if my is None else my)
        self.mxy = (0 if mxy is None else mxy)
