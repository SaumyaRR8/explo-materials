

from pymatgen.electronic_structure.core import Spin
from pymatgen.ext.matproj import MPRester

# This initiliazes the Rest connection to the Materials Project db. Put your own API key if needed.
a = MPRester(api_key="o1lrM5n9tEieOI21bPihwSI9vapMyFzG")
# load the band structure from mp-3748, CuAlO2 from the MP db
bs = a.get_bandstructure_by_material_id("mp-3748")

# is the material a metal (i.e., the fermi level cross a band)
print(bs.is_metal())
# print information on the band gap
print(bs.get_band_gap())
# print the energy of the 20th band and 10th kpoint
print(bs.bands[Spin.up][20][10])
# print energy of direct band gap
print(bs.get_direct_band_gap())
# print information on the vbm
print(bs.get_vbm())

from pymatgen.electronic_structure.plotter import BSPlotter

plotter = BSPlotter(bs)
plotter.show()


plotter.plot_brillouin()