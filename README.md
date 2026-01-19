# BankAPI

A Django-based REST API for managing bank cards and transactions with Telegram integration.

## Features

- Card management (create, view, update)
- Transaction processing between cards
- Balance checking
- Phone number verification via Telegram bot
- Comprehensive API documentation
- Transaction history tracking

## Tech Stack

- Python 3.12
- Django 5.0.4
- Django REST Framework
- SQLite (for development)
- Telegram Bot API integration

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd BankAPI
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

## API Documentation

The API documentation is available at `/docs/` endpoint when the server is running.

## Environment Configuration

- The project uses SQLite as the default database
- DEBUG mode is set to False by default
- The Telegram bot token is hardcoded in views.py (update for production)

## Endpoints

- `GET /cards/` - Retrieve all cards or filter by phone number
- `GET /card/{card_number}` - Get specific card details
- `GET /transactions/` - Retrieve all transactions or filter by phone number/card
- `POST /send_code/` - Send verification code via Telegram
- `POST /check_code/` - Verify the received code
- `POST /add_card/` - Add a card after verification
- `POST /transaction/` - Process a money transfer between cards

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT
