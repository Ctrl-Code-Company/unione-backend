# UniWay Backend

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)

## Getting Started

### Prerequisites

Ensure you have the following prerequisites installed on your machine:

- Python (version 3.12)
- Django (version 5.0)
- Docker (version 25.0.3)

### Setup

- Clone the repository:
   ```bash
   git clone git@github.com:CtrlCode-Company/univway-backend.git
   ```

- Open directory in your terminal
   ```bash
   cd univway-backend
   ```

- Create virtual environment
   - Linux/MacOS
   ```bash
   python3 -m venv venv
   ```
   - Windows
   ```bash
   python -m venv venv
   ```

- Activate virtual environment
   - Linux/MacOS
   ```bash
   source venv/bin/activate
   ```
   - Windows
   ```bash
   venv\Scripts\activate
   ```

- Load *local environment variables* to virtual environment:
```
cp ./deployments/development/env_example ./deployments/development/.env
change .env_local variable according to your settings
source ./deployments/development/.env
```


- If *postgresql database* has not be started please start it by following command:
```
docker-compose -f deployments/development/docker-compose.yml up -d
```

- If *development packages* has not been installed please install by running following commit:
```
pip install -r requirements/development.txt
```

- If *migration* has not been applied please apply it first:
```
cd src
python manage.py migrate
```

- Start development server:
```
python manage.py runserver
```

- Finally open your browser: http://127.0.0.1:8000
