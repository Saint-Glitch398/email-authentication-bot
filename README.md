# email-authentication-bot
This Python script automates sending personalized emails to multiple contacts using Gmail SMTP. It reads contact details from a `.csv` file, personalizes each message using a template, and sends emails with your Curriculum Vitae (CV) attached.

---

## Features

-  Sends bulk emails to multiple recipients
-  Personalizes messages using names from a CSV
-  Attaches your CV automatically
- Uses `.env` for secure credential management
-  Built with plain Python – no external email service required

---

## 📂 Project Structure

```
📁 email-automation-bot/
│
├── email_automation.py      # Core Python script
├── contacts.csv             # List of recipients (name, email)
├── email_template.txt       # Custom email body template
├── Curriculum_Vitae.pdf     # File to attach to every email
├── .env                     # Your credentials (not uploaded to GitHub)
├── .gitignore               # Hides .env and other sensitive files
└── README.md                # You're reading this!