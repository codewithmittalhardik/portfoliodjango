# 👨‍💻 Hardik's Portfolio

![Project Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

Welcome to the official repository for my personal portfolio website. This project is designed to showcase my skills, professional experience, and the projects I've built as a developer. It serves as a central hub for recruiters, clients, and fellow developers to connect with me.

## 🚀 Live Demo

**Check out the live website here:** [https://hardiksportfolio.onrender.com](https://hardiksportfolio.onrender.com)

---

## 🧐 About

This portfolio provides a comprehensive look into my work and technical background. It features:
* **Hero Section:** A quick introduction to who I am.
* **About Me:** Details about my education, journey, and interests.
* **Skills:** A visual display of the technologies I work with.
* **Projects:** A showcase of my best work with links to source code and live demos.
* **Contact:** A way for visitors to get in touch with me directly.

## 🛠️ Built With

This project relies on the following technologies:

### Frontend
* ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white) **HTML5** - For structure and semantic markup.
* ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white) **CSS3** - For styling and responsive layout.
* ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) **JavaScript** - For interactivity and dynamic content.
* ### Backend
* ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) **Python** - Programming Language
* ![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white) **Django** - Backend Framework
* ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white) **SQLite** - Database
* ![Render](https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=white) **Render** - Deployment Platform
* ### Tools & Deployment
* ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) **Git** - Version control.
* ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white) **GitHub Pages** - Hosting and deployment.

## 🎨 Features

* **Responsive Design:** Fully optimized for desktop, tablet, and mobile devices.
* **Interactive UI:** Smooth scrolling, hover effects, and animations.
* **Clean Codebase:** Well-structured HTML and CSS for easy maintenance.
* **Contact Form:** Integrated for easy communication.

## 💻 Getting Started

To view or modify this project locally, follow these steps:

1.  **Clone the repository**
    ```bash
    git clone https://github.com/codewithmittalhardik/hardikportfolio.git
    ```

2.  **Navigate to the project directory**
    ```bash
    cd hardikportfolio
    ```

3.  **Install dependency**
    ```bash
    pip install -r requirement.txt
    ```
4.  ** Copy & Paste in your Terminal to run**
    ```bash
    python3 manage.py runserver
    ```

## 📂 Project Structure

```text
hardikportfolio/
├── manage.py            # Django command-line utility
├── requirement.txt      # List of dependencies
├── db.sqlite3           # Database file
├── portfoliodjango/     # Project Configuration
│   ├── asgi.py
│   ├── settings.py      # Main settings (DB, Apps, Middleware)
│   ├── urls.py          # Project-level URL routing
│   └── wsgi.py
├── protfolio/           # Main Application (App Logic)
│   ├── admin.py         # Admin panel configuration
│   ├── forms.py         # Form handling
│   ├── models.py        # Database models
│   ├── urls.py          # App-level URL routing
│   └── views.py         # View logic (Render templates)
├── static/              # Static files (CSS, JS, Images)
│   ├── css/
│   ├── images/
│   └── js/
└── template/            # HTML Templates
    └── index.html       # Main landing page
```
