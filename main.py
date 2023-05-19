from morse_decoder import MorseDecoder  # Import the MorseDecoder class from my own module "morse_decoder"


def main():
    # Display welcome message
    print('Welcome to Morse Decoder')

    while True:
        # Prompt the user for the encoding or decoding choice
        user_choice = input("Would you like to encode or decode your text?\n"
                            "Enter '0' to encode or '1' to decode: ")

        if user_choice == '0':
            # Encode the user's input
            user_input = input('Enter the message you want to encode: ').upper()
            morse_decoder.encode_message(user_input)
        elif user_choice == '1':
            # Decode the user's input
            user_input = input('Enter the message you want to decode:\n'
                               'Use "|" to separate letters and space to separate words: ')
            morse_decoder.decode_message(user_input)
        else:
            # Invalid input
            print("Invalid input. Please enter '0' or '1'.")

        # Check if the user wants to continue
        play_again = input("Do you want to continue? (Yes/No): ").lower()
        if play_again != 'yes':
            break


if __name__ == '__main__':
    # Create an instance of the MorseDecoder class
    morse_decoder = MorseDecoder()

    # Call the main function
    main()
