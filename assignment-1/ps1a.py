###########################
# 6.0002 Problem Set 1a: Space Cows
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """


    cow_dict = {}
    with open(filename) as f:
        for line in f:
            (key, val) = line.split(',')
            cow_dict[key] = val
    print(cow_dict)
    return cow_dict

    # TODO: Your code here

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trip_list = []
    copyCows = cows.copy()
    sortedCows = sorted(copyCows.items(), key = lambda x: x[1], reverse = True)
    while sum(copyCows.values())>0:
        ship = []
        total = 0
        for cow, value in sortedCows:
            if sortedCows[cow]+total <= limit:
                ship.append(cow)
                total+=value
                copyCows[cow] = 0
        trip_list.append(ship)
    return trip_list
# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    1. filter those list of lists that satisfy the condition i.e. limit is less than 10
    a. how to get the limit
    partitions = get_partitions(cows)
    min_partition = partitions[0]
    pruned_partitions = []
    for trips in partitions :
        for trip in trips:
            sum_weights = 0
            for cow in trip:
                sum_weights += cows[cow]
            if sum_weights > limit:
                break

        if trip.length() < min_trip.length():
            min_trip = trip

    return min_trip


# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass
load_cows("ps1_cow_data.txt")
