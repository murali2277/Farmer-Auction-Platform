# Auction Platform

A console-based auction platform application with role-based access for Farmers and Customers.

## Project Structure

```
Auction_Platform/
├── main.py                 # Application entry point
├── controller/             # Application controllers (MVC)
│   ├── __init__.py
│   ├── auth_controller.py
│   ├── customer_controller.py
│   ├── farmer_controller.py
│   └── (bid logic lives inside role controllers)
├── models/                 # Data models
│   ├── __init__.py
│   ├── bids.py
│   ├── customer.py
│   ├── farmer.py
│   └── user.py
├── views/                  # User interface views
│   ├── __init__.py
│   ├── auth_views.py
│   ├── base_views.py
│   ├── customer_views.py
│   └── farmer_views.py
├── requirements.txt        # Project dependencies
└── README.md              # This file
```

## Setup

### Prerequisites
- Python 3.8 or higher

### Installation

1. Clone or download the project
2. Navigate to the project directory:
   ```bash
   cd Auction_Platform
   ```

3. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
python main.py
```

## Features

- **Farmer Role**: Create bids, view products, close bids
- **Customer Role**: View all bids, place bid requests, view won bids
- **Authentication**: Simple role-based login system

## Code Quality Notes

This is a learning/demo project. For production use, consider:
- Replace global state with proper session handling
- Add input validation and error handling
- Implement database persistence layer
- Add comprehensive unit tests
- Implement API layer for scalability
- Add logging and monitoring
