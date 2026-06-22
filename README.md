# 🛡️ File Integrity Monitor (FIM)

A lightweight Python-based File Integrity Monitoring tool using SHA-256 hashing and SQLite.

This tool helps detect unauthorized file changes in a directory by creating a baseline and comparing it later.

---

## 📌 Features

- SHA-256 file hashing
- Baseline creation of directories
- Integrity checking
- Detects:
  - Modified files
  - Deleted files
  - New files
- SQLite-based storage
- CLI tool for Linux (Kali compatible)

---

## ⚙️ Installation

```bash
git clone https://github.com/adityainfosec/File-Integrity-Monitor.git
cd File-Integrity-Monitor
pip install -r requirements.txt
---

## 🚀 Usage

### Create Baseline
```bash
python3 fim.py baseline test_lab
```

Check Integrity
```bash
python3 fim.py check test_lab
```

🧪 Example Lab Setup

```bash
mkdir test_lab

echo "file one content" > test_lab/a.txt
echo "file two content" > test_lab/b.txt
echo "config data" > test_lab/c.txt
```

Create baseline
```bash
python3 fim.py baseline test_lab
```

Modify files
```bash
echo "HACKED DATA" >> test_lab/a.txt
rm test_lab/b.txt
echo "new file created" > test_lab/d.txt
```

Run check
```bash
python3 fim.py check test_lab
```

📊 Example Output

```
INTEGRITY REPORT
==================================================
[!] Modified Files:
 - a.txt

[!] Deleted Files:
 - b.txt

[!] New Files:
 + d.txt
```

🧠 How It Works

- Scans directory recursively  
- Generates SHA-256 hash for each file  
- Stores hashes in SQLite database  
- Compares baseline vs current state  
- Shows file changes  

⚠️ Disclaimer

This tool is for educational and authorized security testing only.  
Do not use it on systems without permission.

👨‍💻 Author

Aditya  
Cybersecurity Enthusiast | Ethical Hacking | Blue Team Tools
