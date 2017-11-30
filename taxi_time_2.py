
# Prior code assumed that taxis could only arrive after another and that the delay would begin once a taxi was in line.
# In this simulation, we'll add an extra feature to allow taxis to come in groups or almost concurrently

"""
How this simulation works

1. taxi(s) arrive from taxi_arrival_times and gets in taxi_line
2. if line 1 is ready for pickup, passenger from line 1 begins to board the taxi and start counting time to finish boarding
3. if line 2 is ready for pickup, passenger from line 1 begins to board the taxi and start counting time to finish boarding
4. if line 3 is ready for pickup, passenger from line 1 begins to board the taxi and start counting time to finish boarding
4. repeat

"""

import random

# tracker for total passenger pickup for each line
total_pickup = {
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

# how long each passenger takes to get into the taxi
passenger_times = {
    "line_1":0,
    "line_2":0,
    "line_3":0
}

time = input("> Choose how much time, in seconds, experiment should last: ")
time = int(time)

# let's try to do this more intelligently
# randomly generate time for each passenger in each line to get in the taxi
number_of_passengers = 10
for i in passenger_times:
    wait = []
    for j in range(number_of_passengers):
        wait.append(random.randint(3, 10))
    passenger_times[i] = wait

# create a dictionary of taxis with randomly generated arrival times
num_of_taxi = 50
taxi_arrival_times = []
for i in range(num_of_taxi):
    taxi_arrival_times.append(random.randint(1, time + random.randint(0,120)))

# this time, taxis can arrive at the same time
# we can allow this by pre-determining when at what second each taxi will arrive using list comprehension
#

taxi_line = 0

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
def passenger_pickup(line):
    global taxi_line
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

for i in range(time):

    print(i)
    taxi_line, taxi_arrival_times = taxi_arrives(taxi_line = taxi_line, taxi_arrival_times = taxi_arrival_times)
    print("taxi_arrival_times: ", taxi_arrival_times)
    print("taxi_line: ", taxi_line)
    print("")

    cur_pass_time['line_1'], total_pickup['line_1'], taxi_line = passenger_pickup('line_1')
    print("taxi_line: ", taxi_line)
    print("total picked up line 1: ", total_pickup['line_1'])
    print("current passenger time line 1: ", cur_pass_time['line_1'])

    cur_pass_time['line_2'], total_pickup['line_2'], taxi_line = passenger_pickup('line_2')
    print("taxi_line: ", taxi_line)
    print("total picked up line 2: ", total_pickup['line_2'])
    print("current passenger time line 2: ", cur_pass_time['line_2'])

    cur_pass_time['line_3'], total_pickup['line_3'], taxi_line = passenger_pickup('line_3')
    print("taxi_line: ", taxi_line)
    print("total picked up line 3: ", total_pickup['line_3'])
    print("current passenger time line 3: ", cur_pass_time['line_3'])
    print("")

# check
# total passengers picked up + taxis that are left (in line + haven't arrived yet) should be equal to number of taxis we started out with
print(total_pickup['line_1'] + total_pickup['line_2'] + total_pickup['line_3'] + len(taxi_arrival_times) + taxi_line)
