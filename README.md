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
- Python installed on your system  
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
   - `chat:write` (for sending messages)

If you're sending messages to a **private** channel, also add:
   - `groups:read` (to read channel metadata)

4. Install the app to your workspace to generate a **Bot User OAuth Token**.

---

### ✅ Step 5: Invite App to Channel

- Go to your Slack channel.
- Run the command:  
/invite @your_app_name



This ensures the bot has access to the channel.

---

### ✅ Step 6: Update Python Script

In your `messagebot.py` file:

```python
token = "your-slack-bot-token"
url = "https://slack.com/api/chat.postMessage"
channel = "your-channel-id"
Replace your-slack-bot-token with the token from Step 4.

Replace your-channel-id with the actual channel ID.
You can find it by opening the Slack channel and checking the URL.

✅ Sample Python Code
Here’s a simple Python example:


import requests

token = "xoxb-your-token-here"
url = "https://slack.com/api/chat.postMessage"
channel = "CXXXXXXXX"  # replace with actual channel ID

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
🏁 Final Note
Once you've completed the above steps, run your script:


python messagebot.py
Your message will appear in the selected Slack channel! 🎉

📚 Resources
Slack API Docs

Slack Python SDK

