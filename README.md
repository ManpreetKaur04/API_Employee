# Employee Management API

This is a Django REST API project for managing employees in a company. It includes CRUD operations, JWT authentication, employee filtering, pagination, and ordering.

## Features

- Employee CRUD operations
- JWT Authentication (login, refresh)
- Filtering by department and role
- Ordering by name and date joined
- Pagination
- Unit tests for each endpoint

## Technologies

- Django
- Django REST Framework
- SimpleJWT for JWT authentication

## Installation

### Prerequisites

- Python 3.x
- Git

### Setup Instructions

1. **Clone the repository**:
     ```bash
    git clone https://github.com/ManpreetKaur04/API_Employee.git
    cd employee-management

2. Create a virtual environment:
    python -m venv env

3. Activate the virtual environment:
    On Windows:
        .\env\Scripts\activate
    On macOS and Linux:
        source env/bin/activate

4. Install the required packages:
    pip install -r requirements.txt

5. Run database migrations:
    python manage.py migrate

6. Create a superuser for the Django admin interface:
    python manage.py createsuperuser

7. Start the development server:
    python manage.py runserver

### Postman Testing Instructions:

1. Postman Installed: Ensure you have Postman installed on your computer.

2. API Running: Make sure your Django server is running (e.g., python manage.py runserver).

3. Registered User: You need to have at least one registered user to log in and access the employee endpoints.   
    Method: POST   
    URL: http://localhost:8000/api/register/   
    Headers- Content-Type: application/json   
    Body- Select raw and choose JSON as the format, then enter:   
        {   
            "username": "testuser",   
            "password": "testpassword"   
        }   
    Expected Response- 201 Created   
        {   
            "message": "User created successfully"   
        }   
   
4. Login to Obtain JWT Token   
    Method: POST   
    URL: http://localhost:8000/api/login/   
    Headers- Content-Type: application/json    
    Body- Select raw and choose JSON as the format, then enter:   
        {  
            "username": "testuser",   
            "password": "testpassword"   
        }   
    Expected Response- 200 OK   
        {    
            "refresh": "your_refresh_token",   
            "access": "your_access_token"   
        }    
Note: Save the access_token for the next requests.   

5. Create an Employee   
    Method: POST    
    URL: http://localhost:8000/api/employees/    
    Headers- Authorization: Bearer <your_access_token> (use the token obtained in Step 2), Content-Type: application/json   
    Body- Select raw and choose JSON as the format, then enter:   
        {   
            "name": "Alice Johnson",   
            "email": "alice@example.com",   
            "department": "Engineering",   
            "role": "Developer"   
        }   
    Expected Response- 201 Created   
        {   
            "id": 1,    
            "name": "Alice Johnson",   
            "email": "alice@example.com",   
            "department": "Engineering",   
            "role": "Developer",   
            "date_joined": "2024-11-01"   
        }   

6. List All Employees   
    Method: GET   
    URL: http://localhost:8000/api/employees/   
    Headers- Authorization: Bearer your_access_token   
    Expected Response- 200 OK   
        {   
             "id": 1, "name": "Alice Johnson",   
             "email": "alice@example.com",    
             "department": "Engineering",    
             "role": "Developer",    
             "date_joined": "2024-11-01"    
        }    
   
8. Retrieve a Single Employee     
    Method: GET    
    URL: http://localhost:8000/api/employees/1/ (replace 1 with the employee's ID)     
    Headers- Authorization: Bearer your_access_token    
    Expected Response- 200 OK    
        {    
            "id": 1,   
            "name": "Alice Johnson",   
            "email": "alice@example.com",   
            "department": "Engineering",   
            "role": "Developer",    
            "date_joined": "2024-11-01"   
        }   

9. Update an Employee   
    Method: PUT   
    URL: http://localhost:8000/api/employees/1/ (replace 1 with the employee's ID)   
    Headers- Authorization: Bearer your_access_token, Content-Type: application/json   
    Body- Select raw and choose JSON as the format, then enter:   
        {   
            "name": "Alice Smith",   
            "email": "alice.smith@example.com",   
            "department": "Engineering",   
            "role": "Senior Developer"   
        }   
    Expected Response- 200 OK    
        {   
            "id": 1,   
            "name": "Alice Smith",   
            "email": "alice.smith@example.com",    
            "department": "Engineering",    
            "role": "Senior Developer",    
            "date_joined": "2024-11-01"    
        }   

9.Delete an Employee   
    Method: DELETE    
    URL: http://localhost:8000/api/employees/1/ (replace 1 with the employee's ID)   
    Headers- Authorization: Bearer your_access_token   
    Expected Response- 204 No Content    
    No response body expected.    

10. Logout   
    Method: POST   
    URL: http://localhost:8000/api/logout/   
    Headers- Content-Type: application/json    
    Body- Select raw and choose JSON as the format, then enter:   
        {   
            "refresh": "your_refresh_token"    
        }   
    Expected Response- 205 Reset Content    
        {     
            "message": "User logged out successfully"    
        }     



Summary of Endpoints:     

-Register User: POST /api/register/  
-Login User: POST /api/login/   
-Create Employee: POST /api/employees/   
-List Employees: GET /api/employees/   
-Retrieve Employee: GET /api/employees/{id}/   
-Update Employee: PUT /api/employees/{id}/     
-Delete Employee: DELETE /api/employees/{id}/     
-Logout: POST /api/logout/   
