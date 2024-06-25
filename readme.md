# Mouse Tracker and Image Capture

## Setup

Follow these steps to get your development environment set up:

### 1. Clone the Repository

```bash
git clone https://github.com/Avii1099/mouse_tracking.git
cd mouse_tracking
```

### 2. Create a Virtual Environment

Run the following command in the root of your project directory:

```bash
python3 -m venv venv
```

This creates a virtual environment named `venv` in your project directory.

### 3. Activate the Virtual Environment

For Windows:
```bash
venv\Scripts\activate
```

For MacOS/Linux:
```bash
source venv/bin/activate
```

### 4. Install Requirements

With the virtual environment activated, install the project dependencies:

```bash
pip install -r requirements.txt
```

### 5. Set Device Permissions (Linux Only)

This project requires specific device permissions to function properly on Linux. Run the following command with superuser privileges:

```bash
sudo chmod 0666 /dev/input/event*
```

**Warning:** This command allows all users read and write access to all input event devices, which can pose significant security risks. Ensure you understand the implications of this change before proceeding.

## Running the Application

Describe how to run your application. Include any necessary commands.

```bash
python manage.py runserver
```


