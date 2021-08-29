import sys

nums = [int(x) for x in sys.argv[1:]]

def get_most_frequent(elements):
    return max(set(elements), key = elements.count)

print(get_most_frequent(nums))