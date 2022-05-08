"""
Stage 1/4: Input processing
Description
In order to train the machine to predict the next user input, we need to collect data about the user. We will ask them to press 0's and 1's on the keyboard in an unpredictable order. These data will be kept in a string of the format "011100101010...". All other characters should not be taken into account (in case the user makes a mistake and presses "2" instead of "1", for example).

Objectives
In this stage, your program should:

Set the minimal length of the string of zeros and ones that the user should enter. Let's choose the value 100: this will allow you to collect enough statistics without taking too much of the user's time.
Filter out inappropriate symbols from each user input.
Append the processed string to the general string containing all the data from the input.
Keep asking the user for new input strings and appending them to the general string until the length of the general string is equal or exceeds 100. If it exceeds 100, don't remove extra symbols: 100 symbols are the minimum required length, but the more data we have, the better.
Output the final data string.
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

For simplicity, we will limit ourselves to a string of length 20 in this example.

Print a random string containing 0 or 1:

> 01000111001
Current data length is 11, 9 symbols left
Print a random string containing 0 or 1:

> 2345
Current data length is 11, 9 symbols left
Print a random string containing 0 or 1:

> 1010456
Current data length is 15, 5 symbols left
Print a random string containing 0 or 1:

> 0100010

Final data string:
0100011100110100100010
"""


general_string = ''
while len(general_string) < 100:
    st = input('Print a random string containing 0 or 1:\n\n')
    for num in st.split():
        if num == '0' or num == '1':
            general_string += st
    print(f'Current data length is {len(st)}, {100 - len(general_string)} symbols left')
print(general_string)
