
# In Korea, I stood in a line for taxi that split into 3 different lines
#
# That day, the line system somehow felt unfair, but I didn't know how to quantify the unfairness;
# today we will take this exercise to explore exactly how unfair that line was; visual representation of the line below
#
# taxi->taxi->taxi->
#
#  --    --    --
#  --    --    --
#  --    --    --
#        xx
#        xx
#        xx
#        xx

import random

total_pickup =
{
    "line_1":0,
    "line_2":0,
    "line_3":0
}

number_of_passengers = 10

# create an empty list that will be used to store wait times
wait = []

# use a random number generator to arbitrarily set wait times between 3 to 10 (seconds)
for i in range(number_of_passengers):
    wait.append(random.randint(3, 10))

# combine the generated numbers and line keys as tuples and convert to dictionary
line_1_passengers = wait

# repeat for line 2
wait = []

for i in range(number_of_passengers):
    wait.append(random.randint(3, 10))

line_2_passengers = wait

# repeat for line 3
wait = []

for i in range(number_of_passengers):
    wait.append(random.randint(3, 10))

line_3_passengers = wait

# initiate time to get into the vehicle starting with 0 passengers in each lane

time_to_open_1 = 0
time_to_open_2 = 0
time_to_open_3 = 0

# function to check if the line is open for pick up by taxi
def is_open(line):
    if line == 0:
        return(1)
    elif line > 0:
        return(0)
    else:
        return("Something is wrong and you need to fix it")
'''
Function that checks to see the following:

If time to open is 0 meaning person has finished getting in the category
1. add 1 to the count of persons picked up so far
2. once a person starts getting in, add the time back to the time_to_open

If time to open is not 0

1. decrease the time to open by 1
2. return the number of count of persons picked up

'''


# Function: checks to see if line is open and adjusts passenger count and time left in line
# Input: time left in the line, time taken by passenger, passenger pickup count key
# Output: result = updated time left in line, updated pickup count

def passenger_get_in(time_to_open, line_time, key):
    if is_open(time_to_open) == 1:
        time_to_open = time_to_open + line_time.pop(0) # add the time for passenger to get in to taxi and drop first passenger from line
        total_pickup[key] = total_pickup[key] + 1 # increase total_pickup for lane 1 by one
        result = [time_to_open, total_pickup[key]]
        return(result)
    else:
        result = [time_to_open - 1, total_pickup[key]]
        return(result)

# set the number of seconds we want to stop to count the passengers picked up by each lane
time = 30

for i in range(time):
    x = passenger_get_in(time_to_open_1, line_1_passengers, "line_1")
    time_to_open_1 = x[0]
    total_pickup["line_1"] = x[1]

    x = passenger_get_in(time_to_open_2, line_2_passengers, "line_2")
    time_to_open_2 = x[0]
    total_pickup["line_2"] = x[1]

    x = passenger_get_in(time_to_open_3, line_3_passengers, "line_3")
    time_to_open_3 = x[0]
    total_pickup["line_3"] = x[1]

# repeat this

print("")
print("Total passengers picked up so far:", total_pickup["line_1"])
print("Time left until open:", time_to_open_1)
print("Passengers waiting:", line_1_passengers)
print("")
print("Total passengers picked up so far:", total_pickup["line_2"])
print("Time left until open:", time_to_open_2)
print("Passengers waiting:", line_2_passengers)
print("")
print("Total passengers picked up so far:", total_pickup["line_2"])
print("Time left until open:", time_to_open_3)
print("Passengers waiting:", line_3_passengers)
print("")
