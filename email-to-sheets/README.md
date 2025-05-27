### Email to Google Sheet

This script fetches unread emails from Gmail and appends sender & subject to a Google Sheet.

---

#### 🔧 Requirements
- Python 3
- `imaplib`, `email`, `gspread`, `oauth2client`
- Gmail IMAP access
- Google Service Account JSON

---

#### ▶️ How to Run

1. Enable Gmail IMAP in settings  
2. Create a Google Sheet named `Email Log`  
3. Get your Google API JSON key  
4. Run the script:
```bash
python email_to_sheets.py
