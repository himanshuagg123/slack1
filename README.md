# Slack Message Bot using Python

This project demonstrates how to send a message to a Slack channel using a Python script and Slack API.

---

## 💡 Why I Built This Bot

I developed this bot for my **team lead** to automatically notify the team whenever an error occurs in our system.  
It helps in the following ways:

- 🚨 Alerts the team instantly before someone manually reports the issue.
- ⏱️ Saves valuable debugging time.
- ⚙️ Automates error monitoring and improves team response.

This proactive system ensures that errors are identified and acknowledged in real-time, helping our team stay efficient and responsive.

---

## 📌 Prerequisites

- A Slack account  
- Python installed  
- Docker installed  
- Access to create Slack apps via [Slack API](https://api.slack.com)

---

## 🚀 Steps to Get Started

### ✅ Step 1: Create a Slack Account

Sign up at: [https://slack.com/intl/en-in](https://slack.com/intl/en-in)

---

### ✅ Step 2: Set Up a Workspace & Channel

- Create a Slack workspace.
- Create a **channel** (either public or private) within that workspace.

---

### ✅ Step 3: Create a Slack App

- Visit [Slack API](https://api.slack.com)
- Click on **Your Apps**.
- Click **Create New App**.
- Enter your app name and select your workspace.

---

### ✅ Step 4: Add Permissions

1. Go to **OAuth & Permissions**.
2. Scroll to **Scopes**.
3. Under **Bot Token Scopes**, add:
   - `chat:write`

   For **private** channels, also add:
   - `groups:read`

4. Install the app to your workspace to generate a **Bot User OAuth Token**.

---

### ✅ Step 5: Invite App to Channel

In the Slack channel, run:


/invite @your_app_name
✅ Step 6: Update messagebot.py
Update this file:


token = "your-slack-bot-token"
url = "https://slack.com/api/chat.postMessage"
channel = "your-channel-id"
🐳 Using Docker
✅ Step 7: Create a Dockerfile
Dockerfile
Copy
Edit
# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY messagebot.py .

CMD ["python", "messagebot.py"]
✅ Step 8: Create requirements.txt

requests
✅ Step 9: Build and Run with Docker
Build the Docker image:


docker build -t slack-bot .
Run the container:


docker run slack-bot
You should see the output in your terminal and the message appear in Slack.

✅ Sample Python Code (Recap)
python

import requests

token = "xoxb-your-token-here"
url = "https://slack.com/api/chat.postMessage"
channel = "CXXXXXXXX"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

data = {
    "channel": channel,
    "text": "Hello from your Python script!"
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
📚 Resources
Slack API Docs

Slack Python SDK

Docker Official Docs

Built with ❤️ to make our team's workflow smoother and faster ⚡
