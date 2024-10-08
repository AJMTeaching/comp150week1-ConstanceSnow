# ------------------------------------------------------------------------

# Lab 1
# Problem 1
# Put your solution here, make sure I can run it by running this file. Do not submit it commented out.
# 1. Create a list called my_list with the values [1, 5, 'apple', 20.5].
my_list = [1, 5, 'apple', 20.5]

#2. Using indexing, print the value 'apple' from my_list.
print(my_list[2])
# if 'apple' in my_list:
#     print(lst.index('apple'))
#3. Add the value 10 to the end of my_list using the append() method. Print the updated list.
my_list.append(10)
print(my_list)

#4. Remove the value 20.5 from my_list using the remove() method. Print the updated list.
my_list.remove(20.5)
print(my_list)

#5. Reverse the order of the elements in my_list using a method. Print the reversed list.
my_list.reverse()
print(my_list)  

# Problem 2
# Put your solution here, make sure I can run it by running this file. Do not submit it commented out.
#1. Create a dictionary called person with keys 'name', 'age', 'job' and values 'John', 30, 'teacher'.
person = {'name': 'John', 'age': '30', 'job': 'teacher'}

#2. Print the value corresponding to the 'job' key.
job = person['job']
print(job)

#3. Add a new key-value pair: 'city': 'Paris' to the person dictionary. Print the updated dictionary.
person['city'] = 'Paris'
print(person)

#4. Remove the 'age' key-value pair from person. Print the updated dictionary.
person.pop('age')
print(person)

#5. Iterate through the person dictionary and print out each key-value pair on a separate line.
for key, value in person.items():
    print(f"Key: {key}, Value: {value}")
# -----------------------------------------------------------------------------


# Importing sys for test function
import sys


# Custom Test Function
def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    msg = f"Test at line {linenum} {'PASSED' if did_pass else 'FAILED'}."
    print(msg)



# Function 1: count_vowels
def count_vowels(s: str) -> int:
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    x = 0
    for letter in s:
        if letter in vowel_list:
            x = x+1
    return x


    """
    Count the number of vowels in a string.

    Parameters:
    - s (str): The input string

    Returns:
    - int: The number of vowels in the string
    """
    # TODO: Implement this function
    


# Unit Tests for count_vowels
def test_count_vowels():
    test(count_vowels("hello") == 2)
    test(count_vowels("why") == 0)
    test(count_vowels("aeiou") == 5)
    test(count_vowels("") == 0)
    test(count_vowels("bcdfg") == 0)
    test(count_vowels("aeiouAEIOU") == 10)
    test(count_vowels("HELLO") == 2)
    test(count_vowels("aEiOu") == 5)
    test(count_vowels("a e i o u") == 5)
    test(count_vowels("rhythm") == 0)


# Function 2: merge_lists
def merge_lists(list1: list, list2: list) -> list:
    merged_list = []
    for item in list1:
        merged_list.append(item)
    for item in list2:
        merged_list.append(item)
    return merged_list

    # Define a function that accepts a list of strings.
    # Create through the list of strings.
    # Compute and append the length of each string.
    # Return the list of lengths.



    """
    Merge two sorted lists into a single sorted list.

    Parameters:
    - list1 (list): The first sorted list
    - list2 (list): The second sorted list

    Returns:
    - list: A new sorted list containing all elements from list1 and list2
    """
    # TODO: Implement this function
    


# Unit Tests for merge_lists
def test_merge_lists():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    merged = merge_lists(list1, list2)
    test(merged == [1, 2, 3, 4, 5, 6])
    test(merge_lists([], []) == [])
    test(merge_lists([1], [2]) == [1, 2])
    test(merge_lists([1, 1], [2, 2]) == [1, 1, 2, 2])
    test(merge_lists([1, 3, 5], []) == [1, 3, 5])
    test(merge_lists([], [2, 4, 6]) == [2, 4, 6])
    test(merge_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6])
    test(merge_lists([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test(merge_lists([1, 1, 2, 3], [1, 2, 2, 3]) == [1, 1, 1, 2, 2, 2, 3, 3])


# Function 3: word_lengths
def word_lengths(words: list) -> list:
   lengths = []
   for string in words:
        length = len(string)
        lengths.append(length)
        return lengths
     
   
   
    # TODO: Implement this function
    


# Unit Tests for word_lengths
def test_word_lengths():
    words = (["short", "mediummm", "longesttttt"])
    lengths = word_lengths(words)
    
    
    #def test_other_operations(self):
    #    self.assertEqual(other_operations([3, 2, 1]), ([3, 2, 1], 3))
    test(lengths == [5, 5, 6])
    test(word_lengths([]) == [])
    test(word_lengths(["word"]) == [4])
    test(word_lengths(["short", "mediummm", "longesttttt"]) == [5, 8, 10])
    test(word_lengths(["", "a", "ab", "abc"]) == [0, 1, 2, 3])
    test(word_lengths(["  ", "a b", " c "]) == [2, 3, 3])


# Function 4: reverse_string
def reverse_string(s: str) -> str:
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
    
    """
    Reverse a string.

    Parameters:
    - s (str): The input string

    Returns:
    - str: The reversed string
    """
    # TODO: Implement this function
    


# Unit Tests for reverse_string
def test_reverse_string():
    text = "python"
    reversed_text = reverse_string(text)
    test(reversed_text == "nohtyp")
    test(reverse_string("") == "")
    test(reverse_string("a") == "a")
    test(reverse_string("aaa") == "aaa")
    test(reverse_string("Hello, World!") == "!dlroW ,olleH")
    test(reverse_string("12345") == "54321")
    test(reverse_string("  spaces  ") == "  secaps  ")


# Function 5: intersection
def intersection(list1: list, list2: list) -> list:
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    intersection = []
    for item in list1:
        if item in list2 and item not in intersection:
            intersection.append(item)
    return intersection
 
 # To create a nested loop 
 # identify list
 # Create empty intersection list
 # 'for' loop statement 
 # If item in list 1 and item in list 2 and item no in intersection append to intersection list    
    """
    Find the intersection of two lists.

    Parameters:
    - list1 (list): The first list
    - list2 (list): The second list

    Returns:
    - list: The intersection of the two lists
"""
    # TODO: Implement this function
    


# Unit Tests for intersection
def test_intersection():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = intersection(list1, list2)
    test(result == [3, 4])
    test(intersection([], []) == [])
    test(intersection([1, 2], [3, 4]) == [])
    test(intersection([1, 2], [1, 2]) == [1, 2])
    test(intersection([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3])
    test(intersection([1, 2, 3], [4, 5, 6]) == [])
    test(intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3])


# Test Suite
def test_suite():
    print(f"Count Vowels Test Results:")
    test_count_vowels()
    print(f"Merge Lists Test Results:")
    test_merge_lists()
    print(f"Word Lengths Test Results:")
    test_word_lengths()
    print(f"Reverse String Test Results:")
    test_reverse_string()
    print(f"Intersection Test Results:")
    test_intersection()


test_suite()
