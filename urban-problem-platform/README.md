# Urban Problem Reporting and Navigation Platform

This project is designed to provide a platform for reporting urban problems and navigating through various points of interest in Guinea. Users can report issues they encounter in their urban environment and receive guidance on navigating through the city.

## Features

- **Problem Reporting**: Users can submit reports about urban issues such as potholes, broken streetlights, and other infrastructure problems.
- **Navigation**: The platform provides navigation features to help users find routes and points of interest.
- **Database**: Utilizes SQLite3 for data storage, making it lightweight and easy to manage.
- **Admin Interface**: An admin interface is available for managing reports and navigation data.

## Setup Instructions

1. **Clone the Repository**:
   ```
   git clone <repository-url>
   cd urban-problem-platform
   ```

2. **Create a Virtual Environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Requirements**:
   ```
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage Guidelines

- Users can navigate to the reporting section to submit new reports.
- The navigation section allows users to view routes and alerts.
- Admins can manage reports and navigation data through the Django admin interface.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.