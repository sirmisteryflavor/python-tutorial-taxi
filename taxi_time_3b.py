
from taxi_time_3 import taxi_arrives, passenger_pickup, simulate, generate_passengers, generate_taxis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
taxi_line
time
trials
"""

taxi_line = 0
# set the time for which we want to run each simulation
time = input("Enter the time for each simulation to run: ")
time = int(time)
trials = input("Enter the number of simulations that we should run: ")
trials = int(trials)

# create container lists that we'll store the results in

line_1_score = []
line_2_score = []
line_3_score = []


# ask the user for number of taxis
num_of_taxi = input("How many taxis per line? ")
num_of_taxi = int(num_of_taxi)

# ask user for number of passengers
num_of_passengers = input("How many passengers per line? ")
num_of_passengers = int(num_of_passengers)

# repeat the simulation for a set number of times
for i in range(trials):

    # tracker for total passenger pickup for each line
    total_pickup = {
        "line_1":0,
        "line_2":0,
        "line_3":0
    }

    # generate new taxi_arrival_times
    taxi_arrival_times = generate_taxis(time, num_of_taxi)

    # generate new taxi_arrival_times
    passenger_times, cur_pass_time = generate_passengers(num_of_passengers)

    # simulate the passenger pick up given the time, taxi_line, and taxi_arrival_times
    taxi_line, taxi_arrival_times, cur_pass_time, total_pickup = simulate(time, taxi_line, taxi_arrival_times, passenger_times, cur_pass_time, total_pickup)

    # record the total number of passengers picked up from each line
    line_1_score.append(total_pickup['line_1'])
    line_2_score.append(total_pickup['line_2'])
    line_3_score.append(total_pickup['line_3'])

# we'll print average of the results
print("line 1: ", sum(line_1_score)/len(line_1_score))
print("line 2: ", sum(line_2_score)/len(line_2_score))
print("line 3: ", sum(line_3_score)/len(line_3_score))

# we can also visaulize this using packages from python

# turn the lists into a series with row names as just the index number
a = pd.Series(line_1_score, index = range(len(line_1_score)))
b = pd.Series(line_2_score, index = range(len(line_2_score)))
c = pd.Series(line_3_score, index = range(len(line_3_score)))

# build a dictionary of the outcome
d = {
'line_1_pickup': line_1_score,
'line_2_pickup': line_2_score,
'line_3_pickup': line_3_score
}

# build a pandas dataframe from our dictionary
d = pd.DataFrame(d)

# initialize the histogram by filtering on each line
# set transparency to 50% with labels

plt.hist(d['line_1_pickup'], alpha = 0.5, label = 'line_1')
plt.hist(d['line_2_pickup'], alpha = 0.5, label = 'line_2')
plt.hist(d['line_3_pickup'], alpha = 0.5, label = 'line_3')
plt.legend(loc = 'upper right')
plt.show()
