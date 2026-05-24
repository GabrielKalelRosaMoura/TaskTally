TaskTally
A dead-simple web app for tracking the total minutes you've spent focused on a task. Enter your minutes, hit confirm, and watch your running total grow.

The Story
I was deep in a study session and wanted a way to track how much focused time I was putting into a single task. So I did what anyone would do — I went looking for an app or website to do it for me.
What I found was the opposite of what I wanted. Every option was bloated: accounts to create, dashboards I didn't need, timers and tags and reports and notifications, all to answer one tiny question — how many minutes have I actually spent on this?
None of them did the one simple thing I was after, without making me wade through ten features I'd never touch.
So I built it myself. TaskTally does exactly one thing and nothing else: you type in the minutes, you confirm, and it keeps a running total. No accounts, no clutter, no setup. The whole point is that it stays out of your way.

Features

A single input for adding minutes
A confirm button (or just press Enter)
A live running total that updates instantly, without reloading the page

That's it — and that's intentional.

Tech Stack

Python — application logic
Flask — lightweight web framework handling the routes and requests
HTML / CSS / JavaScript — the frontend, with a fetch call that updates the total without a page refresh

Flask was chosen deliberately over a heavier framework like Django. For a project this focused, a micro-framework provides exactly what's needed — URL routing and request handling — without the overhead of features the project would never use. Matching the tool to the size of the problem was part of the point.

How It Works
The app runs on a small Flask server with two routes:

GET / serves the main page with the current total.
POST /add receives the entered minutes, adds them to the running total, and returns the new value as JSON.

When you click Confirm, a bit of JavaScript sends your number to /add in the background, receives the updated total, and updates just that number on screen — so the page never fully reloads.
The total is currently held in memory on the server, which keeps the app simple. The natural next step would be to persist it to a file or a database so it survives restarts.

Running It Locally
You'll need Python 3 installed.
bash# 1. Clone the repository
git clone https://github.com/YOUR-USERNAME/tasktally.git
cd tasktally

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install flask

# 4. Run the app
python app.py
Then open http://127.0.0.1:5000 in your browser.
To stop the server, press Ctrl + C in the terminal.

Future Improvements

Persist the total to a database (e.g. SQLite) so it survives restarts
Support multiple named tasks, each with its own total
A reset button
Deploy it publicly with a production server (Gunicorn) on a host like Render or Railway

