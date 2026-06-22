# 🛡️ File Integrity Monitor (FIM)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📖 Overview

File Integrity Monitor (FIM) is a Python-based cybersecurity tool that detects unauthorized file modifications using SHA-256 hashing.

The tool creates a baseline of file hashes and continuously compares them against current files to identify:

- File Modifications
- File Deletions
- File Integrity Violations
- Unauthorized Changes

This project is designed for cybersecurity learning, digital forensics, and system integrity monitoring.

---

## 🚀 Features

✅ SHA-256 File Hashing

✅ Baseline Creation

✅ Integrity Verification

✅ Detect Modified Files

✅ Detect Deleted Files

✅ JSON Baseline Storage

✅ Lightweight & Fast

✅ Cross Platform Support

---

## ⚙️ Installation

```bash
git clone https://github.com/adityainfosec/File-Integrity-Monitor.git

cd File-Integrity-Monitor

python3 file_integrity_monitor.py
```

---

## 🖥 Usage

### Create Baseline

```bash
python3 file_integrity_monitor.py
```

Select:

```text
1
```

Enter folder path:

```text
/home/user/test
```

Baseline file will be created:

```text
baseline.json
```

---

### Verify Integrity

Run again:

```bash
python3 file_integrity_monitor.py
```

Select:

```text
2
```

The tool compares current files against stored hashes.

Example Output:

```text
[OK] file1.txt

[!] Modified: config.txt

[!] Deleted: database.db
```

---

## 🔐 How It Works

1. Scan selected directory
2. Generate SHA-256 hash for each file
3. Store hashes inside baseline.json
4. Recalculate hashes during verification
5. Compare old and new hashes
6. Report changes instantly

---

## 🛠 Technologies Used

- Python 3
- hashlib
- json
- os module

---

## 🌐 Cybersecurity Applications

- File Integrity Monitoring (FIM)
- Digital Forensics
- SOC Operations
- Incident Response
- Malware Detection
- Security Auditing
- Blue Team Operations

---

## ⚠️ Disclaimer

This project is intended for educational and authorized security monitoring purposes only.

Users are responsible for complying with applicable laws and regulations.

---

## 👨‍💻 Author

Aditya

Cybersecurity Enthusiast

GitHub:
https://github.com/adityainfosec
