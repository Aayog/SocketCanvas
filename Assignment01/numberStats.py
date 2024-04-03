"""
Name: Aayog Koirala
Date: Jan 16, 2020
Desc: Number Stats: gets numbers from the buffer and prints basic statistics
"""
# Example of Counter found from-> https://docs.python.org/2/library/collections.html

from collections import Counter

def get_list_of_count(counts, ct):
    return [x[0] for x in counts.most_common() if x[1] is ct]


least_count, most_count = 0, 0

numbers = []

try:
    while True:
        numbers.append(int(input()))
except:
    pass
# if Ctrl+D worked:
#    except EOFError:
#       pass

print(f'{len(numbers)} values entered.')
print(f'{min(numbers)} was the minimum value.')
print(f'{max(numbers)} was the maximum value.')
print(f'{sum(numbers)} was the sum.')

count = Counter(numbers)
most_count = count.most_common()[0][1]
least_count = count.most_common()[-1][1]

most_list = get_list_of_count(count, most_count)
least_list = get_list_of_count(count, least_count)

print(f'Least mentioned numbers (repeated {least_count} times): {least_list})')
print(f'Most  mentioned numbers (repeated {most_count} times): {most_list})')
