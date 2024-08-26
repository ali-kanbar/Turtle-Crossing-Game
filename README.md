# Turtle Crossing Game

## Project Overview
An interactive game where the goal is to help the turtle to cross the street and avoid getting hit by cars.
  
## Game instructions
Use the arrow up key to move the turtle to the other side of the street without getting hit by a car. Be careful as the cars will be moving faster, each time you level up.

## Usage Example
![20240409190754](https://github.com/ali-kanbar/Turtle-Crossing-Game/assets/155682302/eddf0b7f-ecf1-4911-baaf-05e777257c54)

## Setup Instructions

### Prerequisites

- Python 3.x
- The turtle module

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/tms.git
    cd tms
    ```

2. **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install Flask
    pip install Flask-SQLAlchemy
    pip install Flask-Session
    pip install SQLAlchemy
    pip install python-dotenv
    ```

4. **Set environment variables:**

    On Linux/macOS:

    ```bash
    export SECRET_KEY="8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
    export SQLALCHEMY_DATABASE_URI="sqlite:///Translation_Database.db"
    ```

    On Windows:

    ```powershell
    setx SECRET_KEY "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
    setx SQLALCHEMY_DATABASE_URI "sqlite:///Translation_Database.db"
    ```

5. **Run the application:**

    ```bash
    flask run
    ```

6. **Access the application:**

    Open your web browser and navigate to `http://127.0.0.1:5000`.

## Technologies Used

- **Python**: The core programming language used.
- **Turtle**: A lightweight module that helps us design games in Python.
