'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    
    def the_count(word, i):
        if i > 0:
            part_to_match = word[i-2:i]
            print(part_to_match)
            if part_to_match == "th":
                nonlocal count
                count += 1
            the_count(word, i-1)

    the_count(word, len(word))
    return count
