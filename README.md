# Telegram Echo Bot

A **Python-based Telegram bot** that **echoes** any text messages it receives. The bot also sends a personalized greeting upon receiving the `/start` command. This bot is built using the **PyTelegramBotAPI** library and utilizes **environment variables** to securely store the Telegram Bot API key.

## Features

### **Bot Management**
- **Personalized Greeting**: Upon starting the bot, it sends a custom greeting using the user’s name.
- **Echo Functionality**: The bot echoes back any text message sent by the user, providing a simple interactive experience.
- **Environment Configuration**: The bot’s Telegram API key is managed using environment variables for enhanced security.

### **User Interaction**
- **Start Command**: Upon sending `/start`, the bot sends a welcome message.
- **Text Echoing**: Any text sent to the bot will be echoed back to the user, providing instant feedback.

### **Security**
- The bot’s API key is securely stored using environment variables, preventing accidental exposure of sensitive information.
- The bot does not store any user data, making it lightweight and privacy-conscious.

## Requirements

- **Python 3.8+**
- **PyTelegramBotAPI** library (`pyTelegramBotAPI`)
- **python-dotenv** library to load environment variables

## Installation

### 1. Clone the repository
Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/GhostKX/Echo-Bot.git
```

### 2. Navigate to the file
```
cd Echo-Bot
```

### 3. Install the required dependencies
```
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a .env file in the root directory and add your Telegram Bot API key:
```
API_KEY=Your-Telegram-API-Key
```

### 5. Run the bot
```
python EchoBot_firstbot.py
```

## Usage

The system provides the following options for interaction:

- **/start**: Sends a personalized greeting message.
- **Text Echoing**: Any text you send to the bot will be echoed back.

## Example Usage Scenario
```
Welcome to the Telegram Echo Bot!

Choose an option:
/start
>>> Hi, John Doe
>>> Welcome to the First Echo bot!

Text message echo:
>>> Hello Bot
>>> Hello Bot
```

## Code Structure

### Core Functions

The bot is built with the following core functions:

- **`start()`** – Handles the `/start` command and sends a personalized greeting to the user.
- **`echo()`** – Echoes any text message sent by the user.
- **`load_dotenv()`** – Loads environment variables from the `.env` file, ensuring the bot’s API key is securely loaded.

### Dependencies

- **PyTelegramBotAPI**: The Python library used to interact with the Telegram Bot API.
- **python-dotenv**: A library to load environment variables from a `.env` file to keep the bot’s API key secure.

### Security & Validation

- **Environment Variables**: The Telegram API key is securely stored in a `.env` file and accessed through the `os.getenv()` function.
- **Bot Security**: The bot does not collect or store user data, ensuring privacy and security for its users.

## Author

- Developed by **GhostKX**
- GitHub: **[GhostKX](https://github.com/GhostKX/Echo-Bot)**


## Acknowledgments

- **PyTelegramBotAPI**: The Python library used to interact with the Telegram Bot API.
- **python-dotenv**: A Python library to load environment variables from a `.env` file.
