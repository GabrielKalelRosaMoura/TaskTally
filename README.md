<div align="center">

# TaskTally

A simple web app for tracking the amount of focused time spent on a task.

Enter your minutes, confirm the entry, and watch your total grow.

<img width="969" height="647" alt="Screenshot 2026-05-24 at 19 25 22" src="https://github.com/user-attachments/assets/7b96cefe-c492-4ef9-a352-1936e941b28a" />

</div>

<br>

# **What is it?**

TaskTally was built from a simple need: tracking how many minutes I spend focused on a single task.

I wanted a tool that could quickly record my focused time without unnecessary features. Most apps I found included additional and unnecessary functionality that made it more complicated than it needed to be.

With TaskTally I wanted the experience intentionally minimal.

You enter the number of minutes spent on a task, confirm it, and the app adds that value to a running total. There are no accounts, no setup process, and no distractions — just a clear total of your focused time.

<br>

# **Tech Stack**

| Backend | Frontend | Data Flow |
|---|---|---|
| Python, Flask | HTML, CSS, JavaScript | Fetch API, JSON |

<br>

## How does it work?

TaskTally runs on a small Flask server with two main routes:

| Route | Method | Description |
|---|---|---|
| `/` | `GET` | Serves the main page and displays the current total |
| `/add` | `POST` | Receives the entered minutes, adds them to the total, and returns the updated value as JSON |

When the user clicks **Confirm**, JavaScript sends the entered number to the `/add` route using `fetch`.

The server updates the running total and returns the new value as JSON. The frontend then updates only the displayed total, without reloading the entire page.

The total is currently stored in server memory, keeping the project simple and lightweight.

<br>

## Run it locally
### -> Requirements

- Python 3
- Flask

### -> Installation

```bash
# 1. Clone the repository
git clone [https://github.com/GabrielKalelRosaMoura/TaskTally.git]
cd tasktally

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install flask

# 4. Run the application
python app.py
