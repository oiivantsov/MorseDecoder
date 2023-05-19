from pyperclip import copy

# Load Morse code dictionary from file
with open('morse.csv', mode='r') as data:
    morse_list = data.readlines()
    # Create a dictionary to map characters to Morse code
    morse_dict = {ch.strip().split(',')[0]: ch.strip().split(',')[1] for ch in morse_list}
    # Create a reverse dictionary to map Morse code to characters
    morse_reverse = {value: key for key, value in morse_dict.items()}


class MorseDecoder:
    def encode_message(self, input_message):
        encoded_output = ''
        for char in input_message:
            if char == ' ':
                encoded_output += char
            elif char in morse_dict:
                # Convert character to Morse code and add it to the output
                encoded_output += morse_dict[char] + '|'
            else:
                # Skip characters that are not available in Morse code
                print(f"Skipping character: {char}. It is not available in Morse code.")
        # Copy the encoded message to the clipboard
        self.copy_to_clipboard(encoded_output)

    def decode_message(self, input_message):
        decoded_output = ''
        # Split the input message by the '|' separator to get individual Morse codes
        input_message = input_message.split('|')
        for code in input_message:
            if code == '':
                continue
            elif ' ' in code:
                # Handle the case when a space is present in the Morse code
                space = code[0]
                code_rest = code[1:]
                if code_rest in morse_reverse:
                    # Convert Morse code to character and add it to the output
                    decoded_output += space + morse_reverse[code_rest]
                else:
                    # Skip invalid Morse codes
                    print(f"Skipping code: '{code}'. It is not a valid Morse code.")
            else:
                if code in morse_reverse:
                    # Convert Morse code to character and add it to the output
                    decoded_output += morse_reverse[code]
                else:
                    # Skip invalid Morse codes
                    print(f"Skipping code: '{code}'. It is not a valid Morse code.")
        # Copy the decoded message to the clipboard
        self.copy_to_clipboard(decoded_output)

    def copy_to_clipboard(self, result):
        # Display the result
        print(f'Here is the result: {result}')
        user_copy = input("Do you want to copy the output? (Yes/No): ").lower()
        if user_copy == 'yes':
            # Copy the result to the clipboard
            copy(result)
            print("The output has been copied to the clipboard.")
        else:
            print("The output was not copied.")