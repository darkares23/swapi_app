

# Star Wars Planets API (swapi_app)

A Django project that utilizes the SWAPI to fetch information about planets from the Star Wars universe and exposes them via GraphQL and Django Rest Framework.

## Features

- **Django** as the web framework.
- **GraphQL** for querying third-party API and exposing the data.
- **Django Rest Framework** for RESTful endpoints.
- **Celery** for asynchronous tasks.
- **Redis** as the broker for Celery.
- **Docker and Docker Compose** for containerization and local development.

## Requirements

- Docker and Docker Compose installed.

## Usage Instructions

1. **Clone the Repository**:
   ```
   git clone https://github.com/your_username/swapi_app.git
   cd swapi_app
   ```

2. **Build the Containers**:
   ```
   make build
   ```

3. **Start the Containers**:
   ```
   make up
   ```

4. **Run Migrations**:
   First, create migrations:
   ```
   make migrations
   ```
   Then apply them:
   ```
   make migrate
   ```

5. **Access the Application**:
   - Populate Data: [http://localhost:8000/populate/](http://localhost:8000/populate/)
   - List Planets: [http://localhost:8000/planets/](http://localhost:8000/planets/)
   - Create Planet: [http://localhost:8000/planet/](http://localhost:8000/planet/)
   - Update Planet: [http://localhost:8000/planet/<int:pk>/](http://localhost:8000/planet/<int:pk>/)
   - Delete Planet: [http://localhost:8000/planet/<int:pk>/delete/](http://localhost:8000/planet/<int:pk>/delete/)
   - admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)


6. **Access Django Shell**:
   ```
   make shell
   ```

7. **View Application Logs**:
   ```
   make logs
   ```

8. **Run Tests**:
   ```
   make test
   ```

9. **Create Superuser**:
   If you want to access the Django Admin:
   ```
   make createsuperuser
   ```

10. **Shutdown and Cleanup**:
   To stop the services:
   ```
   make down
   ```
   To clean pyc files:
   ```
   make clean
   ```


## License

[MIT](https://choosealicense.com/licenses/mit/)

---
