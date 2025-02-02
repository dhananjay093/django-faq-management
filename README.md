# FAQ Management System

## Installation
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run migrations: `python manage.py migrate`.
4. Start Redis server.
5. Run the server: `python manage.py runserver`.

## API Usage
- Get English FAQs: `GET /api/faqs/`
- Get Hindi FAQs: `GET /api/faqs/?lang=hi`
- Get Bengali FAQs: `GET /api/faqs/?lang=bn`

## Contributing
- Follow PEP8 guidelines.
- Write tests for new features.
- 
