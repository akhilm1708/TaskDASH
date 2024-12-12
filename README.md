# TaskDASH

todolist_app/
│
├── main.py           # Main entry point to run the app
├── calendar_api.py   # Handles Google Calendar API interactions
├── task_manager.py   # Manages task CRUD (Create, Read, Update, Delete) operations
└── ui.py             # Contains the Tkinter UI code and layout


# 📝 **To-Do List App with Google Calendar Integration**

## 🚀 **Project Overview**

As a student myself, I often struggle with organizing tasks based on priority, and this has led to panic moments just before assignments are due. To help with this issue, I’ve built a **To-Do List App** that allows users to:

- **Add, delete, and prioritize tasks**
- **Sort tasks by priority**
- **Get reminders for tasks by integrating with Google Calendar**

This app is built using **Python** with the **Tkinter** library for the user interface, and it integrates with the **Google Calendar API** to remind you of upcoming tasks based on the due date.

## ✨ **Features**

- **Add Tasks**: Create tasks with a title, priority (1 = High, 3 = Low), and a due date.
- **Delete Tasks**: Remove tasks you no longer need.
- **Task Sorting**: Sort tasks by priority, so you focus on the most important ones first.
- **Google Calendar Integration**: Sync your tasks to Google Calendar with reminders based on the due date.

## 🛠️ **Technologies Used**

- **Python**: Programming language
- **Tkinter**: GUI framework for the user interface
- **Google Calendar API**: To integrate task reminders
- **datetime**: For managing task due dates

## 🎯 **How It Works**

1. **Google Calendar API**: The app uses the Google Calendar API to authenticate the user and add tasks as calendar events. Reminders are set based on the due date.
2. **User Interface**: The UI is built with Tkinter, where users can enter tasks, set priorities, and assign due dates. Tasks are displayed in a sorted list based on their priority.
3. **Task Management**: Tasks can be added, deleted, and saved locally using `pickle`.

---

## 💻 **Getting Started**

### Prerequisites

To run this project locally, you’ll need:

1. **Python 3.x**: Download from [python.org](https://www.python.org/downloads/)
2. **Google API client**: Install with the following command:
   ```bash
   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
3 **Running on the Command Line**: python main.py

