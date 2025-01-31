# Tourism Management System

This is a comprehensive **Tourism Management System** designed to manage users, destinations, packages, bookings, payments, and reviews, along with engaging content such as blogs and FAQs.
# Jirani-Tours

Jirani-Tours is a comprehensive tourism management system designed to streamline the process of booking tours, managing destinations, and handling payments.

## Technologies Used
- Django
- Python
- PostgreSQL
- JavaScript (for front-end integration)
- Bootstrap

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Astro-cmd/Jirani---Tours.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Jirani---Tours
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your database and environment variables.

## Usage Instructions
- Run the development server:
  ```bash
  python manage.py runserver
  ```

## Contributing
If you'd like to contribute, feel free to open an issue or submit a pull request.

## Features

### 1. **User Management**
- Role-based user system: `admin`, `tourist`, `operator`.
- User registration, login, and profile management.

### 2. **Destinations**
- Manage destinations with detailed information such as name, location, and description.
- Upload and display destination images.

### 3. **Packages**
- Create travel packages linked to destinations.
- Manage package details like price, availability, and duration.

### 4. **Bookings and Payments**
- Book travel packages with status tracking (`pending`, `confirmed`, `cancelled`).
- Payment integration supporting multiple methods (`credit card`, `PayPal`, `M-Pesa`).
- Generate invoices for successful payments.

### 5. **Reviews**
- Tourists can leave ratings and reviews for destinations.

### 6. **Content Management**
- Blog publishing system with tagging and image uploads.
- FAQs for common questions.
- Contact form for inquiries.

---

## Database Structure

### Tables Overview

#### Users
Handles user authentication and role-based access.

#### Destinations
Stores information about travel destinations.

#### Packages
Manages travel packages associated with destinations.

#### Bookings
Tracks package bookings by users.

#### Payments
Records payment transactions for bookings.

#### Reviews
Enables users to review destinations.

#### Blogs
Manages blogs and articles for user engagement.

#### FAQs
Stores frequently asked questions.

#### Contacts
Manages inquiries sent through the contact form.

---

## Installation

### Prerequisites
- Python 3.9+
- PostgreSQL
- Django 5.1.4

### Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd tourism-management-system
   ```
2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure the database in `.env`:
   ```env
   DATABASE_URL=postgres://<username>:<password>@localhost:5432/<dbname>
   ```
5. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Run the server:
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

### User Management
- **POST** `/api/auth/register/` - Register a new user.
- **POST** `/api/auth/login/` - Login a user.

### Destinations
- **GET** `/api/destinations/` - List all destinations.
- **POST** `/api/destinations/` - Add a new destination.

### Packages
- **GET** `/api/packages/` - List all packages.
- **POST** `/api/packages/` - Add a new package.

### Bookings
- **POST** `/api/bookings/` - Create a new booking.
- **GET** `/api/bookings/<id>/` - Get booking details.

### Payments
- **POST** `/api/payments/` - Make a payment.

### Reviews
- **POST** `/api/reviews/` - Add a review for a destination.

### Content Management
- **GET** `/api/blogs/` - List all blogs.
- **POST** `/api/blogs/` - Add a new blog.
- **GET** `/api/faqs/` - List FAQs.

---

## Technologies Used

### Backend
- **Django**: Framework for the backend.
- **Django REST Framework (DRF)**: API development.

### Database
- **PostgreSQL**: Relational database for structured data.

### Frontend (Optional)
- Integration-ready for modern frontend frameworks (e.g., React, Vue).

---

## Contributions

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes and push:
   ```bash
   git commit -m "Description of changes"
   git push origin feature-name
   ```
4. Create a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).# Jirani--Tours-and-travel
