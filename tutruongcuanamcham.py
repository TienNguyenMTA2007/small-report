import numpy as np
import matplotlib.pyplot as plt

from pyGDM2 import structures
from pyGDM2 import materials
from pyGDM2 import fields
from pyGDM2 import propagators
from pyGDM2 import core
from pyGDM2 import visu

step = 20              # nm
radius = 160           # nm

geometry = structures.sphere(
    step,
    R=8.2,
    mesh="cube"
)

# Hạt điện môi: n = 2
material = materials.dummy(2.0)

struct = structures.struct(
    step,
    geometry,
    material
)

wavelengths = [400]    # nm

field_generator = fields.plane_wave

kwargs = dict(
    inc_angle=0,
    inc_plane="xz",
    theta=0
)

efield = fields.efield(
    field_generator,
    wavelengths=wavelengths,
    kwargs=kwargs
)

n1 = 1.0

dyads = propagators.DyadsQuasistatic123(
    n1
)
sim = core.simulation(
    struct,
    efield,
    dyads
)

core.scatter(sim)

visu.vectorfield_color_by_fieldindex(
    sim,
    0,
    projection="XZ",
    slice_level=0
)

plt.show()