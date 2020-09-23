'''
Count how many each name there are in the file and print the results 
on the screen
'''

with open('Exercise_22.txt', 'r') as open_file:
    all_text = open_file.read().split('\n')
ans = {}
for attr in all_text:
    if attr not in ans:
        ans[attr] = 0
    ans[attr] += 1
print(ans)