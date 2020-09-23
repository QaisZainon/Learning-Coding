'''
Ask a number, creates a list of all divisors
'''

def all_divisors():
    ans = []
    num = int(input('Give me a number\n'))
    for i in range(1, num + 1):
        if num % i == 0:
            ans.append(i)
    return print(ans)

all_divisors()
