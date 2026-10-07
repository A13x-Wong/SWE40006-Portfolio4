# SWE40006 Deployment Activity 4 - Docker Container Deployment

This repository contains the source code and Docker configuration files developed for **SWE40006 Software Deployment and Evolution - Deployment Activity 4**.

The activity covers Tasks 4.1 to 4.4 and demonstrates Docker installation, container deployment, Python runtime configuration, web server deployment, deployment to another Docker device, a custom web application, and a non-web-based application.

---

## Task 4.1 - Docker Installation and Hello World

Task 4.1 included:

- Creating a Docker account
- Installing Docker Desktop on Windows
- Configuring WSL 2
- Starting the Docker Engine
- Deploying the official Docker Hello World container

Verification command:

```bash
docker run hello-world
```

Successful execution displayed:

```text
Hello from Docker!
```

---

## Task 4.2 - Python Application

Source folder:

```text
task4.2PythonApp
```

Project structure:

```text
task4.2PythonApp/
├── app.py
└── Dockerfile
```

The Python application was deployed using an official Python runtime inside a Docker container.

Build command:

```bash
docker build -t task4-python-app:v1 .
```

Run command:

```bash
docker run --rm task4-python-app:v1
```

The application was first executed directly on Windows and then inside Docker. The Docker version reported Linux as the operating system, confirming that the application was running inside the Docker container.

Public Docker image:

https://hub.docker.com/r/a13xwong/task4-python-app

---

## Task 4.2 - Hello World Web Server

Source folder:

```text
task4.2HelloWeb
```

Project structure:

```text
task4.2HelloWeb/
├── Dockerfile
└── index.html
```

A custom Hello World web page was deployed using the Nginx Alpine Docker image.

Build command:

```bash
docker build -t task4-hello-web:v1 .
```

Run command:

```bash
docker run -d --name task4-hello-web -p 8080:80 task4-hello-web:v1
```

Local access:

```text
http://localhost:8080
```

Public Docker image:

https://hub.docker.com/r/a13xwong/task4-hello-web

---

## Task 4.2 - Deployment to Another Docker Device

The Python application image was pushed from Docker Desktop on Windows to Docker Hub.

A separate Kali Linux virtual machine was configured with Docker Engine and used as the second Docker device.

The image was pulled using:

```bash
sudo docker pull a13xwong/task4-python-app:v1
```

The application was then executed on the Kali Linux Docker installation:

```bash
sudo docker run --rm a13xwong/task4-python-app:v1
```

The Python application executed successfully on the second Docker device, demonstrating that the same Docker image could be transferred through Docker Hub and deployed on another Docker installation.

---

## Task 4.3 - Personal Expense Tracker Web Application

Source folder:

```text
task4.3WebApp
```

A new web application named **Personal Expense Tracker** was developed for Task 4.3.

The application allows users to:

- Add expenses
- Enter an expense description
- Select an expense category
- Enter an amount
- View expense history
- Automatically calculate total spending
- Delete expenses

Technologies used:

- Python
- Flask
- SQLite
- HTML
- CSS
- Docker

Project structure:

```text
task4.3WebApp/
├── app.py
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── static/
│   └── style.css
└── templates/
    └── index.html
```

Build command:

```bash
docker build -t expense-tracker:v1 .
```

Run command:

```bash
docker run -d --name expense-tracker -p 5001:5000 expense-tracker:v1
```

Local access:

```text
http://localhost:5001
```

The application was successfully tested before and after Docker containerisation.

Public Docker image:

https://hub.docker.com/r/a13xwong/expense-tracker

---

## Task 4.4 - Personal Expense Manager CLI

Source folder:

```text
task4.4CliApp
```

A separate non-web-based application named **Personal Expense Manager CLI** was developed for Task 4.4.

The application operates entirely through the command line and does not require a web browser or web server.

Features include:

- Add expenses
- Select expense categories
- View expense history
- View spending summaries
- Calculate total spending
- Calculate average expense
- Display highest expense
- Display lowest expense
- Delete expenses
- Store expense records using SQLite

Project structure:

```text
task4.4CliApp/
├── Dockerfile
└── expense_manager.py
```

Unlike the Task 4.3 application, the CLI application does not use Flask, HTML, CSS, HTTP, a web server, or an exposed network port.

Build command:

```bash
docker build -t expense-manager-cli:v1 .
```

A Docker volume was created for persistent SQLite storage:

```bash
docker volume create expense-manager-data
```

The application was deployed using:

```bash
docker run -it --rm --name expense-manager-cli -v expense-manager-data:/data expense-manager-cli:v1
```

The CLI was successfully executed entirely through the terminal.

A persistence test was also performed. The original container was removed and a new container was started using the same Docker volume. Previously entered expense records remained available, confirming that persistent Docker storage was working correctly.

Public Docker image:

https://hub.docker.com/r/a13xwong/expense-manager-cli

---

## Public Docker Hub Repositories

All Docker images developed for Deployment Activity 4 are publicly available for verification.

| Task | Docker Hub Repository |
|---|---|
| Task 4.2 Python Application | https://hub.docker.com/r/a13xwong/task4-python-app |
| Task 4.2 Hello World Web Server | https://hub.docker.com/r/a13xwong/task4-hello-web |
| Task 4.3 Personal Expense Tracker | https://hub.docker.com/r/a13xwong/expense-tracker |
| Task 4.4 Personal Expense Manager CLI | https://hub.docker.com/r/a13xwong/expense-manager-cli |

---

## Repository Structure

```text
SWE40006-Portfolio4/
├── task4.2PythonApp/
│   ├── app.py
│   └── Dockerfile
│
├── task4.2HelloWeb/
│   ├── Dockerfile
│   └── index.html
│
├── task4.3WebApp/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── .dockerignore
│   ├── static/
│   │   └── style.css
│   └── templates/
│       └── index.html
│
├── task4.4CliApp/
│   ├── Dockerfile
│   └── expense_manager.py
│
├── .gitignore
└── README.md
```

---

## Deployment Environment

The applications were developed and tested using:

- Windows
- Docker Desktop
- WSL 2
- Visual Studio Code
- Python
- Flask
- SQLite
- Nginx
- Docker Hub
- Oracle VirtualBox
- Kali Linux
- Docker Engine

Docker Desktop on Windows was used as the primary Docker environment.

A separate Kali Linux virtual machine running Docker Engine was used as the second Docker device for Task 4.2.

---

## Deployment Outcome

All required deployment levels from **Task 4.1 to Task 4.4** were completed.

### Task 4.1

- Docker account created
- Docker Desktop installed
- WSL 2 configured
- Docker Hello World deployed

### Task 4.2

- Python application deployed
- Python runtime configured
- Hello World web server deployed
- Docker images published to Docker Hub
- Python application pulled and executed on another Docker device

### Task 4.3

- New Personal Expense Tracker web application developed
- Application containerised using Docker
- Flask and SQLite functionality successfully tested
- Web application successfully deployed inside Docker

### Task 4.4

- New Personal Expense Manager CLI developed
- Non-web-based application successfully containerised
- CLI application successfully deployed inside Docker
- Docker persistent storage successfully tested

The completed activity demonstrates Docker image creation, container deployment, Python runtime configuration, web server deployment, public image distribution through Docker Hub, cross-device deployment, custom web application deployment, non-web application deployment, and persistent Docker storage.