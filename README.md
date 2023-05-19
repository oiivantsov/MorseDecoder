# Morse Decoder
[![Python](https://img.shields.io/pypi/pyversions/tensorflow.svg)](https://badge.fury.io/py/tensorflow)

Morse Decoder is a Python program that allows you to encode English text into Morse code and decode Morse code back into English. It provides a command-line interface for easy interaction and supports basic punctuation marks, numbers, and uppercase letters.

## Features

- Encode English text into Morse code.
- Decode Morse code into English text.
- Preserve spaces between words during encoding and decoding.
- Handle invalid inputs gracefully and skip unrecognized characters or codes.
- Copy the result to the clipboard for easy sharing and pasting.

## Installation

1. Clone the repository:
https://github.com/oiivantsov/Morse.git

2. Install the required [pyperclip](https://pypi.org/project/pyperclip/) dependencies (to copy the coding result):
```
$ pip install pyperclip
```

## Usage

- Follow the prompts to encode or decode your text using Morse code. Enter '0' to encode or '1' to decode.
- For encoding, provide the text you want to convert into Morse code. For decoding, enter the Morse code, separating letters with '|' and words with spaces.
- After encoding or decoding, you will be prompted to copy the result to the clipboard. Enter 'Yes' or 'No' to proceed.

## Contributing

Contributions to Morse Decoder are welcome! If you have any ideas, improvements, or bug fixes, please submit a pull request. For major changes, please open an issue first to discuss the proposed changes.

## MISC

Data provided by http://introcs.cs.princeton.edu/java/data/

