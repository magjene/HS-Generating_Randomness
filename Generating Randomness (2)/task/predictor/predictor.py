"""
Stage 4/4: ”Generate randomness” game
Description
In the final stage, we will gather all our components to construct a game where you will try to beat the system created by your hands. Initially, the player has a virtual balance of $1000. Every time the computer guesses a symbol correctly, the player loses one dollar. Every time the system is wrong, the player gets one dollar.

Objectives
In this final stage, your program should:

Get and preprocess user input just like in stage 1.
Learn user patterns by collecting triad statistics like in stage 2.
Ask the user to enter test strings or type enough to exit the game. Each test string must be preprocessed (in order to leave only "0" and "1" symbols). After that, you should launch the prediction algorithm and calculate the number of correctly guessed symbols. After each iteration, you should show the player's balance with the message Your balance is now $X, where X is the player's virtual balance. Since the first three symbols are guessed by chance, don't consider them when calculating the balance.
It would be great if you kept updating the system by allowing it to learn from the test data as well. However, this update should happen only after the prediction and the verification stages are done: let's be honest with the user.
Finish the game with the words Game over!.
Before implementing the solution, examine the example carefully. The output of your program should provide instructions and feedback in the same format.

Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Please give AI some data to learn...
The current data length is 0, 100 symbols left
Print a random string containing 0 or 1:

> 010100100101010101000010001010101010100100100101001
The current data length is 51, 49 symbols left
Print a random string containing 0 or 1:

> 011010001011111100101010100011001010101010010001001010010011

Final data string:
010100100101010101000010001010101010100100100101001011010001011111100101010100011001010101010010001001010010011

You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!

Print a random string containing 0 or 1:
> 0111001001
prediction:
1000101011

Computer guessed right 4 out of 7 symbols (57.14 %)
Your balance is now $999

Print a random string containing 0 or 1:
> some wrong input

Print a random string containing 0 or 1:
> 0101001001
prediction:
0001011011

Computer guessed right 5 out of 7 symbols (71.43 %)
Your balance is now $996

Print a random string containing 0 or 1:
> enough
Game over!
"""


print('Please give AI some data to learn...')
final_string = ''
current_string = []
while len(final_string) < 100:
    print(f'The current data length is {len(current_string)}, {100 - len(final_string)} symbols left')
    st = input('Print a random string containing 0 or 1:\n\n')
    current_string = [num for num in st if num in '01']
    final_string += ''.join(current_string)
print('\nFinal data string:')
print(final_string)

dict_triad = {'000': [0, 0], '001': [0, 0], '010': [0, 0], '011': [0, 0],
              '100': [0, 0], '101': [0, 0], '110': [0, 0], '111': [0, 0]}

for i in range(len(final_string) - 3):
    triad = final_string[i:i + 3]
    number = final_string[i + 3]
    if number == '0':
        dict_triad[triad][0] += 1
    else:
        dict_triad[triad][1] += 1

balance = 1000
print()
print(f'You have ${balance}. Every time the system successfully predicts your next press, you lose $1.')
print('Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!')
while balance > 0:
    while True:
        real_str = input('\nPrint a random string containing 0 or 1:\n')
        if real_str == 'enough':
            break
        current_string = [num for num in real_str if num in '01']
        real_str = ''.join(current_string)
        if len(real_str) > 3:
            break
    if real_str == 'enough':
        break
    prediction = '000'
    predict_true = 0
    for i in range(len(real_str)-3):
        triad = real_str[i:i+3]
        predict_number0, predict_number1 = dict_triad[triad]
        predict_number = '0' if predict_number0 > predict_number1 else '1'
        prediction += predict_number
        if real_str[i+3] == predict_number:
            predict_true += 1
    len_real_str = len(real_str) - 3
    balance += len_real_str - predict_true * 2
    print('prediction:')
    print(prediction + '\n')
    print(f'Computer guessed right {predict_true} out of {len_real_str} symbols '
          f'({round(predict_true / len_real_str * 100, 2)} %)')
    print(f'Your balance is now ${balance}')
print('Game over!')
