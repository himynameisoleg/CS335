import sys

def main():
    file = sys.argv[1]
    # file = "healthyeating.txt"

    lines = len(open(file).readlines())
    unique = get_unique_words(file)
    words = get_words(file)
    chars = get_chars(file)

    most_freq = get_most_freq(file) 
    less_freq = get_less_freq(file)


    print(f'lines: {lines}, unique: {unique}, words: {words}, chars: {chars}')
    print(f'Most frequent word: {most_freq["word"]} ({most_freq["count"]} times),',
        f'Less frequent word: {less_freq["word"]} ({less_freq["count"]} {"time" if less_freq["count"] < 2 else "times"}).')

def get_words(file):
    return len(open(file).read().lower().split())

def get_unique_words(file):
    return len(set(open(file).read().lower().split()))

def get_chars(file):
    return len(open(file).read())

def get_most_freq(file):
    words = open(file).read().lower().split()

    freq = {
        "word": "",
        "count": 0
    }
    
    freq["word"] = max(set(words), key = words.count)
    freq["count"] = words.count(freq["word"])
    return freq

def get_less_freq(file):
    words = open(file).read().lower().split()

    freq = {
        "word": "",
        "count": 0
    }

    freq["word"] = min(set(words), key = words.count)
    freq["count"] = words.count(freq["word"])
    return freq

main()