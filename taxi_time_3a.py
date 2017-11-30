

"""
Last time, we simulated a single instance of a user defined time, but is that really enough for us to make a hard decision?

In this example, we're going to simulate a 1000 times to see on average which line truly has the advantage of being picked up more often
by taxis so that we know which line to hop on next time when we get the chance

We also organize the hardcoding by creating functions
"""

import random

taxi_line = 0

# randomly generate time for each passenger in each line to get in the taxi
def generate_passengers(num_of_passengers):

    # how long each passenger takes to get into the taxi
    passenger_times = {
        "line_1":0,
        "line_2":0,
        "line_3":0
    }

    # tracker for time until open for pickup for each line
    cur_pass_time = {
        "line_1":0,
        "line_2":0,
        "line_3":0
    }

    # for each passenger in each line, randomly generate a number (in seconds)
    for i in passenger_times:
        wait = []
        for j in range(num_of_passengers):
            wait.append(random.randint(2, 10))
        passenger_times[i] = wait
    return(passenger_times, cur_pass_time)

# create a dictionary of taxis with randomly generated arrival times
def generate_taxis(time, num_of_taxi):

    # create an empty list for taxi_arrival_times
    taxi_arrival_times = []

    # for each taxi, generate the time of arrival (in seconds) based on the given time and a random number between 0-120
    for i in range(num_of_taxi):
        taxi_arrival_times.append(random.randint(1, time + random.randint(0,120)))
    return(taxi_arrival_times)

# checks to see line is open for pickup and there are passengers in line for pickup
def taxi_arrives(taxi_arrival_times, taxi_line):

     # sort the list, purley for us to visualize
     taxi_arrival_times = sorted(taxi_arrival_times)

     # decrease everyone's time by 1 second
     taxi_arrival_times = [each - 1 for each in taxi_arrival_times]

     # count number of times that have reached 0 and add that to taxi_line
     taxi_line += len([each for each in taxi_arrival_times if each == 0])

     # create a new list that doesn't include 0 times
     taxi_arrival_times = [each for each in taxi_arrival_times if each != 0]

     # return the new taxi_line and taxi_arrival_times
     return(taxi_line, taxi_arrival_times)

# checks to see if there is a next passenger in line and the line is open for pickup
# cur_pass_time count doesn't start until a taxi is available
""" we make a change by taking out the global taxi_line, and replacing it as an input in the function to avoid global/local variable confusion """

def passenger_pickup(line, taxi_line, passenger_times, cur_pass_time, total_pickup):
    # if passenger is in line, taxi is ready for pickup, and no one is boarding the taxi
    if len(passenger_times[line]) != 0 and cur_pass_time[line] == 0 and taxi_line > 0:

        # add passenger's time to line time
        cur_pass_time[line] = cur_pass_time[line] + passenger_times[line].pop(0)

        # add 1 to count of total passenger picked up for that line
        total_pickup[line] += 1

        # decrease the total number of available taxi by 1
        taxi_line -= 1
        return(cur_pass_time[line], total_pickup[line], taxi_line)

    # if passengers are waiting in line, but taxi is not available for pickup
    elif len(passenger_times[line]) != 0 and cur_pass_time[line] == 0 and taxi_line == 0:

        # skip
        return(cur_pass_time[line], total_pickup[line], taxi_line)

    # if current passenger is still getting in the taxi, and
    elif cur_pass_time[line] > 0 :

        # decrease line time by 1
        cur_pass_time[line] -= 1
        return(cur_pass_time[line], total_pickup[line], taxi_line)

    # otherwise
    else:

        # skip
        return(cur_pass_time[line], total_pickup[line], taxi_line)

# write a function to simulate the taxi arrival and passenger pickup
def simulate(time, taxi_line, taxi_arrival_times, passenger_times, cur_pass_time, total_pickup):
    for i in range(time):
        taxi_line, taxi_arrival_times = taxi_arrives(taxi_line = taxi_line, taxi_arrival_times = taxi_arrival_times)
        cur_pass_time['line_1'], total_pickup['line_1'], taxi_line = passenger_pickup('line_1', taxi_line, passenger_times, cur_pass_time, total_pickup)
        cur_pass_time['line_2'], total_pickup['line_2'], taxi_line = passenger_pickup('line_2', taxi_line, passenger_times, cur_pass_time, total_pickup)
        cur_pass_time['line_3'], total_pickup['line_3'], taxi_line = passenger_pickup('line_3', taxi_line, passenger_times, cur_pass_time, total_pickup)
    return(taxi_line, taxi_arrival_times, cur_pass_time, total_pickup)

"""
cool! so far, so good. But it seems like line 3 is slightly lower each time I run it... I want to verify this simulation
further by repeating it 1000 times and storing the results of the total_pickup each time
"""
