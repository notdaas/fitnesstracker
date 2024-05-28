# Fitness Tracker

A web application to track fitness activities and goals, built with Django. This project includes user authentication, activity logging, goal setting, and data visualization with Chart.js.

## Features

- **User Authentication:** Secure login and registration functionality.
- **Activity Logging:** Users can log various fitness activities with details like type, duration, distance, and calories burned.
- **Goal Setting:** Users can set fitness goals and track their progress.
- **Dashboard:** A user-friendly dashboard displaying activities and goals.
- **Data Visualization:** Interactive charts to visualize fitness data over time.

## Technologies Used

- **Backend:** Django, SQLite
- **Frontend:** Bootstrap, Chart.js, Custom CSS
- **Other:** HTML, JavaScript

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/notdaas/fitnesstracker.git
    cd fitnesstracker
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and navigate to `http://127.0.0.1:8000/fitness/`.

## Usage

- **Log in or Register:** Create an account or log in with an existing one.
- **Log Activities:** Navigate to "Log Activity" to record your fitness activities.
- **Set Goals:** Navigate to "Set Goal" to define your fitness goals.
- **View Dashboard:** Check your logged activities and goals on the dashboard.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests.


