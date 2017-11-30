
# prior code assumed that passengers would get instantaneously picked up the second they became available
# for this exercise, we're going to a step closer to reality and begin to add delays and intervals in the taxis

"""
How this simulation works

1. taxi arrives from taxi_arrival_times and gets in taxi_line
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

# let's try to do this more intelligently
# randomly generate time for each passenger in each line to get in the taxi
number_of_passengers = 10
for i in passenger_times:
    wait = []
    for j in range(number_of_passengers):
        wait.append(random.randint(3, 10))
    passenger_times[i] = wait

# create a dictionary of taxis with randomly generated arrival times
num_of_taxi = 20
taxi_arrival_times = []
for i in range(num_of_taxi):
    taxi_arrival_times.append(random.randint(5, 10))

# create a count until next taxi arrives
next_t_arrive = 0

# there is a pool of taxis somewhere in the city that arrive somehwat sporadically
# these taxis arrive in what is called a taxi line that are readily available to pickup

taxi_line = 0

# checks to see line is open for pickup and there are passengers in line for pickup
def taxi_used(next_t_arrive, taxi_arrival_times, taxi_line):
    # if taxis are available for pickup
    if next_t_arrive == 0 and len(taxi_arrival_times) != 0:
        # take one taxi out from the taxi line and add time until next taxi arrives
        next_t_arrive = next_t_arrive + taxi_arrival_times.pop(0)
        # return the time until next taxi arrives and taxi line
        taxi_line += 1
        return(next_t_arrive, taxi_arrival_times, taxi_line)

    elif next_t_arrive !=0 and len(taxi_arrival_times) != 0:
        next_t_arrive -= 1
        return(next_t_arrive, taxi_arrival_times, taxi_line)

    else:
        return(next_t_arrive, taxi_arrival_times, taxi_line)

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

time = input("What time (in seconds): ")
time = int(time)

for i in range(time):

    print(i)
    next_t_arrive, taxi_arrival_times, taxi_line = taxi_used(next_t_arrive, taxi_arrival_times, taxi_line)
    print("next arrival time: ", next_t_arrive)
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
# total passengers picked up + taxis that are left should be equal to 20
print(total_pickup['line_1'] + total_pickup['line_2'] + total_pickup['line_3'] + len(taxi_arrival_times))
