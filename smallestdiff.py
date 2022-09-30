"""Given two lists, find the smallest difference between any two nums.

For example, given the lists:

  {10, 20, 14, 16, 18}
  {30, 23, 54, 33, 96}

The result would be 3, since 23 - 20 = 3 is the smallest difference of
any pair of numbers in those lists.

IMPORTANT: you must solve this with an algorithm that is faster than
O(ab)---that is, you cannot compare each item of list a against
each item of list b (that would be O(ab) time).

Joel Burton <joel@joelburton.com>.

Adapted from a problem in `Cracking the Coding Interview, 6th Edition`.
Gayle Laakmann McDowell, Career Cup (Palo Alto, CA). 2015.
"""


def smallest_diff(a, b):
    """Return smallest diff between all items in a and b.

        >>> smallest_diff([10, 20, 30, 40], [15, 25, 33, 45])
        3
        
    """

    a = [*set(a)]   #removes duplicates from the list
    b = [*set(b)]

    if len(a) < len(b): #ensures longer list will be the one halved (approx)
        b.sort()
        long_list = b
        short_list = a
    else:
        a.sort()
        long_list = a
        short_list = b
    
    candidates = set()    #sets are unique, so it'll be shorter than short_list

    for item in short_list:            #whole short_list will be checked
        previous = None
        for subtractor in long_list:   #maybe half long_list will be checked
            diff = abs(item - subtractor) 
            if previous == None:       #first subtractor handling
                previous = diff
                continue
            elif previous < diff:      #stop checking when diff starts growing
                candidates.add(previous)
                break
            elif subtractor == long_list[-1]:   #edge case: record final diff
                candidates.add(diff)
            previous = diff            #prepares previous for next loop
                
    return min(candidates)
    


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NICE WORK!\n")
