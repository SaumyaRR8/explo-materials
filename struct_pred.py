import streamlit as st
from pprint import pprint

from pymatgen.analysis.structure_matcher import ElementComparator, StructureMatcher
from pymatgen.analysis.structure_prediction.substitution_probability import (
    SubstitutionPredictor,
)
from pymatgen.analysis.structure_prediction.substitutor import Substitutor
from pymatgen.core.periodic_table import Specie
from pymatgen.ext.matproj import MPRester
from pymatgen.transformations.standard_transformations import (
    AutoOxiStateDecorationTransformation,
)

if 'n_rows' not in st.session_state:
    st.session_state.n_rows = 1

add = st.button(label="add")

if add:
    st.session_state.n_rows += 1
    st.experimental_rerun()

for i in range(st.session_state.n_rows):
    #add text inputs here
    st.text_input(label="element", key=i)
    st.text_input(label="oxidation state", key=i+1)


mpr = MPRester(api_key="o1lrM5n9tEieOI21bPihwSI9vapMyFzG")

threshold = 0.001  # threshold for substitution/structure predictions
num_subs = 10  # number of highest probability substitutions you wish to see

original_species = [
    Specie("Na", 1),
    Specie("Mn", 3),
    Specie("O", -2),
] 

subs = SubstitutionPredictor(threshold=threshold).list_prediction(original_species)
subs.sort(key=lambda x: x["probability"], reverse=True)
subs = subs[0:num_subs]
pprint(subs)

trial_subs = [list(sub["substitutions"].keys()) for sub in subs]
pprint(trial_subs)

elem_sys_list = [[specie.element for specie in sub] for sub in trial_subs]

chemsys_set = set()
for sys in elem_sys_list:
    chemsys_set.add("-".join(map(str, sys)))

pprint(chemsys_set)

'''all_structs = {}
for chemsys in chemsys_set:
    all_structs[chemsys] = mpr.get_structures(
        chemsys
    )

auto_oxi = (
    AutoOxiStateDecorationTransformation()
)  # create object to determine oxidation states at each lattice site

oxi_structs = {}

for chemsys in all_structs:
    oxi_structs[chemsys] = []

    for num, struct in enumerate(all_structs[chemsys]):
        try:
            oxi_structs[chemsys].append(
                {
                    "structure": auto_oxi.apply_transformation(struct),
                    "id": str(chemsys + "_" + str(num)),
                }
            )
        except Exception:
            continue  # if auto oxidation fails, try next structure
pprint(oxi_structs)'''
