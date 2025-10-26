# Omnisaver

**Cyberican's Automation for Decentralized Backup Core**

> *"Save everything. Lose nothing. Automate like a machine."*

---

## 🔥 Overview

**Omnisaver** is a **modular automation utility** designed by **Cyberican** for DevOps engineers who live in a world of **pipelines, processes, and persistence**.

It’s engineered to:

* 📦 **Collect**: source files, configs, or datasets from arbitrary locations
* 📊 **Analyze**: analyze the data, categorize and save to data management system
* 🧩 **Transform**: prepare & validate environments (Python, Git, system checks)
* 🚀 **Run**: controlled initializers and task pipelines inside managed environments

---

## 🛠 Features

* **Dynamic Agents**: configure the Jenkins agent label at runtime
* **Virtual Environments**: ephemeral or persistent Python venv bootstrap
* **Initial Checks**: system probes (`git`, `python3`, `pip`, `df -h`) for baseline health
* **Workspace Discipline**: automated cleanups with `cleanWs()` integration
* **Process Initialization**: kickstart complex workflows with `initializer.py`
* **Environment Aware**: parametric `SOURCE_DIR`, `DESTINATION_DIR`, and `AGENT_LABEL`

---

## ⚙️ Tech Stack

* **Python 3.10+** — core scripts & operations
* **Jenkins** — pipeline orchestration & CI/CD
* **Linux Shell** — brutalist, direct command execution

---

## 🚦 Quickstart

### 🔽 Clone the Repo

```bash
git clone https://github.com/Cyberican/Omnisaver.git
cd Omnisaver
```

### 🐍 Setup Environment



#### Legacy method of installing and activating Virtual Environment
```bash
# Create and activate a uv-managed virtual environment
python3 -m venv venv
. venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```

#### Using [UV](https://docs.astral.sh/uv) to install and activate Virtual Environment
```bash
# Create and activate a uv-managed virtual environment
uv venv venv
source venv/bin/activate

# Install dependencies (automatically upgrades pip-equivalent internals)
uv pip install -r requirements.txt
```

### ▶️ Run Initializer via CLI

```bash
python initializer.py
```

---

## 📂 Project Structure

```
Omnisaver/
├─ operations/       # Core task modules
├─ utils/            # Utility helpers (logging, config, env mgmt)
├─ initializer.py    # Entry point for process runs
├─ requirements.txt  # Dependencies
├─ Jenkinsfile       # CI/CD definition
└─ README.md         # You are here
```

---

## 🧱 Design Philosophy

> Minimalism in software = **clarity > convenience**.

* **Minimal abstractions**: you see the commands, you know what runs.
* **Futuristic resilience**: designed for constrained or edge devices (RPi, low-power agents).
* **Automation as armor**: every run ensures the system is ready, clean, and aligned.

---

## 🔒 Security Notes

* Always run Omnisaver in **controlled environments**; it executes direct shell commands.
* Validate `requirements.txt` and sources before use in production.

---

## 🧑‍💻 Contributing

We welcome contributions from DevOps professionals, automation junkies, and cyberpunks alike! :-)

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/neon-ops`)
3. Commit brutalist code (`git commit -m 'Add raw system probe'`)
4. Push and open a PR

---

## 📜 [License](https://github.com/Cyberican/Omnisaver/blob/main/LICENSE)

This project is licensed under the **Unlicense**

---

## 🌐 Cyberican Signal

Cyberican is building the **future for saving data using Machine Learning and AI + automation networks**.
