#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # create hashtable with capacity set to the length
    hashtable = HashTable(length)
    # initialize route list with lenth number of None elements
    route = [None] * length

    # iterate through tickets list
    for ticket in tickets:
        # create key value pair in hashtable with source as the key and destination as the value 
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # find the first flight ticket by looking for the ticket with the source equal to "NONE" 
    location = hash_table_retrieve(hashtable, "NONE")

    # iterative through all of the tickets
    for i in range(length):
        # set ith index of the list equal to location
        route[i] = location
        # update the next location 
        location = hash_table_retrieve(hashtable, location)

    # return the route list 
    return route
