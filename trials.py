"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)
    


def get_all_evens(nums):
    even_nums = []
    
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
       
    return even_nums

def get_odd_indices(items):
    result = []
    for index in range(len(items)): 
        # the solution is printing the even-index items
        if index % 2 != 0:
            result.append(items[index])
    
    return result
    print(result)


def print_as_numbered_list(items):
    i = 1
    
    for item in items: 
        print(f"{i}. {item}")
        i += 1
 

def get_range(start, stop):
    nums = []
    for num in range(start, stop):
        nums.append(num)
    return nums

def censor_vowels(word):
    pass  # TODO: replace this line with your code


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
