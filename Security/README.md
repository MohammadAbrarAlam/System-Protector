# SecureSys – IT Security Monitoring System

## Overview

SecureSys is a web-based IT Security Monitoring System developed using Python, Django, Django REST Framework, Bootstrap, and Python security modules. This system helps IT administrators monitor system performance, track patch updates, check firewall status, and manage security operations through a web dashboard and REST API.

This project is designed for IT Support Engineers, System Administrators, and Security Analysts to monitor and manage system security efficiently.

---

## Features

### 1. System Monitoring

* Monitor CPU usage
* Monitor RAM usage
* Monitor disk usage
* View running processes
* Real-time system status dashboard

### 2. Firewall Monitoring

* Check firewall status
* Display firewall configuration
* Identify security protection status

### 3. Patch Management

* Add new patch updates
* Track patch installation status
* View patch history
* Status indicators: Installed, Pending, Failed

### 4. Security Features

* Data encryption using cryptography module
* Secure API endpoints
* Role-ready security architecture
* Password protection ready structure

### 5. REST API Support

Provides REST API endpoints for:

* System status
* Process monitoring
* Firewall status
* Patch management
* Encryption

### 6. Professional Dashboard

* Bootstrap UI
* Carousel for security overview
* Cards for feature navigation
* Tables for data display

---

## Technologies Used

### Backend

* Python 3
* Django
* Django REST Framework

### Frontend

* HTML
* Bootstrap 5
* CSS

### Security Modules

* psutil – system monitoring
* cryptography – encryption
* os – firewall status

### Database

* SQLite (default)
* MySQL (optional)

---

## Project Structure

```
Protector/
│
├── Protector/
│    ├── settings.py
│    ├── urls.py
│
├── security/
│    ├── migrations/
│    ├── templates/
│    │    └── security/
│    │         ├── base.html
│    │         ├── dashboard.html
│    │         ├── system_status.html
│    │         ├── processes.html
│    │         ├── firewall.html
│    │         ├── patches.html
│    │
│    ├── models.py
│    ├── views.py
│    ├── urls.py
│    ├── serializers.py
│    ├── monitoring.py
│    ├── firewall.py
│    ├── encryption.py
│
├── manage.py
└── README.md
```

---

## Installation Guide

### Step 1: Clone project

```
git clone https://github.com/yourusername/securesys.git
cd securesys
```

### Step 2: Install dependencies

```
pip install django djangorestframework psutil cryptography
```

### Step 3: Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Run server

```
python manage.py runserver
```

### Step 5: Open browser

```
http://127.0.0.1:8000/
```

---

## API Endpoints

| Endpoint            | Method | Description              |
| ------------------- | ------ | ------------------------ |
| /api/system-status/ | GET    | Get CPU, RAM, Disk usage |
| /api/processes/     | GET    | Get running processes    |
| /api/firewall/      | GET    | Get firewall status      |
| /api/patches/       | GET    | Get patch list           |
| /api/add-patch/     | POST   | Add new patch            |
| /api/encrypt/       | POST   | Encrypt data             |

---

## Dashboard Pages

| Page          | URL             |
| ------------- | --------------- |
| Dashboard     | /               |
| System Status | /system-status/ |
| Processes     | /processes/     |
| Firewall      | /firewall/      |
| Patches       | /patches/       |

---

## Example Use Case

An IT administrator can:

* Monitor system performance
* Track security updates
* Verify firewall status
* Detect system issues
* Manage patch updates

---

## Security Modules Used

### psutil

Used for monitoring system performance

### cryptography

Used for encrypting sensitive data

### os

Used for firewall status detection

---

## Future Enhancements

* User authentication system
* Role-based access control
* Threat detection system
* Email alert system
* Real-time monitoring using AJAX
* Security logs

---

## Resume Description

Developed a SecureSys IT Security Monitoring System using Python, Django, REST API, and Bootstrap to monitor system performance, manage patch updates, and track firewall status. Implemented system monitoring, encryption, and patch management features for improved IT security.

---

## Author

Abrar Alam
Python Developer | IT Security Enthusiast

---

## License

This project is for educational and learning purposes.

---

## Conclusion

SecureSys provides a strong foundation for IT security monitoring and demonstrates practical skills in Python, Django, REST APIs, and cybersecurity concepts suitable for IT Support and Security roles.
