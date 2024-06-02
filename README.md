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

## Usage

### Generating Text Files
Run the `textfiles_generation.py` script to generate a specified number of text files:

python textfiles_generation.py

### Encrypting Text Files
Run the attack.py script to encrypt all .txt files in the current directory:

python attack.py

### Detecting Malicious Files
Run the detection.py script to scan for potentially malicious files:

python detection.py

### Mitigating Detected Threats
Run the mitigation.py script to take action on detected malicious files:

python mitigation.py

You will be prompted to choose whether to delete the files or keep them, and optionally restart the system.

### Decrypting Text Files
Run the decrypt.py script to decrypt all previously encrypted .txt files:

python decrypt.py

### Monitoring File System Changes
Run the monitoring.py script to monitor changes in a specific directory:

python monitoring.py


## Script Details
attack.py
This script encrypts all .txt files in the current directory using RSA encryption.

detection.py
This script scans files for the presence of specific keywords that are commonly associated with malicious scripts. If such keywords are found, the file is flagged as potentially malicious.

mitigation.py
This script provides options to delete files flagged as malicious by detection.py or to restart the system.

watchdog_observer.py
This script uses the watchdog library to monitor a specified directory for any changes and logs these changes.

textfiles_generation.py
This script generates a specified number of text files with unique content for testing purposes.

decrypt.py
This script decrypts all previously encrypted .txt files using RSA decryption.
