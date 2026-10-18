# 🔑 Android Keystore Automation Tool

A lightweight, automated Python CLI tool designed to simplify and speed up Java Keystore (`.jks` / `.keystore`) generation for Android app debugging, signing, and security testing.

---

## 🚀 Features

* **Quick Automation:** Generates keystores using standard `keytool` commands without manual typing errors.
* **Termux & Linux Ready:** Optimized to run seamlessly on Android (via Termux) as well as any Linux terminal.
* **Customizable Parameters:** Easily set validity, alias, key algorithms, and passwords via command-line arguments.
---

## 🛠️ Prerequisites

Before running the tool, make sure you have Python and OpenJDK (`keytool`) installed.

### For Termux (Android):
```bash
pkg update && pkg upgrade -y
pkg install python openjdk-17 -y
```
sudo apt update
sudo apt install python3 default-jdk -y
git clone https://github.com/ayushmanitiwari101-dev/Android-Keystore-Automation.git
cd Android-Keystore-Automation
python generate_keystore.py
---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/ayushmanitiwari101-dev/Android-Keystore-Automation/issues).

---

## 👤 Author

* **Ayush Mani Tiwari**
  * GitHub: [@ayushmanitiwari101-dev](https://github.com/ayushmanitiwari101-dev)
