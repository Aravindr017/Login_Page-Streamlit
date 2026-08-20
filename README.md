# Streamlit Login Application

A simple and professional **Streamlit login application** demonstrating basic authentication, session state management, and logout functionality.

## Features

- Username and password authentication
- Session-based login state using `st.session_state`
- Automatic page refresh after login/logout
- Logout functionality
- Simple and clean user interface

## Demo Credentials

| Field | Value |
|---|---|
| **Username** | `admin` |
| **Password** | `admin123` |

> ⚠️ **Note:** The credentials are hard-coded for demonstration purposes only and should **not** be used in a production application.

## Tech Stack

- **Python**
- **Streamlit**

## Getting Started

### Clone the Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### Install Dependencies

```bash
pip install streamlit
```


### Run the Application

```bash
streamlit run app.py
```

### Application Flow

```bash
Login Page
    │
    ├── Valid Credentials ──► Welcome Page
    │                              │
    │                              └── Logout ──► Login Page
    │
    └── Invalid Credentials ─► Error Message
```

### Project Structure

```bash
project/
│
├── app.py
└── README.md
```

##  Purpose

This project is intended as a beginner-friendly example of implementing login authentication and session management in Streamlit.
