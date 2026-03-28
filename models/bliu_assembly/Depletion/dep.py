#!/groups/tripoli/openmc/openmc_env/bin/python

import openmc
import openmc.deplete as dep

materials = openmc.Materials.from_xml("materials.xml")
geometry = openmc.Geometry.from_xml("geometry.xml")
settings = openmc.Settings.from_xml("settings.xml")
chain = dep.Chain.from_xml("chain_endfb71_sfr.xml")

MSFR_model = openmc.model.Model(geometry,materials,settings)

#openmc.deplete.pool.USE_MULTIPROCESSING = False
with openmc.StatePoint('statepoint.400.h5') as sp:
    k_eff = sp.keff
operator = dep.Operator(MSFR_model,"chain_endfb71_sfr.xml")
dt=[0.1, 0.3, 0.6, 1.0, 3.0, 8.0, 17.0, 27.0, 40.0, 51.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0]
power = 3e9

leqi = dep.PredictorIntegrator(operator, dt, power=power, timestep_units='d')
leqi.integrate()
