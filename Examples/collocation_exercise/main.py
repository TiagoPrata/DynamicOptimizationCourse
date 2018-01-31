from apm import * # load APM Toolbox
import numpy as np

# define server and application names
s = 'http://byu.apmonitor.com'
a = 'node_test'

sol = np.empty(5) # store 5 results
i = 0
for nodes in range(2,7):
    apm(s,a,'clear all') # clear prior application
    apm_load(s,a,'collocation.apm') # load model
    csv_load(s,a,'collocation.csv') # load data
    apm_option(s,a,'nlc.imode',4)   # imode = 4, simulation
    apm_option(s,a,'nlc.nodes',nodes) # nodes (2-6)
    apm(s,a,'solve') # solve problem
    y = apm_sol(s,a) # retrieve solution
    sol[i] = y['x'][-1] # store solution (last point)
    i += 1

print sol
