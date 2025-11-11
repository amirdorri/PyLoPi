# PyLoPi Quick Start Guide

Get up and running with PyLoPi in 5 minutes! ⚡

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- A modern web browser

## Installation

### Option 1: Quick Install (Recommended)

**Linux/Mac:**
```bash
git clone https://github.com/PicoBaz/PyLoPi.git
cd PyLoPi
chmod +x run.sh
./run.sh
```

**Windows:**
```cmd
git clone https://github.com/PicoBaz/PyLoPi.git
cd PyLoPi
run.bat
```

### Option 2: Manual Install

```bash
git clone https://github.com/PicoBaz/PyLoPi.git
cd PyLoPi
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Option 3: Docker

```bash
git clone https://github.com/PicoBaz/PyLoPi.git
cd PyLoPi
docker-compose up -d
```

## First Steps

### 1. Access the Dashboard

Open your browser and go to:
```
http://localhost:5000
```

### 2. Add Log Files

1. Look for the "Start Monitoring" section
2. Enter the path to your log file (e.g., `/var/log/app.log`)
3. Click "Add Log Path"
4. Add more paths if needed

### 3. Start Monitoring

Click the "Start Monitoring" button. PyLoPi will begin analyzing your logs in real-time!

## Test It Out

Want to see PyLoPi in action without real logs? Generate test data:

```bash
python test_log_generator.py test.log 20 2
```

This creates a test log file with 20 sample errors (2 seconds apart).

Then add `test.log` to PyLoPi and watch it analyze!

## Common Use Cases

### Monitor a Python Application

```python
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    result = 10 / 0
except Exception as e:
    logging.error(f"Error occurred: {e}")
```

Add `app.log` to PyLoPi to monitor this application.

### Monitor Web Server Logs

**Apache:**
```bash
ErrorLog /var/log/apache2/error.log
```

**Nginx:**
```bash
error_log /var/log/nginx/error.log;
```

Add these paths to PyLoPi.

### Monitor Multiple Applications

```bash
/var/log/app1/error.log
/var/log/app2/error.log
/home/user/project/debug.log
```

Add all paths you want to monitor!

## Configure Email Notifications

1. Click "Settings" tab
2. Enable "Email Notifications"
3. Enter your email address
4. Configure SMTP settings:
   - Server: `smtp.gmail.com`
   - Port: `587`
   - Username: Your Gmail address
   - Password: Your Gmail app password
5. Click "Save Settings"

### Gmail Setup

For Gmail, you need to:
1. Enable 2-factor authentication
2. Generate an app password: https://myaccount.google.com/apppasswords
3. Use the app password in PyLoPi settings

## Filter Error Types

Only want specific errors? Configure filters:

1. Go to Settings
2. Scroll to "Enabled Error Types"
3. Check only the errors you want to monitor
4. Click "Save Settings"

Example: Monitor only SyntaxError and TypeError

## View Analysis

When an error is detected:

1. It appears on the Dashboard
2. Click "View Details" for full analysis
3. See:
   - Error explanation
   - Suggested solutions
   - Code fixes (when applicable)
   - Full log context

## Tips & Tricks

### 🎯 Monitor Only Critical Errors

Uncheck low-priority error types in Settings

### 📧 Set Up Email Alerts

Configure email notifications for instant alerts

### 🌍 Change Language

Use the EN/FA buttons in the header

### 🔄 Auto-Refresh

Dashboard updates every 5 seconds automatically

### 📊 View Statistics

Check the dashboard for:
- Total logs count
- Today's errors
- Critical error count
- Top error types

## Troubleshooting

### Port 5000 Already in Use?

Edit `app.py` and change the port:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Logs Not Appearing?

1. Check file path is correct
2. Verify file permissions
3. Ensure file exists
4. Try absolute path instead of relative

### Email Not Working?

1. Check SMTP settings
2. Verify Gmail app password
3. Check spam folder
4. Try port 465 instead of 587

### Database Error?

Delete `pylopi.db` and restart:
```bash
rm pylopi.db
python app.py
```

## Next Steps

- 📖 Read the [full documentation](README.md)
- 🔧 Explore [configuration options](README.md#configuration)
- 🤝 [Contribute](CONTRIBUTING.md) to the project
- ⭐ Star the repository on GitHub

## Need Help?

- 💬 Ask questions: [Telegram](https://t.me/picobaz)
- 📧 Email: picobaz3@gmail.com

---

**Ready to dive deeper?** Check out the [complete documentation](README.md)!

Happy monitoring! 🚀