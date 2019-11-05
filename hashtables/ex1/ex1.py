#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

# This is the two sum problem 
# https://coderbyte.com/algorithm/two-sum-problem
# https://www.youtube.com/watch?v=8uYHAM-dtVA
# https://www.youtube.com/watch?v=2uWRxgN1Sbo

def get_indices_of_item_weights(weights, length, limit):
    # instantiate Hashtable object with a capacity of 16
    ht = HashTable(16)

    # iterate through weights list
    for index, item in enumerate(weights):
        # set variable match to the difference between the weight limit and the current item's weight
        match = hash_table_retrieve(ht, limit - item)
        # if the sum of the weights of both items equals the weight limit
        if match is not None:
            # if index is larger than match
            if index > match:
                # return the higher value in the 0th index
                return (index, match)
            # else match is larger than index, no need to swap
            return (match, index)
        else:
            hash_table_insert(ht, item, index)
    
    # there are no two items in weights who's sum is equal to the limit
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
