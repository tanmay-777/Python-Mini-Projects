# 🔐 Caesar Cipher

A lightweight, crash-resistant terminal application for encrypting and decrypting secret messages using the classic Caesar Cipher method.

Whether you're hiding a message or cracking a code, this script handles alphanumeric characters and automatically copies your results to the clipboard.

## ✨ Features

* **Two-Way Translation:** Encrypt new messages or decrypt existing secrets on the fly.
* **Custom Keys:** Shift characters using any key from `0` to `46`.
* **Bulletproof Input:** Built-in error handling and input validation means accidental typos won't crash the script.
* **Smart Parsing:** Shifts letters and numbers (A-Z, 0-9) while leaving spaces and punctuation exactly as they are.
* **Auto-Copy:** Automatically sends the final output to your clipboard for instant pasting.

## 🚀 Quick Start

### Prerequisites


You'll need Python 3 installed, along with the `pyperclip` module for clipboard support.

```bash
pip install pyperclip
```

### Running the App

Navigate to the project folder and run the script from your terminal:

```bash
python caesar_cipher.py
```

## 💻 Usage

The script runs an interactive loop right in your terminal. Here's what a quick session looks like:

```text
Welcome to Caesar Cipher Encryption/Decryption
Do you wanna (E)ncrypt or (D)ecrypt using Caesar Cipher?
> e
Enter the size of key ranging from 0 to 35:
> 5
Write the message to encrypt:
> HELLO GITHUB 2024!

The encrypted message is:
MJQQT LNYMZF 7579!
(Message copied to clipboard!)

Do you wanna try this again? (y/n)
> n
```

## 🛠️ Built With

* **Python 3** - Core logic and terminal interface.
* **Pyperclip** - Cross-platform clipboard integration.
* **Zero Magic:** Built using fundamental string manipulation, modular math (wrap-around logic), and continuous `while` loops for a seamless terminal experience.