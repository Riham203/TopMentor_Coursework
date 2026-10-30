# Python Email Automation with File Attachments

## Project Overview

This project is a Python-based email automation tool that allows users to send emails through Gmail using Python's built-in email and SMTP libraries.

Users can enter the recipient's email address, specify the subject, write a multi-line email message, and attach multiple files before sending the email.

The project uses Gmail's SMTP server with SSL authentication to send emails securely.

## Features

- **Dynamic Recipient Input:** Enter the recipient's email address at runtime.
- **Custom Subject:** Specify the email subject.
- **Multi-line Email Content:** Write email content directly in the terminal.
- **Multiple File Attachments:** Attach multiple files using their file paths.
- **Automatic MIME Type Detection:** Identifies attachment types using Python's `mimetypes` module.
- **Secure Authentication:** Uses Gmail SMTP over SSL.
- **Environment Variables:** Stores the Gmail app password outside the source code.

## Tools & Technologies

- **Python** – Programming language
- **smtplib** – Sending emails through an SMTP server
- **email.message** – Creating email messages and attachments
- **mimetypes** – Detecting file MIME types
- **python-dotenv** – Loading environment variables
- **Gmail SMTP** – Email delivery service

## Project Structure

```text
Send_Email/
│
├── Send_email.ipynb
├── .env
├── .gitignore
└── README.md
```

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Riham203/TopMentor_Coursework.git
```

### 2. Navigate to the Project Folder

```bash
cd TopMentor_Coursework/projects/Send_Email
```

Adjust the folder name if your actual GitHub project folder uses a different name.

### 3. Install Dependencies

```bash
pip install python-dotenv
```

The other libraries used in the notebook are part of Python's standard library.

### 4. Configure Gmail App Password

1. Enable 2-Step Verification on your Google account.
2. Generate a Google App Password.
3. Create a `.env` file in the project directory.
4. Add the following:

```env
app_pass=your_gmail_app_password
```

Do not share or upload your actual app password.

## How to Run

1. Open `Send_email.ipynb` in Jupyter Notebook or VS Code.
2. Make sure the `.env` file is configured.
3. Run the notebook cell.
4. Enter the recipient's email address.
5. Enter the email subject.
6. Type your email content. Press Enter on an empty line to finish.
7. Enter file paths for attachments. Press Enter on an empty line when finished.
8. The program connects to Gmail and sends the email.

## Concepts Practiced

- Python environment variables.
- Working with SMTP servers.
- Email composition using `EmailMessage`.
- Reading files in binary mode.
- MIME types and email attachments.
- Exception handling.
- Automating email communication.

## Security Notes

- Never hardcode or upload Gmail app passwords.
- Add `.env` to `.gitignore`.
- Use a Gmail App Password rather than your regular Gmail password.
- Be careful when sending emails or attachments to external recipients.

## Author

**Riham**

GitHub: [Riham](https://github.com/Riham203)
