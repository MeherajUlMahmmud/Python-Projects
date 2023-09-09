# Email Sender

This repository contains a Python script for sending emails using the `smtplib` library, a part of the Python Standard Library, and the `email.message` module. This script provides a command-line interface to send emails easily.

## Prerequisites

Before you can use this script, make sure you have the following prerequisites:

-   Python 3.x installed on your system.
-   A Gmail account from which you want to send emails.
-   Less secure apps enabled for your Gmail account or an [App Password](https://support.google.com/accounts/answer/185833?hl=en) if you have 2-step verification enabled.

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

You can use this script to send emails by providing the recipient's email address, subject, and body through command-line arguments.

**Syntax:**

```
python main.py -r <receiver_email> -s <subject> -b <body>
```

**Example:**

```
python main.py -r somebody@gmail.com -s 'Hello' -b 'Hello World'
```

### Command-Line Arguments

-   `-r` or `--receiver`: The email address of the recipient.
-   `-s` or `--subject`: The subject of the email.
-   `-b` or `--body`: The body or content of the email.

## Configuration

Before using the script, you need to configure the sender's Gmail account and password:

1. Open the `main.py` file in a text editor.
2. Replace the `FROM_EMAIL` variable with your Gmail email address.
3. Set the `FROM_EMAIL_PASSWORD` variable to your Gmail password or an App Password if you have 2-step verification enabled.

**Note:** Be cautious with your Gmail password and never share it publicly or hardcode it in scripts without proper security measures.

## Sending Email

To send an email, run the script with the appropriate command-line arguments as described in the "Usage" section. The script will send the email using the provided Gmail account.

## Troubleshooting

If you encounter any issues while using this script, make sure:

-   Your Gmail account settings allow less secure apps or use an App Password.
-   You have an active internet connection.
-   The email address, subject, and body are provided correctly as command-line arguments.

## Disclaimer

This script is provided for educational and testing purposes. Use it responsibly and consider security best practices when handling email credentials.

For any questions or issues, please contact the repository owner at meherajmahmmd@email.com.

Happy emailing!
