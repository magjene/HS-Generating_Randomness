"""
Stage 2/4: Analyzing user input
Description
Now it's time to reveal the secret of our magical predictive system. We will create a "profile" of the user that will contain information about patterns found in their "random" clicks. To do this, we will count how many times a certain character (0 or 1) follows a specific triad of numbers (for example, 000 or 011). For example, in the string "00010000", the triad "000" is followed once by a "0" and once by "1".

In the next stage, we will create a prediction algorithm based on this information.

Objectives
In this stage, your program should:

Read the user input the same way it did in the previous stage.
Output the result in the following format: triad: counts of 0, counts of 1, for example, 000: 57,12. The result for each triad should be printed on a new line. The triads must be ordered in ascending order of their decimal representation (for example, 110 in binary = 1*4+1*2+0*1 = 6 in decimal).
Hint

How many different triads are there? There are three vacant seats: _ _ _. Two options (0 or 1) for the first seat, then two options for the second seat and so on. In the case of the same number of options at each seat, the number of unique sequences can be calculated as follows:
\text {number of options} ^ {\text {number of seats}}
number of options
number of seats

Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Print a random string containing 0 or 1:

> 01010010010001010100100101001001
The current data length is 32, 68 symbols left
Print a random string containing 0 or 1:

> 10100011001010101010111101001001011010
The current data length is 70, 30 symbols left
Print a random string containing 0 or 1:

> 0101101010100110101010101010001110011

Final data string:
01010010010001010100100101001001101000110010101010101111010010010110100101101010100110101010101010001110011

000: 0,3
001: 10,5
010: 13,18
011: 5,2
100: 3,12
101: 20,3
110: 2,5
111: 2,1
"""


general_string = ''
while len(general_string) < 100:
    st = input('Print a random string containing 0 or 1:\n\n')
    current_string = [num for num in st if num in '01']
    general_string += ''.join(current_string)
    print(f'Current data length is {len(current_string)}, {100 - len(general_string)} symbols left')
print('\nFinal data string:')
print(general_string)

dict_triad = {'000': [0, 0], '001': [0, 0], '010': [0, 0], '011': [0, 0],
              '100': [0, 0], '101': [0, 0], '110': [0, 0], '111': [0, 0]}

for i in range(len(general_string)-3):
    triad = general_string[i:i+3]
    number = general_string[i+3]
    if number == '0':
        dict_triad[triad][0] += 1
    else:
        dict_triad[triad][1] += 1

print()
for key, val in dict_triad.items():
    print(f'{key}: {val[0]},{val[1]}')
