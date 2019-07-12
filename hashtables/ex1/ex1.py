#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    Example:
    input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
    output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
    """

    for i in range(0, len(weights)):
        hash_table_insert(ht, weights[i],  i)

    # will continue later

    return None


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
