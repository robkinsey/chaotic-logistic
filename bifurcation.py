# What we want to do:
#   Map out doubling birfurcations with the logistic map: x1 = r*x0*(1-x0)
# How to do it:
#   Run the logistic map equation multiple times using different values for r
#   On each iteration, plot the limit(s) using matplotlib

import matplotlib.pyplot as plt
import numpy as np

def run_single_logistic(r, x0, iterations, ret_length) :
  x = x0
  n = 1
  arr_result = np.zeros( iterations )
  arr_result[0] = x0
  while n < iterations :
    x = r * x * ( 1 - x )
    arr_result[n] = x
    n = n + 1
  return arr_result[ len(arr_result)-ret_length : ]

def run_multi_logistic(r0, r_max, r_increment, x0, iterations, ret_length) :
  r = r0
  
  # Using n as a counter variable for number of runs.
  # Calculate n_runs as the number of runs there will be in the model.
  n = 0
  n_runs = int ( (r_max - r0) / r_increment )
  print("n_runs: %d" % (n_runs))
  
  # Create an array to store the results of all the model runs.
  # Length will be the number of runs, width will be the number of results
  #  returned from each run.
  arr_results = np.zeros( ( n_runs , ret_length ) )  

  while n < n_runs :
    arr_results[n] = run_single_logistic( r, x0, iterations, ret_length )
    n = n + 1
    r = r + r_increment
  
  return arr_results

### Experiments in this section ###

# Do a single run
#arr_s = run_single_logistic( 4.0, 0.63, 100, 100 )
#plt.plot(arr_s, ',-g',lw=0.25)
#plt.show()

# Do a range of runs
arr_m = run_multi_logistic( 2.9, 4.0, 0.001, 0.15, 100, 20 )
plt.plot( arr_m, ',-g' , lw=0.25 )
plt.show()
