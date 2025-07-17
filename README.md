🧠 AI Social Media # 🤖 AI Social Media Bot

[![Workflow Status](https://github.com/itsabhibhagat/SocialMedia_Post_Scheduler/actions/workflows/post-bot.yml/badge.svg)](https://github.com/itsabhibhagat/SocialMedia_Post_Scheduler/actions)

> Automatically posts your daily GitHub activity (DSA progress, development work, and personal projects) to **LinkedIn**, **Twitter**, and **Telegram** every morning at 6:00 AM IST. Built with Python, OpenAI, GitHub Actions, and APIs.

---

## 📌 Features

- ⏰ Scheduled daily auto-run at 6:00 AM IST via GitHub Actions
- 📊 Fetches GitHub events: push, create, and commit
- 🧠 Summarizes activity using OpenAI
- 🟦 Posts to **LinkedIn**
- 🐦 Posts to **Twitter** (via Pipedream webhook)
- 📲 Sends Telegram notifications for:
  - Post success ✅
  - Skipped (no GitHub activity) 🛌
  - Errors ❌

---

## ⚙️ Tech Stack

| Tool        | Role                        |
|-------------|-----------------------------|
| Python      | Main logic and automation   |
| OpenAI      | Generate engaging summaries |
| GitHub API  | Fetch daily activity        |
| LinkedIn API| Auto-post updates           |
| Twitter API | Post via Pipedream webhook  |
| Telegram Bot| Real-time status alerts     |
| GitHub Actions | Automated daily schedule |

---

## 🗂️ Folder Structure
.
├── .github/
│ └── workflows/
│ └── post-bot.yml
├── github_activity.py
├── generate_post.py
├── linkedin_post.py
├── twitter_post.py
├── notify.py
├── main.py
├── requirements.txt
├── .env # Keep this secret
├── .env.example # Example template
├── log.txt # Daily logs


---

## 🚀 Quick Start

git clone https://github.com/itsabhibhagat/SocialMedia_Post_Scheduler.git
cd SocialMedia_Post_Scheduler

2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

3. Set Up .env
bash
Copy
Edit
cp .env.example .env
# Then edit `.env` and add your secrets
4. Test Locally
bash
Copy
Edit
python main.py


🔐 GitHub Actions Secrets
Go to your repo → Settings → Secrets → Actions → Add:

Secret Name	Description
OPENAI_API_KEY	OpenAI API Key
MY_GITHUB_TOKEN	GitHub Personal Access Token
MY_GITHUB_USERNAME	Your GitHub username
LINKEDIN_ACCESS_TOKEN	LinkedIn Access Token
LINKEDIN_PERSON_URN	Your LinkedIn person URN
TELEGRAM_BOT_TOKEN	Telegram Bot Token
TELEGRAM_CHAT_ID	Your Telegram Chat ID
PIPEDREAM_WEBHOOK_URL	Webhook URL for posting to Twitter


✅ GitHub Actions Automation
No server needed! Fully deployed via GitHub Actions.

Schedule: Runs daily at 6:00 AM IST (30 0 * * * UTC)

Defined in .github/workflows/post-bot.yml

💬 Example Output
yaml
Copy
Edit
✅ Posted successfully:

🚀 GitHub Activity:
• Pushed to Donocare/DonocareNextJs
• Created repo itsabhibhagat/portfolio

#100DaysOfCode #DevLog

📬 Notifications
Status is sent to Telegram after every run:

Success ✅

No activity 🛌

Error ❌


👨‍💻 Author
Abhijeet Kumar Bhagat
🔗 LinkedIn
💻 GitHub
🐦 Twitter
