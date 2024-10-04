def test_location(cards, query, mid):
    if cards[mid] == query:
        #mid > 0 checks for out of range and 
        #checks if the left of mid is the same as query 
        #then return left 
        #else return found
        if mid > 0 and cards[mid - 1] == query:
            return "left"
        else:
            return "found"
    else:
        #checks if mid is less than query
        #return left
        #else return right
        #
        #if it was asccending order we swap the < to >
        if cards[mid] < query:
            return "left"
        else:
            return "right"
def binary_search_decsending_order(cards, query):
    #sets high to the last index in the list
    high = len(cards) - 1
    low = 0
    while low <= high:
        mid = (low + high) // 2
        result = test_location(cards, query, mid)

        if result == "found":
            return mid
        elif result == "left":
            high = mid - 1
        elif result == "right":
            low = mid + 1
    return -1
cards = [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
query = 6
result = binary_search_decsending_order(cards, query)

if result == -1:
    print("The query does not exist in list")
else:
    print(f"The query is in position {result}")
