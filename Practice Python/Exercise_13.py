'''
Asks the user how many numbers to generate
'''
def fibonnaci_sequence():
    times = int(input('How many times do you want to generate the fibonnaci sequence\n'))
    input_num1 = int(input('First number of the sequence\n'))
    input_num2 = int(input('Second number of the sequence\n'))
    sequence = []
    sequence.append(input_num1)
    sequence.append(input_num2)
    for i in range(times):
        sequence.append(sequence[-2] + sequence[-1])
    return print(sequence)

fibonnaci_sequence()