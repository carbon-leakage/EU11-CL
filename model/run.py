#!/usr/bin/python3

import sys
import numpy as np
import pypsa

from co2_price_scripts import co2_price_update

save_path = './results/'

mu = float(sys.argv[1])
alpha = float(sys.argv[2])

mu = round(mu)
alpha = round(alpha,1)

print('CO2 Price mu is:')
print(mu)
print('Distribution Factor alpha is:')
print(alpha)

network = pypsa.Network(csv_folder_name='./network/')

network = co2_price_update(network,mu,alpha)
network.lopf(solver_name='gurobi',snapshots=network.snapshots,
             solver_options={'method': 2, 'crossover': 0},
             solver_logfile=str(mu)+'_'+str(alpha)+'.log')

network.export_to_netcdf(save_path + str(mu) + '_' + str(alpha) + '.nc')
