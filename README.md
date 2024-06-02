# Ransomware-Project

# Project: File Encryption, Detection, and Mitigation System

## Overview

This project consists of a series of Python scripts designed to handle file encryption, detection of potentially malicious files, mitigation actions, file decryption, and file system monitoring. The project includes the following scripts:

1. `textfiles_generation.py`
2. `attack.py`
3. `detection.py`
4. `mitigation.py`
5. `decrypt.py`
6. `monitoring.py`
   
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
4. [Script Details](#scriptdetails)


## Prerequisites

- Python 3.6+
- `rsa` library
- `pycryptodome` library
- `watchdog` library

You can install the required libraries using the following command:
```sh
pip install rsa pycryptodome watchdog


## Setup and Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. Ensure all required libraries are installed:
    ```sh
    pip install -r requirements.txt
    ```

3. Make the scripts executable:
    ```sh
    chmod +x *.py
    ```
