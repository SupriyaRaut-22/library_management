# Library Management System

A web-based Library Management System built with **Django**.  
It helps librarians manage books, members, book issues/returns, and track outstanding debts.

---

## 🚀 Features

-  Search books by **title** and **author**
-  Import books from the [Frappe Library API](https://frappe.io)
-  Member management with outstanding debt control
-  Book inventory with CRUD operations
-  Issue & return books
-  Charge rent fees and auto-track outstanding balances
-  Block issuing to members with debt over ₹500

---
## Search Book
![Search Book](screenshots/Search%20book.PNG)

## Book List and CRUD
![Book List](screenshots/Book%20list%20and%20CRUD%20operations.PNG)

## Member List and CRUD
![Member List](screenshots/Member%20list%20and%20CRUD%20operations.PNG)

## Import Books from API
![Import](screenshots/Import%20books%20from%20API.PNG)

## Issue a Book
![Issue](screenshots/Issue%20a%20book.PNG)

## Blocked Member Example
![Blocked](screenshots/Debt%20more%20than%20500.PNG)

---

## Technologies Used

- Django 5.x
- Python 3.11+
- Bootstrap 5
- SQLite (default)
- Frappe API (for book imports)

---

## Setup Instructions

### Prerequisites
- Python 3.11+
- pip

### Database Setup
- python manage.py makemigrations
- python manage.py migrate

### Runserver
- python manage.py runserver


