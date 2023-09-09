# Random Password Generator

This Python script allows you to generate random passwords of specified lengths, including lowercase letters, uppercase letters, digits, and special characters.

## Prerequisites

Before you can use this script, make sure you have the following prerequisites:

-   Python 3.x installed on your system.
-   Basic knowledge of using the command line.

## Installation

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/MeherajUlMahmmud/Python-Projects.git
    ```

2. Navigate to the project directory:

    ```
    cd EmailSender
    ```

## Usage

Run the script with the desired password length as an argument:

```bash
python main.py 12
```

Replace `12` with the desired password length.

The script, `main.py`, consists of two main functions:

1. `generate_password(length)`: Generates a random password of the specified length.

2. `main()`: Parses the command-line argument for the desired password length and prints the generated random password.

## Customization

You can customize the following aspects of the generated passwords by modifying the code:

-   Password length: Change the length argument when calling `generate_password`.
-   Character sets: Modify the `lowercase_letters`, `uppercase_letters`, `digits`, and `special_characters` variables to adjust the character sets used in password generation.

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## Acknowledgments

-   Inspired by the need for secure and randomly generated passwords.
-   Built with Python's `random` and `argparse` modules.

Feel free to use and modify this script for your password generation needs. Enjoy your random passwords!
