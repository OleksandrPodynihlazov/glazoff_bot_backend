# Glazoff Bot Backend

Glazoff Bot is a Telegram mini-app for managing service orders. The project consists of a Flask-based backend, a Telegram bot, and an SQLite database. The frontend part of this project is located at **frontend_glazoff_bot**.

## Project Structure

- `app.py` — Main backend application using Flask.
- `bot.py` — Telegram bot code that transmits and receives data from the mini-app.
- `database.py` — Module for interacting with the database.
- `.env` — Configuration file containing protected environment variables.
- `requirements.txt` — File listing dependencies.

## Features

### Backend (Flask)

1. **Retrieve service list** (`GET /services`)
    - Returns a list of available services from the database.

2. **Create an order** (`POST /api/orders`)
    - Accepts user order details and stores them in the database.

### Telegram Bot

1. **Launch the mini-app**
    - Sends a button to the user to open the web interface of the mini-app.

2. **Receive data from WebApp**
    - Processes data sent from the mini-app and forwards it to support.

### Database (SQLite)

- `web_orders`: Stores order details.
- `users`: Stores user information.

## Setup and Execution

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start the Backend

```bash
python app.py
```

### Start the Bot

```bash
python bot.py
```

### Environment Variables Setup

Create a `.env` file and add:

```
BOT_TOKEN=your_bot_token
MY_TELEGRAM_ID=your_id
SUPPORT_CONTACT=support_id
BASE_URL=your_backend_url
BOT_USERNAME=your_bot_username
```

## Technologies Used

- **Flask** — for the backend
- **Telegram Bot API** — for user interaction
- **SQLite** — for data storage
- **dotenv** — for managing environment variables

## Author

Glazoff Bot — A Telegram mini-app for service order management.

