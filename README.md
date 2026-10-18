# Android Keystore Generator & Security Lab Tool

A lightweight Python utility to automate the generation of self-signed Java Keystores (`.jks`) for Android application debugging, reverse engineering labs, and local security testing environments.

## Features
- Automates `keytool` commands for quick cryptographic key generation.
- Configurable keystore parameters (alias, validity, filename).
- Designed for secure local testing and educational research.

## Prerequisites
- Termux (Android) or Linux environment with OpenJDK installed (`pkg install openjdk-17`).
- Python 3.x

## Usage
Run the script in your terminal:
```bash
python generate_keystore.py

