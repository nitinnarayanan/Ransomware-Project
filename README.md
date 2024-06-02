# Ransomware-Project

# Project: File Encryption, Detection, and Mitigation System

## Overview

This project consists of a series of Python scripts designed to handle file encryption, detection of potentially malicious files, mitigation actions, file decryption, and file system monitoring. The project includes the following scripts:

1. `attack.py`
2. `detection.py`
3. `mitigation.py`
4. `watchdog_observer.py`
5. `textfiles_generation.py`
6. `decrypt.py`

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup and Installation](#setup-and-installation)
3. [Usage](#usage)
    - [Generating Text Files](#generating-text-files)
    - [Encrypting Text Files](#encrypting-text-files)
    - [Detecting Malicious Files](#detecting-malicious-files)
    - [Mitigating Detected Threats](#mitigating-detected-threats)
    - [Decrypting Text Files](#decrypting-text-files)
    - [Monitoring File System Changes](#monitoring-file-system-changes)
4. [Security Considerations](#security-considerations)
5. [License](#license)

## Prerequisites

- Python 3.6+
- `rsa` library
- `pycryptodome` library
- `watchdog` library

You can install the required libraries using the following command:
```sh
pip install rsa pycryptodome watchdog

