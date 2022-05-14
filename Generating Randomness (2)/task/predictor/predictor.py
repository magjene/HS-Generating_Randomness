"""
Stage 3/4: Predicting future input
Description
Now we will start predicting the next symbol of the user input. You will be surprised how often people repeat the same patterns!

Imagine the following: after the second stage for a string 0101010100101001010101000111101010010101010010101010101 we have calculated the amount of a certain character (0 or 1) that follows a specific triad of numbers: '000': [0, 1], '001': [4, 1], '010': [5, 16], '011': [0, 1], '100': [1, 4], '101': [16, 0], '110': [0, 1], '111': [1, 1]. Now, the user enters the sequence 001110. How can we foresee the next numbers?

Starting with the 4th character, we can predict the input based on the triads obtained in the previous stage. We've learned that the combination "001" (the first three characters) was followed by a "0" in 4 cases out of 5. So, the estimated probability that the user will enter "0" as the fourth character is 4/5 = 80%. For "1" probability is 1/5 = 20%. Therefore, we predict "0'" as the fourth character. Unfortunately, we didn't guess but let's go further. In the same way, the 5th character is more likely to be "1" relying on statistics for the triad preceding it ("011"). This time we are right. In this stage, you're invited to write a program, which will sequentially scan three characters of the user's sequence at a time and make a prediction of what goes next.

And what about the first three characters? Generate a sequence of three binary numbers, and that's it. Based on this triple, make predictions for further symbols.

Objectives
In this stage, your program should:

Take and preprocess user input as described in stage 1.
Calculate user statistics using triads as described in stage 2 (but don't output the statistics this time).
Ask the user to enter another test string of 0's and 1's, which we will try to predict, and preprocess the new input.
Going through the string entered by the user, estimate the frequency of occurrence of "0" or "1" after each triad and generate predictions: if the count of 0's after the current triad is higher, the program should predict "0", otherwise, predict "1". If the counts are equal, the choice can be made in a random way.
The first three symbols may be predicted by chance one by one using the random module. You can also invent your own algorithm here, for instance, make use of the overall frequencies of 0's and 1's in the user input. In the output, print your prediction right after the user's test string.
Test the accuracy of our predictor (excluding the first 3 randomly predicted symbols) by comparing the real input and the prediction. As the final output, print the line Computer guessed right N out of M symbols (ACC%), where N is the number of correctly guessed symbols, M is the total length of the test input, and ACC is the accuracy value with 0.01% precision. Remember to exclude the first 3 symbols from the calculation!
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Print a random string containing 0 or 1:

> 0101001010010101011111100010010110000101010101010100101
The current data length is 55, 45 symbols left
Print a random string containing 0 or 1:

> 01010101001010010101010001111001010010101010010101010101

Final data string:
010100101001010101111110001001011000010101010101010010101010101001010010101010001111001010010101010010101010101


Please enter a test string containing 0 or 1:

0110001010100101
prediction:
1101011010101101

Computer guessed right 10 out of 13 symbols (76.92 %)
"""


from random import randint

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

real_str = input('\nPlease enter a test string containing 0 or 1:\n\n')
prediction = '000'
for i in range(len(real_str)-3):
    triad = real_str[i:i+3]
    number = real_str[i+3]
    predict_number0, predict_number1 = dict_triad[triad]
    predict_number = '0' if predict_number0 > predict_number1 else '1'
    prediction += predict_number

print('prediction:')
print(prediction)
print()
print(f'Computer guessed right 10 out of {len(real_str)-3} symbols (76.92 %)')
'''
0101001010010101011111100010010110000101010101010100101
01010101001010010101010001111001010010101010010101010101
0110001010100101
'''
