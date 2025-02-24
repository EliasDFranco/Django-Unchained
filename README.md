# 🚀 Django-Unchained Project - Introduction  

This is an introductory Django project that explores the basic concepts of the framework, including creating models, views, and templates.  

## 🛠️ Technologies Used  

-  **Python**  
-  **Django 4**  
-  **SQLite** (default **database**)  
-  **Git and GitHub** (for version control)  

## 📂 Project Structure  

```plaintext
Django-Unchained/
├── mysite/               # ⚙️ Project configuration
│   ├── __init__.py
│   ├── settings.py       # 🔧 Project settings
│   ├── urls.py           # 🌍 URL configurations
│   └── wsgi.py           # 🚀 WSGI application
├── myapp/                # 🏗️ Django application
│   ├── migrations/       # 📦 Database migrations
│   ├── templates/        # 🎨 HTML templates
│   │   ├── layouts/      # 🏗️ Layout templates
│   │   │   ├── base.html # 🏠 Base template
│   │   ├── projects/     # 📂 Project-related templates
│   │   │   ├── create_project.html  # ➕ Create new project page
│   │   │   ├── projects.html        # 📋 List of projects
│   │   │   ├── details.html         # 🔍 Project details
│   │   ├── tasks/        # ✅ Task-related templates
│   │   │   ├── helloworld.html  # 🌎 Hello World page
│   │   │   ├── index.html       # 🏠 Tasks home page
│   ├── static/           # 🎨 Static files (CSS, images)
│   │   ├── css/          # 💅 CSS stylesheets
│   │   │   ├── main.css  # 🎨 Main CSS file
|   |   ├── folderimage.jpg       # 🖼️ Example image file
│   ├── __init__.py
│   ├── admin.py          # 🛠️ Admin site configurations
│   ├── apps.py           # 🏢 Application configuration
│   ├── models.py         # 🗄️ Data models
│   ├── tests.py          # ✅ Test cases
│   └── views.py          # 👀 Request handlers
├── db.sqlite3            # 🗃️ SQLite database
├── folderimage.jpg       # 🖼️ Example image file
├── manage.py             # 🏗️ Django management script
└── README.md             # 📖 Project documentation
