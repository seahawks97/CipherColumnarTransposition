"""
Steven Tucker, Alec, and Grant
CSC 380
Assignment 1: Cipher
"""
import re

# INPUT: two text phrases. Will only count letters, not punctuation or numbers.
keyword = 'abc'
phrase = 'I am text from a Wikipedia page. Feed me hamburgers.'
print('Original keyword:', keyword)
print('Original phrase:', phrase)

# Parse strings
# keyword_a = keyword
# phrase_a = phrase
keyword_a = keyword.replace(' ', '').lower()              # Removes \s and makes lowercase
phrase_a = phrase.replace(' ', '')                        # Removes \s

keyword_a = re.sub(r'[^$\w\s]', '', keyword_a)
phrase_a = re.sub(r'[^$\w\s]', '', phrase_a)

keyword_a = re.sub(r'[\n\t]*', '', keyword_a)
phrase_a = re.sub(r'[\n\t]*', '', phrase_a)

print('Key (alpha only):', keyword_a)
print('Phrase (alpha only):', phrase_a)

# Makes top (editable) row for array
top = [x for x in keyword_a]
print('Top row:', top)

# Makes new array
array = []
array.append(top)
# print('Top row into array:', array)

# Calculate number of rows
pcounter = 0
kcounter = len(top)
for x in phrase:
    if x.isalpha():
        pcounter += 1
m = (pcounter // kcounter) + 1
print('m (# rows):', m)
print('Number of chars in phrase:', pcounter)
print('Number of chars in key:', kcounter)

# Construct rest of array
for i in range(m):
    array.append([x for x in phrase_a[:kcounter]])
    phrase_a = phrase_a[kcounter:]
print('New array:', array)
for j in range(kcounter - (pcounter % kcounter)):
    array[-1].append('x')
print('Final array (Xs appended):', array)

# Put array into order
order_list = [ord(x) for x in keyword_a]

# Generate string to be output
str_out = ''
# Make a copy of array so that I can edit it but also keep orig
array_copy = [[i for i in row] for row in array]
# Iterate through length of top row
for z in range(len(order_list)):
    # print('Order List:', order_list)
    # print('Current array:', array_copy)
    # Position is set to the index of the 1st minimum value
    mini_pos = order_list.index(min(order_list))
    for row in range(1, len(array_copy)):
        str_out += array_copy[row][mini_pos]
        array_copy[row].remove(array_copy[row][mini_pos])
    order_list.remove(min(order_list))

print('Length of string out:', len(str_out))
print('String out:', str_out)

input('Press Enter to exit: ')
