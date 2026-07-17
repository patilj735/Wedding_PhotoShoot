# 💍 Wedding Photoshoot

> A visually engaging wedding photography web application built with Python and designed to showcase memorable wedding moments through a beautiful digital experience.

---

## ✨ Features

* Elegant wedding photography presentation
* Image-based visual experience
* Responsive web interface
* Python-powered backend
* Organized wedding image gallery
* Automated project validation using GitHub Actions

---

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **HTML5**
* **CSS3**
* **Git & GitHub**
* **GitHub Actions**

---

## 📁 Project Structure

```text
Wedding-Photoshoot/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── images/
│   └── wedding photos
│
├── index.html
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ GitHub Actions

GitHub Actions is configured to automatically validate the project whenever changes are pushed to the repository.

### Workflow

```text
Code Changes
     │
     ▼
Git Commit & Push
     │
     ▼
GitHub Actions
     │
     ├── Checkout Repository
     │
     ├── Setup Python
     │
     ├── Install Dependencies
     │
     └── Validate Application
```

### CI Workflow

The workflow:

* Runs on every push to the `main` branch
* Runs on pull requests targeting `main`
* Sets up the Python environment
* Installs dependencies from `requirements.txt`
* Verifies that the application can be imported successfully

---

## 🎯 Project Objective

The objective of this project is to create a visually appealing wedding photography application while demonstrating Python web development, project organization, Git version control, and automated validation using GitHub Actions.

---

## 👨‍💻 Author

**Janhavi Patil**
