# CompositesLib

CompositesLib is a Python package designed for composite materials 
calculations, laminate stresses and failure indexes.

## Installation

`pip install -i https://test.pypi.org/simple/ CompositesLib`

## Basic Usage
```
    from compositeslib.classes import *
    from compositeslib.plot import *
    from compositeslib.output import *

    ply1 = ply(
        e1=55000.,
        e2=18000.,
        nu12=0.3,
        g12=6000.,
        thickness=0.5,
        )

    laminate1 = laminate([
        (ply1, 45),
        (ply1, -30),
        (ply1, 0),
        (ply1, -30),
        (ply1, 45),
        ])

    load1 = load(nx=1524, ny=200)

    calculate_stress(laminate1, load1)

    print_stress(laminate1)
    plot_stress(laminate1)
```
