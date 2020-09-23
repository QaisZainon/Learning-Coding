'''
two .txt  files with overlapping numbers, 
find the overlapping numbers
'''

with open('Practice Python\Exercise_23_prime.txt', 'r') as open_file:
    prime_num = open_file.read().split('\n')
with open('Practice Python\Exercise_23_happy.txt', 'r') as open_file:
    happy_num = open_file.read().split('\n')
common = []
for i in prime_num:
    if i in happy_num:
        common.append(i)
print(common)