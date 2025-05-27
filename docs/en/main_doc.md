# OIADB - Comprehensive User Guide

## Table of Contents

*   [1. Introduction](#1-introduction)
    *   [1.1. What is OIADB?](#11-what-is-oiadb)
    *   [1.2. Why Choose OIADB?](#12-why-choose-oiadb)
    *   [1.3. Key Features](#13-key-features)
    *   [1.4. Target Audience](#14-target-audience)
*   [2. Installation and Setup](#2-installation-and-setup)
    *   [2.1. Prerequisites](#21-prerequisites)
        *   [2.1.1. Python](#211-python)
        *   [2.1.2. ADB (Android Debug Bridge)](#212-adb-android-debug-bridge)
        *   [2.1.3. OpenCV and NumPy (Optional, for Image Recognition)](#213-opencv-and-numpy-optional-for-image-recognition)
    *   [2.2. Installing ADB](#22-installing-adb)
        *   [2.2.1. Windows](#221-windows)
        *   [2.2.2. macOS](#222-macos)
        *   [2.2.3. Linux (Debian/Ubuntu)](#223-linux-debianubuntu)
        *   [2.2.4. Verifying ADB Installation](#224-verifying-adb-installation)
    *   [2.3. Installing OIADB](#23-installing-oiadb)
        *   [2.3.1. Installing from PyPI (Recommended)](#231-installing-from-pypi-recommended)
        *   [2.3.2. Installing with Image Recognition Support](#232-installing-with-image-recognition-support)
        *   [2.3.3. Installing from Source (For Developers)](#233-installing-from-source-for-developers)
    *   [2.4. Setting Up Android Device](#24-setting-up-android-device)
        *   [2.4.1. Enable Developer Options](#241-enable-developer-options)
        *   [2.4.2. Enable USB Debugging](#242-enable-usb-debugging)
        *   [2.4.3. Authorize ADB Connection](#243-authorize-adb-connection)
        *   [2.4.4. Debugging over Wi-Fi (Optional)](#244-debugging-over-wi-fi-optional)
    *   [2.5. Verifying OIADB Installation](#25-verifying-oiadb-installation)
*   [3. Library Architecture](#3-library-architecture)
    *   [3.1. Overview](#31-overview)
    *   [3.2. Module Structure](#32-module-structure)
    *   [3.3. Main Workflow](#33-main-workflow)
    *   [3.4. Error Handling and Exceptions](#34-error-handling-and-exceptions)
*   [4. The MyADB Class - Interaction Core](#4-the-myadb-class---interaction-core)
    *   [4.1. Initialization and Configuration](#41-initialization-and-configuration)
    *   [4.2. Main Methods](#42-main-methods)
    *   [4.3. Automatic Server Installation and Management](#43-automatic-server-installation-and-management)
    *   [4.4. Basic Usage Example](#44-basic-usage-example)
*   [5. Commands Module - Detailed Command Set](#5-commands-module---detailed-command-set)
    *   [5.1. `app_info`: Get Application Information](#51-app_info-get-application-information)
    *   [5.2. `apps`: Manage Application Lifecycle](#52-apps-manage-application-lifecycle)
    *   [5.3. `basic`: Basic ADB Commands](#53-basic-basic-adb-commands)
    *   [5.4. `connect`: Manage Device Connections](#54-connect-manage-device-connections)
    *   [5.5. `device_actions`: Device-Level Actions](#55-device_actions-device-level-actions)
    *   [5.6. `device_info`: Collect Device Information](#56-device_info-collect-device-information)
    *   [5.7. `file_ops`: File System Operations](#57-file_ops-file-system-operations)
    *   [5.8. `interaction`: Simulate User Interaction](#58-interaction-simulate-user-interaction)
    *   [5.9. `image_interaction`: Image-Based Interaction](#59-image_interaction-image-based-interaction)
    *   [5.10. `logs`: Collect and Manage Logs](#510-logs-collect-and-manage-logs)
    *   [5.11. `permissions`: Manage Application Permissions](#511-permissions-manage-application-permissions)
    *   [5.12. `xml_dump`: Analyze User Interface](#512-xml_dump-analyze-user-interface)
    *   [5.13. `android14_support` & `ui_compatibility`: Compatibility Support](#513-android14_support--ui_compatibility-compatibility-support)
*   [6. Utils Module - Helper Utilities](#6-utils-module---helper-utilities)
    *   [6.1. `advanced`: Advanced Utilities (Cache, Async, Monitor)](#61-advanced-advanced-utilities-cache-async-monitor)
    *   [6.2. `image_recognition`: Image Recognition Processing](#62-image_recognition-image-recognition-processing)
    *   [6.3. `runner`: ADB Command Execution](#63-runner-adb-command-execution)
    *   [6.4. `platform_utils`: Cross-Platform Utilities](#64-platform_utils-cross-platform-utilities)
    *   [6.5. `adb_manager`: ADB Version Management](#65-adb_manager-adb-version-management)
*   [7. Detailed Usage Guide](#7-detailed-usage-guide)
    *   [7.1. Connecting and Managing Devices](#71-connecting-and-managing-devices)
    *   [7.2. Managing Applications (Install, Uninstall, Run, Stop)](#72-managing-applications-install-uninstall-run-stop)
    *   [7.3. Working with Files and Directories](#73-working-with-files-and-directories)
    *   [7.4. Simulating Interactions (Tap, Swipe, Input)](#74-simulating-interactions-tap-swipe-input)
    *   [7.5. Automating with Image Recognition](#75-automating-with-image-recognition)
    *   [7.6. Collecting Logs and Debugging](#76-collecting-logs-and-debugging)
    *   [7.7. Analyzing UI with XML Dump](#77-analyzing-ui-with-xml-dump)
    *   [7.8. Using Advanced Features (Async, Cache)](#78-using-advanced-features-async-cache)
*   [8. Practical Examples and Advanced Scenarios](#8-practical-examples-and-advanced-scenarios)
    *   [8.1. Simple Automated Test Script](#81-simple-automated-test-script)
    *   [8.2. Automating Repetitive Tasks](#82-automating-repetitive-tasks)
    *   [8.3. Testing Complex UI with Image Recognition](#83-testing-complex-ui-with-image-recognition)
    *   [8.4. Collecting Data from Multiple Devices](#84-collecting-data-from-multiple-devices)
*   [9. Troubleshooting](#9-troubleshooting)
    *   [9.1. Common Errors and Solutions](#91-common-errors-and-solutions)
    *   [9.2. Debugging ADB Connections](#92-debugging-adb-connections)
    *   [9.3. Debugging Image Recognition](#93-debugging-image-recognition)
    *   [9.4. Debugging XML Dump](#94-debugging-xml-dump)
    *   [9.5. Reporting Bugs and Seeking Help](#95-reporting-bugs-and-seeking-help)
*   [10. Best Practices](#10-best-practices)
    *   [10.1. Optimizing Performance](#101-optimizing-performance)
    *   [10.2. Writing Maintainable Code](#102-writing-maintainable-code)
    *   [10.3. Robust Error Handling](#103-robust-error-handling)
    *   [10.4. Efficient Device Management](#104-efficient-device-management)
*   [11. Contributing to the Project](#11-contributing-to-the-project)
    *   [11.1. Contribution Workflow](#111-contribution-workflow)
    *   [11.2. Bug Reports](#112-bug-reports)
    *   [11.3. Feature Requests](#113-feature-requests)
    *   [11.4. Submitting Pull Requests](#114-submitting-pull-requests)
    *   [11.5. Code of Conduct](#115-code-of-conduct)
*   [12. References and Resources](#12-references-and-resources)
    *   [12.1. Official ADB Documentation](#121-official-adb-documentation)
    *   [12.2. OpenCV Documentation](#122-opencv-documentation)
    *   [12.3. OIADB GitHub Repository](#123-oiadb-github-repository)
    *   [12.4. OIADB PyPI Page](#124-oiadb-pypi-page)
*   [13. Appendix](#13-appendix)
    *   [13.1. Android Key Code List](#131-android-key-code-list)
    *   [13.2. Common Logcat Options](#132-common-logcat-options)

---

## 1. Introduction

### 1.1. What is OIADB?

**OIADB** (short for **O**penCV **I**mage **A**ndroid **D**ebug **B**ridge) is a powerful and flexible Python library that acts as a high-level wrapper for the **Android Debug Bridge (ADB)** command-line tool. It is designed to simplify and automate tasks involving interaction, management, and testing of Android devices from a Python environment.

Instead of directly calling complex and hard-to-remember ADB commands, OIADB provides an intuitive, Pythonic API that is easy to use. The library goes beyond simply mapping basic ADB commands; it integrates unique advanced features, most notably **image recognition** capabilities based on the **OpenCV** library. This allows for the creation of robust automation scripts capable of interacting with the Android application's user interface (UI) even without element IDs or a stable UI structure.

Furthermore, OIADB offers utilities for **analyzing UI structure (XML Dump)** with accessibility information support, automatic ADB version management, asynchronous command execution, and cross-platform support (Windows, macOS, Linux, and even Termux on Android).

### 1.2. Why Choose OIADB?

While numerous tools and libraries support Android automation, OIADB stands out with the following advantages:

*   **Pythonic and Easy-to-Use API:** Instead of memorizing ADB command syntax, you can use clear Python functions and classes with comprehensive documentation.
*   **Powerful Automation with Image Recognition:** The ability to find and interact with UI elements based on template images (template matching) opens the door for automating complex applications, games, or apps that don't provide stable APIs or element IDs.
*   **Integrated Advanced Features:** Utilities like XML Dump, automatic server management, asynchronous execution, and command result caching accelerate development and improve execution efficiency.
*   **Cross-Platform:** Works smoothly on popular operating systems, allowing you to develop and run automation scripts anywhere.
*   **Open Source and Community:** As an open-source project, OIADB encourages contributions and development from the community.
*   **Comprehensive Solution:** Provides a complete toolkit ranging from device, application, and file management to UI interaction, debugging, and analysis.

### 1.3. Key Features

*   **Device Management:** Connect/disconnect (USB, Wi-Fi), list devices, get detailed information (model, Android version, resolution, battery, CPU, memory, IP, IMEI, serial...), reboot, shutdown, enter bootloader/recovery mode.
*   **Application Management:** Install/uninstall (APK), start/stop apps, clear data/cache, list installed apps, check installation status, get app info (version, path).
*   **File Operations:** Push/pull files and directories, list files, check existence, create/delete directories, delete files.
*   **User Interface (UI) Interaction:**
    *   **Basic:** Tap, swipe, long press, text input, send key events, press hardware keys (Back, Home, Power, Volume...).
    *   **Advanced:** Pinch/zoom, drag, scroll, unlock screen (pattern, PIN).
*   **Image Recognition (OpenCV):**
    *   Find template images on the screen (single or all occurrences).
    *   Supports searching by region, similarity threshold, scale, and rotation angle.
    *   Optimizes search using grayscale and Canny edge detection.
    *   Direct interaction: Tap found images, wait for images to appear/disappear before interacting.
*   **UI Analysis (XML Dump):**
    *   Get UI structure as XML.
    *   Supports retrieving accessibility properties.
    *   Search for elements based on attributes (text, resource-id, class...). (*Note: Element search from XML dump might require further development or integration with other libraries*).
*   **Log Management:** View real-time logcat, filter logs by tag/priority/message, clear logs, save logs to file, create bug reports.
*   **Permission Management:** Grant/revoke app permissions, list permissions, check permissions.
*   **Advanced Utilities:**
    *   Asynchronous ADB command execution.
    *   Cache command results for speed.
    *   Monitor device connection/disconnection events.
    *   Automatically manage (download, install) the appropriate ADB version for the OS.
    *   Automatically install and manage oiadb-server on the device (required for some advanced features like XML Dump).

### 1.4. Target Audience

OIADB is suitable for a wide range of users:

*   **QA Automation Engineers:** Build efficient and flexible automated test scripts for Android applications.
*   **Android Developers:** Automate repetitive tasks during development, debugging, or unit testing.
*   **DevOps Engineers:** Integrate Android device management tasks into CI/CD pipelines.
*   **Python Users:** Anyone wanting to interact with and control Android devices via Python code.
*   **Researchers:** Collect data or perform automated experiments on Android devices.

---

## 2. Installation and Setup

This section provides detailed instructions for installing OIADB and preparing your working environment.

### 2.1. Prerequisites

Before installing OIADB, ensure your system meets the following requirements:

#### 2.1.1. Python

*   **Version:** Python 3.6 or higher. Python 3.7+ is recommended to leverage the latest language features.
*   **Check Version:** Open a terminal or command prompt and run:
    ```bash
    python --version
    # or
    python3 --version
    ```
*   **Install Python:** If you don't have Python, download and install it from the official [python.org](https://www.python.org/downloads/) website. Ensure you check the "Add Python to PATH" option during installation on Windows.
*   **pip:** The `pip` package manager is usually installed with Python. Check with `pip --version` or `pip3 --version`. If missing, refer to the `pip` installation guide at [pip.pypa.io](https://pip.pypa.io/en/stable/installation/).

#### 2.1.2. ADB (Android Debug Bridge)

*   **Concept:** ADB is a versatile command-line tool that lets you communicate with an Android device. OIADB uses ADB underneath to execute commands.
*   **Requirement:** ADB needs to be installed on your computer and **accessible via the system's PATH environment variable** (meaning you can run the `adb` command from any directory in your terminal).
*   **Automatic Installation (Optional):** OIADB can automatically download and set up ADB if it's not found (this feature is enabled by default when initializing `MyADB`). However, installing it manually beforehand ensures stability and gives you control over the ADB version.
*   **Installation Guide:** See details in section [2.2. Installing ADB](#22-installing-adb).

#### 2.1.3. OpenCV and NumPy (Optional, for Image Recognition)

*   **Purpose:** These two libraries are **required** if you intend to use image recognition features (`image_interaction`, `image_recognition`).
*   **OpenCV (cv2):** The leading open-source library for image processing and computer vision.
*   **NumPy:** The fundamental package for scientific computing in Python, needed for OpenCV's array operations.
*   **Installation:** You can install them along with OIADB by specifying the `[image]` extra dependency:
    ```bash
    pip install oiadb[image]
    ```
    Or install them individually:
    ```bash
    pip install opencv-python numpy
    ```
*   **Note:** If you don't need image recognition, you can skip this step and install the basic OIADB package. The library will function normally for other features but will raise an error if you attempt to call image-related functions.

### 2.2. Installing ADB

Follow these steps to install ADB on your operating system:

#### 2.2.1. Windows

1.  **Download Platform Tools:** Go to the [SDK Platform Tools release notes](https://developer.android.com/studio/releases/platform-tools) page and download the latest ZIP file for Windows.
2.  **Extract:** Unzip the file to a permanent location on your computer, for example, `C:\platform-tools`.
3.  **Add to PATH:**
    *   Press the `Windows` key, type "environment variables", and select "Edit the system environment variables".
    *   In the System Properties window, click the "Environment Variables..." button.
    *   In the "System variables" section (or "User variables" if you only want it for the current user), find the `Path` variable and click "Edit...".
    *   Click "New" and paste the path to the directory where you extracted the tools (e.g., `C:\platform-tools`).
    *   Click "OK" on all windows.
4.  **Restart Terminal:** Close and reopen any open command prompt or PowerShell windows for the changes to take effect.

#### 2.2.2. macOS

1.  **Using Homebrew (Recommended):** If you have [Homebrew](https://brew.sh/) installed, open Terminal and run:
    ```bash
    brew install --cask android-platform-tools
    ```
2.  **Manual Installation:**
    *   Download the Platform Tools ZIP for macOS from the [SDK Platform Tools release notes](https://developer.android.com/studio/releases/platform-tools).
    *   Extract the ZIP file, for example, to `~/platform-tools`.
    *   Add the directory to your PATH. Edit your shell configuration file (`~/.zshrc` for Zsh, `~/.bash_profile` or `~/.bashrc` for Bash) and add the following line:
        ```bash
        export PATH="$HOME/platform-tools:$PATH"
        ```
    *   Save the file and apply the changes by running `source ~/.zshrc` (or the corresponding file for your shell) or by opening a new Terminal window.

#### 2.2.3. Linux (Debian/Ubuntu)

1.  **Using Package Manager:** Open a terminal and run:
    ```bash
    sudo apt update
    sudo apt install android-tools-adb
    ```
    (Package name might vary slightly on other distributions, e.g., `android-adb` on Fedora).

#### 2.2.4. Verifying ADB Installation

Open a new terminal or command prompt and run:

```bash
adb version
```

If ADB is installed correctly and added to your PATH, you should see output displaying the ADB version number.

### 2.3. Installing OIADB

#### 2.3.1. Installing from PyPI (Recommended)

The easiest way to install the latest stable version of OIADB is using pip:

```bash
pip install oiadb
```

#### 2.3.2. Installing with Image Recognition Support

If you need the image recognition features, install with the `[image]` extra, which will also pull in `opencv-python` and `numpy`:

```bash
pip install oiadb[image]
```

#### 2.3.3. Installing from Source (For Developers)

If you want to contribute to OIADB or use the very latest (potentially unstable) code:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/tiendung2k03/oiadb.git
    cd oiadb
    ```
2.  **Install in editable mode:** This allows you to make changes to the code and have them reflected immediately without reinstalling.
    ```bash
    pip install -e .
    ```
    If you need image support:
    ```bash
    pip install -e .[image]
    ```

### 2.4. Setting Up Android Device

To allow ADB (and thus OIADB) to communicate with your Android device, you need to enable developer options and USB debugging.

#### 2.4.1. Enable Developer Options

1.  Go to **Settings** on your Android device.
2.  Scroll down and tap on **About phone** (or **About tablet**).
3.  Find the **Build number** entry.
4.  Tap the **Build number** entry **seven times** consecutively. You might see a countdown message.
5.  You'll see a message saying "You are now a developer!" (or similar).
6.  Go back to the main Settings screen, and you should now see a new **Developer options** menu (it might be under **System** or near the bottom).

#### 2.4.2. Enable USB Debugging

1.  Go to **Settings > Developer options**.
2.  Find the **USB debugging** option and toggle it **on**.
3.  Confirm any warning messages.

#### 2.4.3. Authorize ADB Connection

1.  Connect your Android device to your computer using a USB cable.
2.  On your device's screen, you should see a dialog box asking "Allow USB debugging?" with your computer's RSA key fingerprint.
3.  Check the box **Always allow from this computer** (recommended for convenience).
4.  Tap **Allow** (or **OK**).

#### 2.4.4. Debugging over Wi-Fi (Optional)

Connecting via Wi-Fi is convenient as it doesn't require a USB cable after initial setup.

*   **Method 1 (Android 10 and below, or initial setup via USB):**
    1.  Connect your device via USB and ensure it's authorized (`adb devices` shows `device`).
    2.  Find your device's IP address (usually in **Settings > Wi-Fi > [Your Network] > Advanced** or **Settings > About phone > Status**).
    3.  Run the following command in your terminal:
        ```bash
        adb tcpip 5555
        ```
        (This tells the device to listen for ADB connections on port 5555. You can use a different port if needed).
    4.  Disconnect the USB cable.
    5.  Connect to the device using its IP address and the port:
        ```bash
        adb connect DEVICE_IP:5555
        ```
        (Replace `DEVICE_IP` with the actual IP address).
*   **Method 2 (Android 11 and above - Wireless Debugging):**
    1.  Ensure your device and computer are on the same Wi-Fi network.
    2.  Go to **Settings > Developer options > Wireless debugging**.
    3.  Toggle **Wireless debugging** on.
    4.  Tap **Pair device with pairing code**. Note the **IP address & Port** and the **Wi-Fi pairing code** displayed.
    5.  On your computer, run:
        ```bash
        adb pair PAIRING_IP:PAIRING_PORT
        ```
        (Use the IP and *pairing* port shown on the device).
    6.  Enter the **Wi-Fi pairing code** when prompted in the terminal.
    7.  After successful pairing, note the *different* **IP address & Port** listed under the main "Wireless debugging" toggle (this is the *connection* port).
    8.  Connect using this connection port:
        ```bash
        adb connect CONNECTION_IP:CONNECTION_PORT
        ```

### 2.5. Verifying OIADB Installation

1.  Connect your authorized Android device via USB or Wi-Fi.
2.  Open a Python interpreter or create a simple Python script (`test_oiadb.py`):
    ```python
    from oiadb import MyADB
    
    try:
        # Initialize MyADB, automatically finds the first connected device
        adb = MyADB()
        
        # Get device serial number
        serial = adb.run("get-serialno")
        print(f"Successfully connected to device: {serial.strip()}")
        
        # Get device model
        model = adb.run("shell getprop ro.product.model")
        print(f"Device model: {model.strip()}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure ADB is installed, your device is connected, authorized, and USB debugging is enabled.")
    ```
3.  Run the script: `python test_oiadb.py`.
4.  If everything is set up correctly, you should see the serial number and model of your connected device printed without errors.

---




## 3. Library Architecture

### 3.1. Overview

OIADB is structured as a high-level wrapper around the standard ADB command-line tool. It intercepts Python method calls, translates them into appropriate ADB commands, executes these commands using the `subprocess` module, parses the output (stdout and stderr), and returns the results in a Python-friendly format or raises specific exceptions upon failure.

Key components include:

*   **`MyADB` Class:** The main entry point for interacting with the library. It manages the connection to a specific device, handles command execution, and provides access to various functionalities.
*   **`commands` Module:** Contains sub-modules organized by functionality (e.g., `apps`, `file_ops`, `interaction`), each implementing specific ADB command logic.
*   **`utils` Module:** Provides helper classes and functions for tasks like image recognition (`image_recognition`), asynchronous command execution (`advanced`), platform detection (`platform_utils`), ADB executable management (`adb_manager`), and command running (`runner`).
*   **`exceptions` Module:** Defines custom exception classes for specific ADB-related errors (e.g., `DeviceNotFoundError`, `ADBCommandError`, `FileOperationError`).
*   **`oiadb-server`:** An optional companion Android application (instrumentation test runner) that runs on the device to facilitate certain advanced features like efficient XML dumping.

### 3.2. Module Structure

```
oiadb/
├── __init__.py       # Makes oiadb a package, exports MyADB
├── adb.py            # Defines the main MyADB class
├── commands/         # Modules for specific command groups
│   ├── __init__.py
│   ├── app_info.py
│   ├── apps.py
│   ├── basic.py
│   ├── connect.py
│   ├── device_actions.py
│   ├── device_info.py
│   ├── file_ops.py
│   ├── image_interaction.py
│   ├── interaction.py
│   ├── logs.py
│   ├── permissions.py
│   └── xml_dump.py
├── utils/            # Helper utilities
│   ├── __init__.py
│   ├── adb_manager.py
│   ├── advanced.py
│   ├── image_recognition.py
│   ├── platform_utils.py
│   └── runner.py
├── exceptions.py     # Custom exception classes
├── server/           # Contains the oiadb-server APK
│   └── oiadb-server.apk
└── py.typed          # Marker file for type checking
```

### 3.3. Main Workflow

1.  **Initialization:** The user creates an instance of `MyADB`, optionally specifying a device ID, ADB path, and other configurations.
2.  **Device Connection:** `MyADB` verifies the ADB installation, finds the target device (or the first available one), and establishes a connection context.
3.  **Server Management (Optional):** If `auto_start_server` is enabled, `MyADB` checks for `oiadb-server` on the device, installs/updates it if necessary, starts it, and sets up port forwarding.
4.  **Command Call:** The user calls a method on the `MyADB` instance (e.g., `adb.install_app(...)`, `adb.tap(...)`).
5.  **Command Delegation:** `MyADB` delegates the call to the appropriate function or class within the `commands` or `utils` modules.
6.  **ADB Command Construction:** The specific command module constructs the necessary ADB command string(s).
7.  **Command Execution:** The `runner` utility (or `advanced` for async) executes the ADB command using `subprocess.run` or `subprocess.Popen`.
8.  **Result Parsing:** The output (stdout, stderr) and return code are captured.
9.  **Return Value/Exception:** The result is parsed into a Pythonic format (string, list, boolean, custom object) and returned to the user. If an error occurs (non-zero return code, specific stderr patterns), an appropriate exception from the `exceptions` module is raised.

### 3.4. Error Handling and Exceptions

OIADB uses custom exceptions to provide more specific error information than generic Python exceptions:

*   **`ADBError`:** Base class for most OIADB errors.
*   **`DeviceNotFoundError`:** Raised when no connected devices are found or the specified `device_id` does not match any connected device.
*   **`ADBCommandError(ADBError)`:** Raised when an ADB command execution fails (returns a non-zero exit code). Contains attributes like `command`, `return_code`, `stdout`, and `stderr`.
*   **`FileOperationError(ADBCommandError)`:** Specific error for failed `push` or `pull` operations.
*   **`InvalidInputError(ADBError)`:** Raised for invalid user input (e.g., incorrect coordinates).
*   **`ImageNotFoundError(ADBError)`:** Raised by image recognition functions when the template image cannot be found on the screen.
*   **`ServerError(ADBError)`:** Raised when there's an issue communicating with the `oiadb-server` on the device.

Properly handling these exceptions using `try...except` blocks is crucial for writing robust automation scripts.

---

## 4. The MyADB Class - Interaction Core

The first step in using OIADB is creating an instance of the `MyADB` class.

### 4.1. Initialization and Configuration

```python
from oiadb import MyADB
from oiadb.exceptions import DeviceNotFoundError, ADBError

try:
    # Simple initialization, automatically finds the first device
    adb_instance_1 = MyADB()
    print(f"Successfully connected to device: {adb_instance_1.device_id}")

    # Initialize with a specific device ID (e.g., from 'adb devices' output)
    # device_serial = "emulator-5554" # Or "192.168.1.100:5555" if connected via Wi-Fi
    # adb_instance_2 = MyADB(device_id=device_serial)
    # print(f"Successfully connected to device: {adb_instance_2.device_id}")

    # Initialize with other configuration options
    adb_instance_3 = MyADB(
        cache_enabled=False,      # Disable command result caching
        timeout=60,               # Increase command timeout to 60 seconds
        adb_path="/usr/local/bin/adb", # Specify a custom ADB path
        auto_start_server=False,  # Do not automatically install/start oiadb-server
        auto_install_adb=False    # Do not automatically download ADB if not found
    )
    print(f"Successfully connected to device: {adb_instance_3.device_id}")

except DeviceNotFoundError:
    print("Error: No devices found.")
except ADBError as e:
    print(f"ADB Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

**Key Initialization Parameters (`__init__`):**

*   `device_id` (Optional[str], default=None): The ID (serial number or `ip:port`) of the target device. If `None`, OIADB attempts to connect to the first device found in the `adb devices` list.
*   `cache_enabled` (bool, default=True): Enables or disables the command result caching mechanism. When enabled, identical commands executed within a short period (default 60 seconds) will return the cached result instead of re-executing, significantly speeding up information-retrieval commands.
*   `timeout` (int, default=30): The maximum time (in seconds) to wait for an ADB command to complete before considering it failed (timed out).
*   `adb_path` (Optional[str], default=None): Allows specifying the absolute path to the `adb` executable. If `None`, OIADB tries to find ADB in the system PATH or automatically download it (if `auto_install_adb=True`).
*   `auto_start_server` (bool, default=True): If `True`, OIADB automatically checks, installs (if needed), and starts the `oiadb-server.apk` on the device upon `MyADB` initialization. This server is required for some advanced features like XML Dump.
*   `auto_install_adb` (bool, default=True): If `True` and ADB is not found in the PATH or `adb_path` is invalid, OIADB attempts to automatically download and install the appropriate ADB version for the current operating system.

**Key Attributes of a `MyADB` instance:**

*   `device_id` (str): The ID of the currently connected device.
*   `adb_path` (str): The path to the ADB executable being used.
*   `platform_info` (PlatformInfo): An object containing information about the current operating system.
*   `timeout` (int): The timeout value currently in use.
*   `cache_enabled` (bool): The status of the cache.
*   `_cache` (ResultCache | None): The instance of the cache class (if enabled).
*   `_async_executor` (AsyncCommandExecutor): The instance used for executing asynchronous commands.
*   `local_server_port` (int | None): The local port used for forwarding to the `oiadb-server` on the device (if the server was started).

### 4.2. Main Methods

The `MyADB` class provides several core methods for executing commands and managing the device. More specific functionalities are delegated to modules within `commands` and `utils`, but the following methods are often used directly:

*   **`run(command: str, use_cache: bool = True) -> str`:**
    *   **Description:** Executes a custom ADB command and returns the `stdout` result as a string. This is the fundamental method for most ADB interactions.
    *   **Parameters:**
        *   `command`: The ADB command string to execute (the part after `adb -s <device_id>`). Examples: `"shell getprop ro.product.model"`, `"logcat -d"`.
        *   `use_cache`: Whether to use the cache for this command (only effective if `cache_enabled=True` during initialization).
    *   **Returns:** The `stdout` string of the command if successful.
    *   **Raises:** `ADBCommandError` if the command fails (return code != 0), or other exceptions like `DeviceNotFoundError`.
    *   **Example:**
        ```python
        try:
            model = adb.run("shell getprop ro.product.model")
            print(f"Model: {model.strip()}")
            # Get recent logs, don't use cache
            logs = adb.run("logcat -d -t 50", use_cache=False)
            print(f"Logs:\n{logs}")
        except ADBCommandError as e:
            print(f"Error running command '{e.command}': {e.stderr}")
        ```

*   **`run_async(command: str, command_id: Optional[str] = None, callback: Optional[Callable] = None) -> str`:**
    *   **Description:** Executes an ADB command asynchronously (does not block the main thread). Useful for long-running commands like continuous `logcat` or event monitoring.
    *   **Parameters:**
        *   `command`: The ADB command string to execute.
        *   `command_id` (Optional): A unique ID to manage the asynchronous process. If `None`, a random ID is generated.
        *   `callback` (Optional): A function to be called when the command completes. The callback function receives a `CommandResult` object as an argument.
    *   **Returns:** The `command_id` used for the command.
    *   **Example:**
        ```python
        from oiadb.utils.advanced import CommandResult # Import for type hint

        def log_handler(result: CommandResult):
            if result.success:
                print(f"Logcat output:\n{result.stdout}")
            else:
                print(f"Logcat error: {result.stderr}")

        cmd_id = adb.run_async("logcat -d", callback=log_handler)
        print(f"Started logcat with ID: {cmd_id}")
        # ... (do other work while logcat runs)
        # Can check status: adb._async_executor.is_running(cmd_id)
        # Or get result later: result = adb._async_executor.get_result(cmd_id)
        ```

*   **`get_devices_list() -> List[str]`:**
    *   **Description:** Returns a list of IDs for all devices currently connected and recognized by ADB on the host machine.
    *   **Returns:** A list of device ID strings.
    *   **Example:**
        ```python
        connected_devices = adb.get_devices_list()
        print(f"Connected devices: {connected_devices}")
        ```

*   **`push_file(local_path: str, remote_path: str) -> bool`:**
    *   **Description:** Pushes (copies) a file or directory from the local computer to the Android device.
    *   **Parameters:**
        *   `local_path`: Path to the file/directory on the computer.
        *   `remote_path`: Destination path on the Android device.
    *   **Returns:** `True` if successful, `False` otherwise.
    *   **Raises:** `FileOperationError` on failure.
    *   **Example:**
        ```python
        if adb.push_file("./my_script.sh", "/data/local/tmp/script.sh"):
            print("File pushed successfully!")
        ```

*   **`pull_file(remote_path: str, local_path: str) -> bool`:**
    *   **Description:** Pulls (copies) a file or directory from the Android device to the local computer.
    *   **Parameters:**
        *   `remote_path`: Path to the file/directory on the Android device.
        *   `local_path`: Destination path on the computer.
    *   **Returns:** `True` if successful, `False` otherwise.
    *   **Raises:** `FileOperationError` on failure.
    *   **Example:**
        ```python
        if adb.pull_file("/sdcard/DCIM/Camera/image.jpg", "./downloaded_image.jpg"):
            print("File pulled successfully!")
        ```

*   **`take_screenshot(output_path: Optional[str] = None, as_bytes: bool = False) -> Union[str, bytes]`:**
    *   **Description:** Takes a screenshot of the device's current display.
    *   **Parameters:**
        *   `output_path` (Optional): Path to save the PNG image file on the computer. If `None` and `as_bytes=False`, the image is saved to a temporary path.
        *   `as_bytes` (bool): If `True`, returns the image data as bytes instead of saving to a file. `output_path` is ignored.
    *   **Returns:** The path to the saved image file (if `as_bytes=False`) or a `bytes` object containing the PNG image data (if `as_bytes=True`).
    *   **Raises:** `ADBCommandError` if taking the screenshot fails.
    *   **Example:**
        ```python
        # Save to file
        saved_path = adb.take_screenshot("./screenshot.png")
        print(f"Screenshot saved to: {saved_path}")

        # Get bytes data
        image_bytes = adb.take_screenshot(as_bytes=True)
        # (Can use PIL or other libraries to process image_bytes)
        # from PIL import Image
        # import io
        # img = Image.open(io.BytesIO(image_bytes))
        # img.show()
        ```

*   **`get_screen_size() -> Dict[str, int]`:**
    *   **Description:** Gets the screen dimensions (width and height) of the device.
    *   **Returns:** A dictionary like `{"width": <int>, "height": <int>}`.
    *   **Example:**
        ```python
        size = adb.get_screen_size()
        print(f"Screen size: {size['width']}x{size['height']}")
        ```

### 4.3. Automatic Server Installation and Management

One convenient feature of OIADB is its ability to automatically manage the `oiadb-server` on the device. This server is a small Android application (based on an instrumentation test runner) required for some advanced features, particularly `xml_dump` for efficient UI structure retrieval.

When you initialize `MyADB` with `auto_start_server=True` (the default), the following steps happen automatically:

1.  **Server Check:** OIADB checks if the `oiadb-server` (both the main package and the test package) is already installed on the device.
2.  **Install/Update:** If the server is not installed or if an older version is detected (version checking logic might be improved in the future), OIADB will:
    *   Locate the pre-packaged `oiadb-server.apk` within the OIADB library.
    *   Push the APK file to a temporary location on the device.
    *   Execute the `pm install` command to install or update the server.
    *   Delete the temporary APK file from the device.
3.  **Start Server:** OIADB executes the `am instrument` command to start the `oiadb-server`'s instrumentation test runner in the background.
4.  **Set Up Port Forwarding:** OIADB finds an available local port on the host machine and sets up ADB port forwarding (`adb forward`) from that local port to the port the `oiadb-server` is listening on within the device (default is 9008).
5.  **Verify Server Connection:** OIADB sends a `ping` request to the server via the forwarded port to ensure the server is running and ready to accept commands.

This entire process simplifies the usage of server-dependent features. If any error occurs during this process (e.g., installation fails, server doesn't start), an `ADBError` exception will be raised.

You can disable this feature by setting `auto_start_server=False` during `MyADB` initialization if you prefer to manage the server manually or don't require the features that depend on it.

### 4.4. Basic Usage Example

```python
from oiadb import MyADB
from oiadb.exceptions import ADBError, DeviceNotFoundError

try:
    # Connect to the first found device
    adb = MyADB()
    print(f"Connected to: {adb.device_id}")

    # Get some basic info
    model = adb.run("shell getprop ro.product.model").strip()
    version = adb.run("shell getprop ro.build.version.release").strip()
    size = adb.get_screen_size()
    print(f"Device: {model}, Android {version}, Screen: {size['width']}x{size['height']}")

    # Take a screenshot
    screenshot_file = adb.take_screenshot("current_screen.png")
    print(f"Screenshot taken: {screenshot_file}")

    # Push a text file to the device
    with open("hello.txt", "w") as f:
        f.write("Hello from OIADB!")
    if adb.push_file("hello.txt", "/sdcard/hello_oiadb.txt"):
        print("Pushed 'hello.txt' to /sdcard/")
        # Check file content on device
        content = adb.run("shell cat /sdcard/hello_oiadb.txt")
        print(f"Content on device: {content.strip()}")
        # Remove file from device
        adb.run("shell rm /sdcard/hello_oiadb.txt")
        print("Removed file from device.")

except DeviceNotFoundError:
    print("Error: No devices found.")
except ADBError as e:
    print(f"ADB Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---




## 5. Commands Module - Detailed Command Set

The `commands` module is where the main functionalities of OIADB are gathered, organized into separate Python files corresponding to specific task groups. This helps keep the source code clear, maintainable, and extensible.

To use these commands, you typically call the corresponding methods on an initialized `MyADB` instance. The `MyADB` class acts as a facade, delegating commands to the appropriate functions/classes within the `commands` module.

```python
from oiadb import MyADB

adb = MyADB()

# Example: Call the app installation command (uses logic in commands/apps.py)
# adb.install_app("path/to/app.apk") 

# Example: Call the command to get device model (uses logic in commands/device_info.py)
# model = adb.get_device_model() 
```

In this section, we will delve into each command sub-module, explaining its function and usage.

### 5.1. `app_info`: Get Application Information

This module provides basic functions to query information about installed application packages on the device.

**Location:** `oiadb/commands/app_info.py`

**Main Functions:**

*   **`list_packages() -> str`:**
    *   **Description:** Lists all installed application packages (both system and third-party) on the device.
    *   **ADB Equivalent:** `adb shell pm list packages`
    *   **Returns:** A string containing the list of package names, one per line (e.g., `package:com.example.app`).

*   **`list_packages_r() -> str`:**
    *   **Description:** Lists all packages and the paths to their APK files.
    *   **ADB Equivalent:** `adb shell pm list packages -f` (Note: The original command is `pm list packages -f`. The `-r` mentioned in the source might be a typo or custom implementation detail).
    *   **Returns:** A string containing the list of packages and their APK paths.

*   **`list_packages_3rd() -> str`:**
    *   **Description:** Lists only third-party application packages (installed by the user).
    *   **ADB Equivalent:** `adb shell pm list packages -3`
    *   **Returns:** A string containing the list of third-party package names.

*   **`list_packages_sys() -> str`:**
    *   **Description:** Lists only system application packages.
    *   **ADB Equivalent:** `adb shell pm list packages -s`
    *   **Returns:** A string containing the list of system package names.

*   **`list_packages_uninstalled() -> str`:**
    *   **Description:** Lists packages that have been uninstalled but still retain their data (usually uncommon).
    *   **ADB Equivalent:** `adb shell pm list packages -u`
    *   **Returns:** A string containing the list of uninstalled package names with retained data.

*   **`dumpsys_package() -> str`:**
    *   **Description:** Retrieves detailed information about all packages on the system using `dumpsys`. The output is very large and detailed.
    *   **ADB Equivalent:** `adb shell dumpsys package packages`
    *   **Returns:** A large string containing detailed information for all packages.

*   **`dump(name: str) -> str`:**
    *   **Description:** Retrieves detailed information about a specific application package using `dumpsys`.
    *   **Parameter:**
        *   `name`: The package name to query (e.g., `"com.android.settings"`).
    *   **ADB Equivalent:** `adb shell dumpsys package <name>`
    *   **Returns:** A string containing detailed information for the specified package.
    *   **Raises:** `ADBCommandError` if the package doesn't exist or another error occurs.

*   **`apk_path(package: str) -> str`:**
    *   **Description:** Gets the full path to the base APK file of an installed application package.
    *   **Parameter:**
        *   `package`: The application package name (e.g., `"com.google.android.youtube"`).
    *   **ADB Equivalent:** `adb shell pm path <package>`
    *   **Returns:** A string containing the path (e.g., `package:/data/app/com.google.android.youtube-1/base.apk`).
    *   **Raises:** `ADBCommandError` if the package is not found.

*   **`check_package_installed(package: str) -> bool`:**
    *   **Description:** Checks if a specific package is installed on the device.
    *   **Parameter:**
        *   `package`: The package name to check.
    *   **Implementation:** Typically checks if the package name appears in the output of `list_packages()`.
    *   **Returns:** `True` if the package is installed, `False` otherwise.

**Usage Example:**

```python
from oiadb import MyADB
from oiadb.commands import app_info # Can be accessed directly if needed

try:
    adb = MyADB()
    package_name = "com.android.settings"

    # Check if settings app is installed
    is_installed = app_info.check_package_installed(package_name)
    print(f"Is '{package_name}' installed? {is_installed}")

    if is_installed:
        # Get APK path
        path = app_info.apk_path(package_name)
        print(f"APK path for '{package_name}': {path.strip()}")

        # Get detailed dump
        # dump_info = app_info.dump(package_name)
        # print(f"\nDumpsys info for '{package_name}':\n{dump_info[:500]}...") # Print first 500 chars

    # List third-party apps
    third_party_apps = app_info.list_packages_3rd()
    print("\nThird-party packages:")
    print(third_party_apps)

except Exception as e:
    print(f"An error occurred: {e}")
```

### 5.2. `apps`: Manage Application Lifecycle

This module (often implemented within a class like `AppCommands`) handles operations related to the lifecycle of applications, such as installation, uninstallation, starting, stopping, and clearing data.

**Location:** `oiadb/commands/apps.py` (Often encapsulated in a class)

**Main Functions/Methods (within `AppCommands` class):**

*   **`install(apk_path: str, grant_permissions: bool = False, reinstall: bool = False, test_app: bool = False, allow_downgrade: bool = False) -> bool`:**
    *   **Description:** Installs an application from an APK file located on the host computer.
    *   **Parameters:**
        *   `apk_path`: Path to the `.apk` file on the local machine.
        *   `grant_permissions` (bool): If `True`, attempts to grant all runtime permissions declared in the app's manifest (requires Android 6.0+).
        *   `reinstall` (bool): If `True`, allows reinstalling the app, keeping existing data (`-r` flag).
        *   `test_app` (bool): If `True`, allows installing a test APK (`-t` flag).
        *   `allow_downgrade` (bool): If `True`, allows installing an older version over a newer one (`-d` flag).
    *   **ADB Equivalent:** `adb install [-r] [-t] [-g] [-d] <apk_path>`
    *   **Returns:** `True` if installation succeeds, `False` otherwise.
    *   **Raises:** `InstallationError` or `FileNotFoundError`.

*   **`uninstall(package: str, keep_data: bool = False) -> bool`:**
    *   **Description:** Uninstalls an application from the device.
    *   **Parameters:**
        *   `package`: The package name of the app to uninstall.
        *   `keep_data` (bool): If `True`, keeps the application's data and cache directories (`-k` flag).
    *   **ADB Equivalent:** `adb uninstall [-k] <package>`
    *   **Returns:** `True` if uninstallation succeeds, `False` otherwise.
    *   **Raises:** `UninstallationError`.

*   **`start_app(package: str, activity: Optional[str] = None) -> bool`:**
    *   **Description:** Starts the main activity of an application, or a specific activity if provided.
    *   **Parameters:**
        *   `package`: The package name of the app to start.
        *   `activity` (Optional): The specific activity to launch (e.g., `.MainActivity`, `com.example.app.SpecificActivity`). If `None`, tries to launch the default main activity.
    *   **ADB Equivalent:** `adb shell am start -n <package>/[activity]` or `adb shell monkey -p <package> -c android.intent.category.LAUNCHER 1` (if activity is None).
    *   **Returns:** `True` if the start command was issued successfully (doesn't guarantee the app started without crashing).

*   **`stop_app(package: str) -> bool`:**
    *   **Description:** Force-stops an application.
    *   **Parameter:**
        *   `package`: The package name of the app to stop.
    *   **ADB Equivalent:** `adb shell am force-stop <package>`
    *   **Returns:** `True` if the stop command was issued successfully.

*   **`clear_app_data(package: str) -> bool`:**
    *   **Description:** Clears all data associated with an application (equivalent to going to Settings > Apps > [App Name] > Storage > Clear Data).
    *   **Parameter:**
        *   `package`: The package name of the app to clear.
    *   **ADB Equivalent:** `adb shell pm clear <package>`
    *   **Returns:** `True` if the clear command was issued successfully.

**Usage Example:**

```python
from oiadb import MyADB
from oiadb.exceptions import InstallationError, PackageNotFoundError
import time

try:
    adb = MyADB()
    package = "com.android.calculator2" # Example package
    apk_file = "path/to/calculator.apk" # Replace with actual path if testing install

    # Check if installed
    if adb.run(f"shell pm path {package}"): # Simple check using pm path
        print(f"Application {package} is installed.")

        # Stop the app
        print("Stopping the app...")
        adb.stop_app(package)
        time.sleep(1)

        # Start the app
        print("Starting the app...")
        adb.start_app(package)
        time.sleep(2)

        # Stop again
        adb.stop_app(package)

        # Uninstall (Careful!)
        # print("Uninstalling...")
        # adb.uninstall(package)

        # Clear data (Careful!)
        # print("Clearing data...")
        # adb.clear_app_data(package)

        # Relaunch
        print("Relaunching the app...")
        adb.start_app(package)
        
    else:
        print(f"Application {package} is not installed.")
        # Try installing if APK exists
        # try:
        #     adb.install(apk_file, grant_permissions=True)
        #     print("Installation successful!")
        # except InstallationError as e:
        #     print(f"Installation failed: {e}")
        # except FileNotFoundError:
        #     print("APK file not found for installation.")

except PackageNotFoundError as e:
    print(f"Error: Package {e.package_name} not found")
except Exception as e:
    print(f"An error occurred: {e}")
```

### 5.3. `basic`: Basic ADB Commands

This module contains functions corresponding to the most fundamental ADB commands, often used for managing the ADB server, device connections, and general actions.

**Location:** `oiadb/commands/basic.py`

**Main Functions:**

*   **`devices() -> str`:**
    *   **Description:** Lists connected devices and their states (e.g., `device`, `offline`, `unauthorized`).
    *   **ADB Equivalent:** `adb devices`
    *   **Returns:** String output from the `adb devices` command.

*   **`devices_long() -> str`:**
    *   **Description:** Lists connected devices with more detailed information (often includes product, model, device identifiers).
    *   **ADB Equivalent:** `adb devices -l`
    *   **Returns:** String output from the `adb devices -l` command.

*   **`root() -> str`:**
    *   **Description:** Restarts the `adbd` (ADB daemon on the device) with root permissions. Only works on rooted devices or eng/userdebug builds.
    *   **ADB Equivalent:** `adb root`
    *   **Returns:** String output from the `adb root` command (usually "restarting adbd as root" or an error message).

*   **`start_server() -> str`:**
    *   **Description:** Starts the ADB server process on the host computer if it's not already running.
    *   **ADB Equivalent:** `adb start-server`
    *   **Returns:** String output from the command.

*   **`kill_server() -> str`:**
    *   **Description:** Stops the ADB server process on the host computer.
    *   **ADB Equivalent:** `adb kill-server`
    *   **Returns:** String output from the command.

*   **`reboot() -> str`:**
    *   **Description:** Reboots the Android device.
    *   **ADB Equivalent:** `adb reboot`
    *   **Returns:** String output (usually empty on success).

*   **`shell() -> str`:**
    *   **Description:** Opens an interactive shell on the device. This function in OIADB might just execute `adb shell` without truly opening an interactive session, or return the output of some default shell command. The specific implementation needs checking.
    *   **ADB Equivalent:** `adb shell`
    *   **Returns:** Output from the shell command (if any).

*   **`help() -> str`:**
    *   **Description:** Displays the general ADB help information.
    *   **ADB Equivalent:** `adb help`
    *   **Returns:** String containing the help content.

*   **`custom_command(device_id: str, command: str) -> str`:**
    *   **Description:** Executes a custom ADB command targeting a specific device. Useful for running commands not directly supported by OIADB or when needing explicit device targeting.
    *   **Parameters:**
        *   `device_id`: The ID of the target device.
        *   `command`: The command string to execute (the part after `adb -s <device_id>`).
    *   **ADB Equivalent:** `adb -s <device_id> <command>`
    *   **Returns:** String output from the command.

*   **`usb_only(command: str) -> str`:**
    *   **Description:** Executes an ADB command targeting only a USB-connected device (if multiple devices, including emulators/Wi-Fi, are present).
    *   **Parameter:** `command`: The command string to execute (the part after `adb -d`).
    *   **ADB Equivalent:** `adb -d <command>`
    *   **Returns:** String output from the command.

*   **`emulator_only(command: str) -> str`:**
    *   **Description:** Executes an ADB command targeting only a running emulator (if multiple devices, including USB/Wi-Fi, are present).
    *   **Parameter:** `command`: The command string to execute (the part after `adb -e`).
    *   **ADB Equivalent:** `adb -e <command>`
    *   **Returns:** String output from the command.

**Usage Example:**

```python
from oiadb import MyADB
from oiadb.commands import basic # Can be accessed directly if needed

try:
    adb = MyADB() # Connect to the first device

    # List devices with details
    devices_info = basic.devices_long()
    print("Detailed device info:\n", devices_info)

    # Try to get root access (only succeeds on supported devices)
    # try:
    #     root_result = basic.root()
    #     print("adb root result:", root_result)
    # except Exception as root_err:
    #     print("Could not get root:", root_err)

    # Run a custom shell command
    wifi_status = basic.custom_command(adb.device_id, "shell dumpsys wifi | grep Wi-Fi")
    print("Wi-Fi Status:", wifi_status.strip())

    # Reboot the device (Careful!)
    # print("Rebooting device...")
    # basic.reboot()

except Exception as e:
    print(f"An error occurred: {e}")
```




### 5.4. `connect`: Manage Device Connections

This module handles establishing ADB connections to devices, especially over the network (Wi-Fi).

**Location:** `oiadb/commands/connect.py`

**Main Functions:**

*   **`connect_default(ip: str, port: int) -> str`:**
    *   **Description:** Performs a standard ADB connection to a device via IP address and port.
    *   **Parameters:**
        *   `ip`: The IP address of the Android device.
        *   `port`: The ADB port the device is listening on (usually 5555 after running `adb tcpip 5555`).
    *   **ADB Equivalent:** `adb connect <ip>:<port>`
    *   **Returns:** String output from the `adb connect` command (e.g., `connected to 192.168.1.100:5555` or `failed to connect to ...`).

*   **`connect_pair(ip: str, port: int, pairing_code: str) -> str`:**
    *   **Description:** Performs an ADB connection using the Wi-Fi pairing mechanism, typically required on Android 11 and above when "Wireless debugging" is enabled.
    *   **Parameters:**
        *   `ip`: The IP address of the device.
        *   `port`: The pairing port displayed on the device's "Wireless debugging" screen.
        *   `pairing_code`: The 6-digit pairing code displayed on the "Wireless debugging" screen.
    *   **ADB Equivalent:** `adb pair <ip>:<port> <pairing_code>`
    *   **Returns:** String output from the `adb pair` command (e.g., `Successfully paired to ...`). Note: This command only performs pairing; you still need to run `adb connect` (using the separate connection port) afterwards to actually connect the shell.

**Usage Example:**

```python
from oiadb import MyADB
from oiadb.commands import connect # Can be accessed directly if needed

# --- Regular Connection (after running adb tcpip 5555 on device via USB) ---
try:
    device_ip = "192.168.1.105" # Replace with actual IP
    connect_port = 5555
    print(f"Connecting to {device_ip}:{connect_port}...")
    result = connect.connect_default(device_ip, connect_port)
    print(f"Connection result: {result}")

    # After connecting, can initialize MyADB with IP:PORT as device_id
    # adb = MyADB(device_id=f"{device_ip}:{connect_port}")
    # print(f"Initialized MyADB for {adb.device_id}")
    # model = adb.run("shell getprop ro.product.model")
    # print(f"Model: {model.strip()}")

except Exception as e:
    print(f"Connection error: {e}")

# --- Connection using Pairing Code (Android 11+) ---
# try:
#     pair_ip = "192.168.1.108" # IP shown on Wireless Debugging screen
#     pair_port = 41234        # PAIRING port shown
#     pair_code = "123456"     # PAIRING code shown
#     connect_port_after_pair = 37890 # CONNECTION port shown (different from pairing port)

#     print(f"Pairing with {pair_ip}:{pair_port} using code {pair_code}...")
#     pair_result = connect.connect_pair(pair_ip, pair_port, pair_code)
#     print(f"Pairing result: {pair_result}")

#     if "Successfully paired" in pair_result:
#         print(f"Connecting to {pair_ip}:{connect_port_after_pair}...")
#         connect_result = connect.connect_default(pair_ip, connect_port_after_pair)
#         print(f"Connection result: {connect_result}")
#         # Initialize MyADB
#         # adb_paired = MyADB(device_id=f"{pair_ip}:{connect_port_after_pair}")
#         # print(f"Initialized MyADB for {adb_paired.device_id}")
#     else:
#         print("Pairing failed.")

# except Exception as e:
#     print(f"Pairing error: {e}")
```

**Important Note on Pairing:**

*   The pairing mechanism (`adb pair`) only establishes trust between the computer and the device.
*   After successful pairing, you **still must** use the `adb connect` command with the IP address and the **connection port** displayed on the "Wireless debugging" screen (this port is different from the pairing port) to actually establish the ADB session.
*   OIADB currently seems to provide the `connect_pair` function only for the pairing step. You need to manually call `connect_default` with the correct connection port after successful pairing.

### 5.5. `device_actions`: Device-Level Actions

This module includes commands that perform device-level actions such as rebooting into different modes, capturing/recording the screen, and backup/restore.

**Location:** `oiadb/commands/device_actions.py`

**Main Functions:**

*   **`reboot_recovery() -> str`:**
    *   **Description:** Reboots the device into Recovery mode.
    *   **ADB Equivalent:** `adb reboot recovery`
    *   **Returns:** String output from the command.

*   **`reboot_fastboot() -> str`:**
    *   **Description:** Reboots the device into Bootloader mode (often called Fastboot).
    *   **ADB Equivalent:** `adb reboot bootloader` (Note: The standard ADB command is `bootloader`, not `fastboot`. Check OIADB source or this might be a custom alias).
    *   **Returns:** String output from the command.

*   **`screencap(path: str) -> str`:**
    *   **Description:** Takes a screenshot and saves it directly to a path **on the device**.
    *   **Parameter:** `path`: Full path on the device to save the PNG image file (e.g., `/sdcard/screenshot.png`).
    *   **ADB Equivalent:** `adb shell screencap -p <path>`
    *   **Returns:** String output from the `screencap` command (usually empty on success).
    *   **Note:** This differs from `adb.take_screenshot()` (in the `MyADB` class), which pulls the image to the host computer.

*   **`screenrecord(path: str) -> str`:**
    *   **Description:** Starts recording the screen video and saves it to a path **on the device**. Recording continues until stopped (Ctrl+C in shell) or the default time limit is reached (usually 3 minutes).
    *   **Parameter:** `path`: Full path on the device to save the MP4 video file (e.g., `/sdcard/video.mp4`).
    *   **ADB Equivalent:** `adb shell screenrecord <path>` (Can add options like `--time-limit`, `--size`, `--bit-rate`).
    *   **Returns:** String output from the command. This command usually runs in the background, so managing the recording process needs separate handling (e.g., using `run_async` and `kill`).

*   **`backup_all(filename: str) -> str`:**
    *   **Description:** Creates a full backup of the device (including apps and their data) to a file on the local computer. Requires confirmation on the device screen.
    *   **Parameter:** `filename`: Path and filename on the computer to save the backup (e.g., `./my_backup.ab`).
    *   **ADB Equivalent:** `adb backup -apk -all -f <filename>` (The `-apk` option includes APK files, `-all` includes all apps).
    *   **Returns:** String output from the `adb backup` command.

*   **`restore_backup(filename: str) -> str`:**
    *   **Description:** Restores the device from a previously created backup file. Requires confirmation on the device screen.
    *   **Parameter:** `filename`: Path to the backup file (`.ab`) on the computer.
    *   **ADB Equivalent:** `adb restore <filename>`
    *   **Returns:** String output from the `adb restore` command.

*   **`start_activity(intent: str) -> str`:**
    *   **Description:** Launches an Activity using an Intent. Provides a more flexible way to launch app components compared to `apps.start_app`.
    *   **Parameter:** `intent`: String describing the Intent, including action, data, component, extras... (e.g., `-a android.intent.action.VIEW -d http://example.com`, `-n com.example.app/.MainActivity`).
    *   **ADB Equivalent:** `adb shell am start <intent_arguments>`
    *   **Returns:** String output from the `am start` command.

**Usage Example:**

```python
from oiadb import MyADB
from oiadb.commands import device_actions
import time
import os # Needed for os.path.exists

try:
    adb = MyADB()

    # Take screenshot and save on device
    device_path = "/sdcard/temp_screenshot.png"
    print(f"Taking screenshot and saving to {device_path}...")
    device_actions.screencap(device_path)
    # Check if file exists (example)
    ls_output = adb.run(f"shell ls {device_path}")
    if device_path in ls_output:
        print("Screenshot successful!")
        # Pull to computer if desired
        # adb.pull_file(device_path, "./device_screenshot.png")
        # Delete file on device
        adb.run(f"shell rm {device_path}")
    else:
        print("Screenshot failed.")

    # Launch browser with a URL
    print("Opening browser...")
    device_actions.start_activity("-a android.intent.action.VIEW -d https://www.google.com")

    # Backup (Requires confirmation on device!)
    # print("Starting backup, please confirm on device...")
    # backup_file = "full_backup.ab"
    # backup_result = device_actions.backup_all(backup_file)
    # print(f"Backup result: {backup_result}")

    # Reboot into recovery (Careful!)
    # print("Rebooting into Recovery...")
    # device_actions.reboot_recovery()

except Exception as e:
    print(f"An error occurred: {e}")
```

### 5.6. `device_info`: Collect Device Information

This module (often implemented within a class like `DeviceCommands`) provides methods to retrieve detailed information about the device's hardware, software, and current state.

**Location:** `oiadb/commands/device_info.py` (Often encapsulated in a class)

**Main Functions/Methods (within `DeviceCommands` class):**

*   **`get_state() -> str`:**
    *   **Description:** Gets the current connection state of the device relative to ADB.
    *   **ADB Equivalent:** `adb get-state`
    *   **Returns:** State string (`"device"`, `"offline"`, `"unknown"`, `"bootloader"`, `"recovery"`).

*   **`get_serialno() -> str`:**
    *   **Description:** Gets the unique serial number of the device.
    *   **ADB Equivalent:** `adb get-serialno`
    *   **Returns:** Serial number string.

*   **`get_imei() -> str`:**
    *   **Description:** Attempts to get the device's IMEI number. Note: The command `dumpsys iphonesybinfo` (used in the source) might not exist on all devices or Android versions, or may require special permissions. Retrieving IMEI is often restricted for security reasons.
    *   **ADB Equivalent:** `adb shell dumpsys iphonesybinfo` (Not a standard command, low reliability).
    *   **Returns:** IMEI string if successful, or error output.

*   **`battery() -> Dict[str, Any]`:**
    *   **Description:** Gets detailed battery information by parsing the output of `dumpsys battery`.
    *   **ADB Equivalent:** `adb shell dumpsys battery`
    *   **Returns:** Dictionary containing information like `level`, `status` (charging state), `health`, `temperature`, `voltage`, `technology`, etc.

*   **`current_dir() -> str`:**
    *   **Description:** Gets the current working directory within the ADB shell.
    *   **ADB Equivalent:** `adb shell pwd`
    *   **Returns:** Current directory path string.

*   **`list_features() -> List[str]`:**
    *   **Description:** Lists hardware and software features supported by the device (e.g., `android.hardware.camera`, `android.software.live_wallpaper`).
    *   **ADB Equivalent:** `adb shell pm list features`
    *   **Returns:** A list of feature strings.

*   **`get_all_props() -> Dict[str, str]`:**
    *   **Description:** Gets all system properties from the device.
    *   **ADB Equivalent:** `adb shell getprop`
    *   **Returns:** A dictionary where keys are property names and values are property values.

*   **`get_prop(prop_name: str) -> str`:**
    *   **Description:** Gets the value of a specific system property.
    *   **Parameter:** `prop_name`: The name of the property to retrieve (e.g., `"ro.product.model"`).
    *   **ADB Equivalent:** `adb shell getprop <prop_name>`
    *   **Returns:** The property value string.

*   **`get_device_model() -> str`:**
    *   **Description:** Convenience method to get the device model.
    *   **Implementation:** Calls `get_prop("ro.product.model")`.
    *   **Returns:** Device model string.

*   **`get_android_version() -> str`:**
    *   **Description:** Convenience method to get the Android OS version.
    *   **Implementation:** Calls `get_prop("ro.build.version.release")`.
    *   **Returns:** Android version string (e.g., "12", "13").

*   **`get_sdk_version() -> str`:**
    *   **Description:** Convenience method to get the Android SDK API level.
    *   **Implementation:** Calls `get_prop("ro.build.version.sdk")`.
    *   **Returns:** SDK version string (e.g., "31", "33").

*   **`get_screen_resolution() -> str`:**
    *   **Description:** Gets the physical screen resolution (width x height).
    *   **ADB Equivalent:** `adb shell wm size` (parses the "Physical size" line).
    *   **Returns:** Resolution string (e.g., "1080x1920").

*   **`get_screen_density() -> str`:**
    *   **Description:** Gets the physical screen density in DPI (dots per inch).
    *   **ADB Equivalent:** `adb shell wm density` (parses the "Physical density" line).
    *   **Returns:** Density string (e.g., "480").

*   **`get_ip_address() -> str`:**
    *   **Description:** Attempts to get the device's Wi-Fi IP address.
    *   **ADB Equivalent:** `adb shell ip route | awk '{print $9}'` (or similar `ip addr show wlan0` parsing).
    *   **Returns:** IP address string if connected via Wi-Fi, otherwise might be empty or show an error.

*   **`get_mac_address() -> str`:**
    *   **Description:** Attempts to get the device's Wi-Fi MAC address.
    *   **ADB Equivalent:** `adb shell ip addr show wlan0 | grep link/ether | awk '{print $2}'` (or parsing `/sys/class/net/wlan0/address`).
    *   **Returns:** MAC address string.

**Usage Example:**

```python
from oiadb import MyADB
from oiadb.commands import device_info # Often accessed via adb instance methods

try:
    adb = MyADB()

    state = device_info.get_state() # Or adb.get_state()
    serial = device_info.get_serialno() # Or adb.get_serialno()
    model = device_info.get_device_model() # Or adb.get_device_model()
    android_ver = device_info.get_android_version() # Or adb.get_android_version()
    sdk_ver = device_info.get_sdk_version() # Or adb.get_sdk_version()
    resolution = device_info.get_screen_resolution() # Or adb.get_screen_resolution()
    density = device_info.get_screen_density() # Or adb.get_screen_density()
    ip_addr = device_info.get_ip_address() # Or adb.get_ip_address()
    mac_addr = device_info.get_mac_address() # Or adb.get_mac_address()

    print(f"State: {state.strip()}")
    print(f"Serial: {serial.strip()}")
    print(f"Model: {model.strip()}")
    print(f"Android Version: {android_ver.strip()} (SDK: {sdk_ver.strip()})")
    print(f"Resolution: {resolution.strip()}")
    print(f"Density: {density.strip()} DPI")
    print(f"IP Address: {ip_addr.strip()}")
    print(f"MAC Address: {mac_addr.strip()}")

    # Get battery info
    batt_info = device_info.battery() # Or adb.battery()
    print("\nBattery Info:")
    for key, value in batt_info.items():
        print(f"  {key}: {value}")

    # Get all properties (can be large)
    # all_props = device_info.get_all_props() # Or adb.get_all_props()
    # print("\nAll Properties (first 10):")
    # count = 0
    # for key, value in all_props.items():
    #     print(f"  {key}: {value}")
    #     count += 1
    #     if count >= 10:
    #         break

except Exception as e:
    print(f"An error occurred: {e}")
```

### 5.7. `file_ops`: File System Operations

This module (often implemented within a class like `FileCommands`) provides functions for interacting with the file system on the Android device, including listing, creating, deleting, copying, moving, reading, and writing files and directories.

**Location:** `oiadb/commands/file_ops.py` (Often encapsulated in a class)

**Main Functions/Methods (within `FileCommands` class):**

*   **`list_files(remote_path: str, long_format: bool = False, all_files: bool = False) -> List[str]`:**
    *   **Description:** Lists files and directories at a given path on the device.
    *   **Parameters:**
        *   `remote_path`: The directory path on the device to list.
        *   `long_format` (bool): If `True`, uses `ls -l` for detailed output (permissions, owner, size, date).
        *   `all_files` (bool): If `True`, includes hidden files (starts with `.`), uses `ls -a`.
    *   **ADB Equivalent:** `adb shell ls [-l] [-a] <remote_path>`
    *   **Returns:** A list of strings, where each string is a file/directory name or a detailed line if `long_format=True`.

*   **`exists(remote_path: str) -> bool`:**
    *   **Description:** Checks if a file or directory exists at the specified path on the device.
    *   **Parameter:** `remote_path`: The path to check.
    *   **Implementation:** Typically uses `ls` and checks the output or return code.
    *   **Returns:** `True` if the path exists, `False` otherwise.

*   **`is_dir(remote_path: str) -> bool`:**
    *   **Description:** Checks if the specified path exists and is a directory.
    *   **Parameter:** `remote_path`: The path to check.
    *   **Implementation:** Often uses `ls -ld` and checks the first character of the permission string.
    *   **Returns:** `True` if the path is a directory, `False` otherwise.

*   **`is_file(remote_path: str) -> bool`:**
    *   **Description:** Checks if the specified path exists and is a regular file.
    *   **Parameter:** `remote_path`: The path to check.
    *   **Implementation:** Often uses `ls -ld` and checks the first character of the permission string.
    *   **Returns:** `True` if the path is a file, `False` otherwise.

*   **`mkdir(remote_path: str, parents: bool = False) -> str`:**
    *   **Description:** Creates a directory on the device.
    *   **Parameters:**
        *   `remote_path`: The directory path to create.
        *   `parents` (bool): If `True`, creates parent directories as needed (like `mkdir -p`).
    *   **ADB Equivalent:** `adb shell mkdir [-p] <remote_path>`
    *   **Returns:** String output from the `mkdir` command.
    *   **Raises:** `FileOperationError` on failure.

*   **`remove(remote_path: str, recursive: bool = False, force: bool = False) -> str`:**
    *   **Description:** Removes a file or directory on the device.
    *   **Parameters:**
        *   `remote_path`: The path to the file/directory to remove.
        *   `recursive` (bool): If `True`, removes directories and their contents recursively (`-r`).
        *   `force` (bool): If `True`, ignores non-existent files and never prompts for confirmation (`-f`).
    *   **ADB Equivalent:** `adb shell rm [-r] [-f] <remote_path>`
    *   **Returns:** String output from the `rm` command.
    *   **Raises:** `FileOperationError` on failure.

*   **`copy(source_path: str, dest_path: str) -> str`:**
    *   **Description:** Copies a file or directory from one location to another **on the same device**.
    *   **Parameters:**
        *   `source_path`: Source path on the device.
        *   `dest_path`: Destination path on the device.
    *   **ADB Equivalent:** `adb shell cp -r <source_path> <dest_path>` (Always uses `-r` to support directories).
    *   **Returns:** String output from the `cp` command.
    *   **Raises:** `FileOperationError` on failure.

*   **`move(source_path: str, dest_path: str) -> str`:**
    *   **Description:** Moves (or renames) a file or directory from one location to another **on the same device**.
    *   **Parameters:**
        *   `source_path`: Source path on the device.
        *   `dest_path`: Destination path on the device.
    *   **ADB Equivalent:** `adb shell mv <source_path> <dest_path>`
    *   **Returns:** String output from the `mv` command.
    *   **Raises:** `FileOperationError` on failure.

*   **`cat(remote_path: str) -> str`:**
    *   **Description:** Reads and returns the entire content of a text file on the device.
    *   **Parameter:** `remote_path`: Path to the file on the device.
    *   **ADB Equivalent:** `adb shell cat <remote_path>`
    *   **Returns:** String containing the file content.
    *   **Raises:** `FileOperationError` if reading fails.

*   **`write(remote_path: str, content: str) -> str`:**
    *   **Description:** Overwrites the content of a file on the device. This method works by creating a temporary file on the host, pushing it to the device, then using `cat` and redirection (`>`) to write the content to the target file.
    *   **Parameters:**
        *   `remote_path`: Path to the target file on the device.
        *   `content`: String content to write.
    *   **Returns:** String output from the `cat ... > ...` command.
    *   **Raises:** `FileOperationError` if writing fails.

*   **`append(remote_path: str, content: str) -> str`:**
    *   **Description:** Appends content to the end of a file on the device. Works similarly to `write` but uses append redirection (`>>`).
    *   **Parameters:**
        *   `remote_path`: Path to the target file on the device.
        *   `content`: String content to append.
    *   **Returns:** String output from the `cat ... >> ...` command.
    *   **Raises:** `FileOperationError` if appending fails.

*   **`chmod(remote_path: str, mode: str) -> str`:**
    *   **Description:** Changes the access permissions of a file or directory on the device.
    *   **Parameters:**
        *   `remote_path`: Path to the file/directory.
        *   `mode`: String representing the permissions in octal format (e.g., `"755"`, `"644"`) or symbolic format (e.g., `"u+x"`).
    *   **ADB Equivalent:** `adb shell chmod <mode> <remote_path>`
    *   **Returns:** String output from the `chmod` command.
    *   **Raises:** `FileOperationError` if changing permissions fails.

*   **`get_size(remote_path: str) -> int`:**
    *   **Description:** Gets the size of a file on the device in bytes.
    *   **Parameter:** `remote_path`: Path to the file.
    *   **ADB Equivalent:** `adb shell stat -c %s <remote_path>`
    *   **Returns:** Integer representing the file size (bytes).
    *   **Raises:** `FileOperationError` if getting size fails (e.g., file not found, not a file).

*   **`get_free_space(mount_point: str = "/data") -> int`:**
    *   **Description:** Gets the free space available on a specific partition (mount point) of the device.
    *   **Parameter:** `mount_point`: Path to the mount point (default is `/data`). Other common points: `/sdcard`, `/system`.
    *   **ADB Equivalent:** `adb shell df <mount_point>`
    *   **Returns:** Integer representing the free space in bytes.
    *   **Raises:** `FileOperationError` if getting free space info fails.

**Usage Example:**

```python
from oiadb import MyADB
from oiadb.commands import file_ops
from oiadb.exceptions import FileOperationError
import os # Needed for os.path.exists, os.remove

try:
    adb = MyADB()
    remote_dir = "/sdcard/oiadb_test_dir"
    remote_file = f"{remote_dir}/test_file.txt"
    local_file = "./local_copy.txt"

    # Create directory
    print(f"Creating directory {remote_dir}...")
    file_ops.mkdir(remote_dir, parents=True)

    # Check existence
    if file_ops.exists(remote_dir) and file_ops.is_dir(remote_dir):
        print("Directory created successfully.")
    else:
        print("Failed to create directory.")
        exit()

    # Write file
    content_to_write = "First line.\n"
    print(f"Writing to {remote_file}...")
    file_ops.write(remote_file, content_to_write)

    # Append to file
    content_to_append = "Second line.\n"
    print(f"Appending to {remote_file}...")
    file_ops.append(remote_file, content_to_append)

    # Read file content
    print(f"Reading content of {remote_file}...")
    read_content = file_ops.cat(remote_file)
    print(f"Content:\n{read_content}")

    # Get file size
    size = file_ops.get_size(remote_file)
    print(f"File size: {size} bytes")

    # Pull file to computer
    print(f"Pulling {remote_file} to {local_file}...")
    file_ops.pull(remote_file, local_file)
    if os.path.exists(local_file):
        print("File pulled successfully.")
        with open(local_file, "r") as f:
            print(f"Local file content:\n{f.read()}")
        os.remove(local_file) # Remove local file after checking
    else:
        print("Failed to pull file.")

    # List directory contents
    print(f"Contents of directory {remote_dir}:")
    files_list = file_ops.list_files(remote_dir)
    for item in files_list:
        print(f"- {item}")

    # Remove file and directory
    print(f"Removing {remote_file}...")
    file_ops.remove(remote_file)
    print(f"Removing {remote_dir}...")
    file_ops.remove(remote_dir, recursive=True)

    # Check existence again
    if not file_ops.exists(remote_dir):
        print("Cleanup successful.")
    else:
        print("Cleanup failed.")

except FileOperationError as e:
    print(f"File operation error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
```

### 5.8. `interaction`: Simulate User Interaction

This module (often implemented within a class like `InteractionCommands`) focuses on simulating user interaction actions on the device screen, such as tapping, swiping, typing, and pressing keys.

**Location:** `oiadb/commands/interaction.py` (Often encapsulated in a class)

**Main Functions/Methods (within `InteractionCommands` class):**

*   **`tap(x: int, y: int) -> str`:**
    *   **Description:** Simulates a tap at the specified (x, y) coordinates on the screen.
    *   **Parameters:**
        *   `x`: X coordinate.
        *   `y`: Y coordinate.
    *   **ADB Equivalent:** `adb shell input tap <x> <y>`
    *   **Returns:** String output from the command.

*   **`swipe(x1: int, y1: int, x2: int, y2: int, duration: int = 300) -> str`:**
    *   **Description:** Simulates a swipe gesture from point (x1, y1) to point (x2, y2) over a specified duration.
    *   **Parameters:**
        *   `x1`, `y1`: Starting coordinates.
        *   `x2`, `y2`: Ending coordinates.
        *   `duration`: Duration of the swipe gesture (in milliseconds, default 300ms).
    *   **ADB Equivalent:** `adb shell input swipe <x1> <y1> <x2> <y2> [duration]`
    *   **Returns:** String output from the command.

*   **`text_input(text: str) -> str`:**
    *   **Description:** Inputs a string of text into the currently focused input field on the device. Note: This command might not work with all keyboards or input fields, and special characters (like spaces, quotes) need proper escaping (OIADB source handles this).
    *   **Parameter:** `text`: The text string to input.
    *   **ADB Equivalent:** `adb shell input text '<escaped_text>'`
    *   **Returns:** String output from the command.

*   **`key_event(key_code: int) -> str`:**
    *   **Description:** Sends a key event to the device using a keycode. A list of keycodes can be found in the Android documentation (KeyEvent).
    *   **Parameter:** `key_code`: Integer code of the key (e.g., 4 for BACK, 3 for HOME, 66 for ENTER).
    *   **ADB Equivalent:** `adb shell input keyevent <key_code>`
    *   **Returns:** String output from the command.

*   **Convenience functions for `key_event`:**
    *   `back() -> str`: Sends keycode 4 (Back button).
    *   `home() -> str`: Sends keycode 3 (Home button).
    *   `menu() -> str`: Sends keycode 82 (Menu button - may not work on newer devices).
    *   `power() -> str`: Sends keycode 26 (Power button).
    *   `volume_up() -> str`: Sends keycode 24 (Volume Up).
    *   `volume_down() -> str`: Sends keycode 25 (Volume Down).
    *   `enter() -> str`: Sends keycode 66 (Enter key).
    *   `tab() -> str`: Sends keycode 61 (Tab key).
    *   `delete() -> str`: Sends keycode 67 (Delete/Backspace key).
    *   `recent_apps() -> str`: Sends keycode 187 (Show recent apps).

*   **`long_press(x: int, y: int, duration: int = 1000) -> str`:**
    *   **Description:** Simulates a long press at coordinates (x, y) for a specified duration. Implemented by calling `swipe` with identical start and end points.
    *   **Parameters:**
        *   `x`, `y`: Coordinates for the long press.
        *   `duration`: Duration of the press (milliseconds, default 1000ms).
    *   **Returns:** String output from the corresponding swipe command.

*   **`pinch(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int, duration: int = 500) -> Tuple[str, str]`:**
    *   **Description:** Simulates a two-finger pinch gesture. Requires start and end coordinates for both "fingers". Implemented by running two `swipe` commands in parallel (or near-parallel).
    *   **Parameters:**
        *   `(x1, y1)`: Start point finger 1.
        *   `(x2, y2)`: End point finger 1.
        *   `(x3, y3)`: Start point finger 2.
        *   `(x4, y4)`: End point finger 2.
        *   `duration`: Duration of the gesture (milliseconds).
    *   **Returns:** A tuple containing the output results of the two swipe commands.

*   **`zoom_in(center_x: int, center_y: int, distance: int = 200, duration: int = 500) -> Tuple[str, str]`:**
    *   **Description:** Convenience function to simulate a zoom-in gesture around a center point. Implemented by calling `pinch` with calculated coordinates to move two fingers away from near the center.
    *   **Parameters:**
        *   `center_x`, `center_y`: Center coordinates for zooming.
        *   `distance`: How far each finger moves (total distance increases by double this).
        *   `duration`: Duration of the gesture.
    *   **Returns:** A tuple containing the output results of the two swipe commands.

*   **`zoom_out(center_x: int, center_y: int, distance: int = 200, duration: int = 500) -> Tuple[str, str]`:**
    *   **Description:** Convenience function to simulate a zoom-out gesture around a center point. Implemented by calling `pinch` with calculated coordinates to move two fingers towards the center.
    *   **Parameters:** Same as `zoom_in`.
    *   **Returns:** A tuple containing the output results of the two swipe commands.

*   **`drag(x1: int, y1: int, x2: int, y2: int, duration: int = 1000) -> str`:**
    *   **Description:** Simulates dragging an object from point (x1, y1) to (x2, y2). Essentially the same as `swipe` but often with a longer default `duration`.
    *   **Parameters:** Same as `swipe`, default `duration` is 1000ms.
    *   **Returns:** String output from the corresponding swipe command.

*   **Convenience functions for `swipe` (scrolling):**
    *   `scroll_up(distance: int = 500, duration: int = 500) -> str`: Scrolls up by `distance` pixels.
    *   `scroll_down(distance: int = 500, duration: int = 500) -> str`: Scrolls down by `distance` pixels.
    *   `scroll_left(distance: int = 500, duration: int = 500) -> str`: Scrolls left by `distance` pixels.
    *   `scroll_right(distance: int = 500, duration: int = 500) -> str`: Scrolls right by `distance` pixels.
    *   **Note:** These scroll functions attempt to get the screen size to calculate swipe coordinates in the middle of the screen. If getting the size fails, they use default values.

*   **`type_keycode_sequence(keycodes: List[int]) -> List[str]`:**
    *   **Description:** Sends a sequence of key events in order.
    *   **Parameter:** `keycodes`: A list of keycodes to send.
    *   **Returns:** A list of string outputs from each `key_event` command.

*   **`wake_up() -> str`:**
    *   **Description:** Wakes the device if it's asleep.
    *   **ADB Equivalent:** `adb shell input keyevent KEYCODE_WAKEUP` (or 224).
    *   **Returns:** String output from the command.

*   **`sleep() -> str`:**
    *   **Description:** Puts the device to sleep (turns off the screen).
    *   **ADB Equivalent:** `adb shell input keyevent KEYCODE_SLEEP` (or 223).
    *   **Returns:** String output from the command.

*   **`unlock(pattern: Optional[List[int]] = None, pin: Optional[str] = None) -> str`:**
    *   **Description:** Attempts to unlock the device screen. It first wakes the device and swipes up to dismiss the basic lock screen. Then, if a `pattern` or `pin` is provided, it attempts to input them.
    *   **Parameters:**
        *   `pattern`: A list of integers from 1-9 representing the points in the unlock pattern.
        *   `pin`: The PIN code string.
    *   **Returns:** The result of the last PIN input or pattern swipe command.
    *   **Note:** Calculating coordinates for the pattern relies on screen size and might not be perfectly accurate on all devices. Unlocking with more complex PINs/passwords might require `text_input` and `enter` commands.

**Usage Example:**

```python
from oiadb import MyADB
from oiadb.commands import interaction
import time

try:
    adb = MyADB()

    # Wake up and basic unlock
    print("Waking up and basic unlock...")
    interaction.unlock()
    time.sleep(1)

    # Open Settings app (example)
    print("Opening Settings app...")
    adb.run("shell am start -n com.android.settings/.Settings")
    time.sleep(2)

    # Get screen size for coordinate calculation
    size = adb.get_screen_size()
    width, height = size.get("width", 1080), size.get("height", 1920)

    # Scroll down
    print("Scrolling down...")
    interaction.scroll_down(distance=height // 2, duration=500)
    time.sleep(1)

    # Tap somewhere near the middle (example)
    tap_x, tap_y = width // 2, height // 2
    print(f"Tapping at ({tap_x}, {tap_y})...")
    interaction.tap(tap_x, tap_y)
    time.sleep(1)

    # Input text (e.g., into a search box if available)
    # print("Typing 'Wi-Fi'...")
    # interaction.text_input("Wi-Fi")
    # time.sleep(0.5)
    # interaction.enter()
    # time.sleep(2)

    # Press Back button
    print("Pressing Back...")
    interaction.back()
    time.sleep(1)

    # Press Home button
    print("Pressing Home...")
    interaction.home()

except Exception as e:
    print(f"An error occurred: {e}")
```




### 5.9. `image_interaction`: Interaction Based on Image Recognition

This module (often implemented within a class like `ImageInteractionCommands`) extends interaction capabilities by allowing searching for and manipulating elements on the screen based on template images, rather than fixed coordinates. This is very useful for automating complex or dynamic graphical user interfaces (GUIs).

**Location:** `oiadb/commands/image_interaction.py` (Often encapsulated in a class, utilizing `oiadb.utils.image_recognition`)

**Main Functions/Methods (within `ImageInteractionCommands` class):**

*   **`find_image(template_path: str, threshold: float = 0.8, region: Optional[Tuple[int, int, int, int]] = None, save_screenshot: Optional[str] = None, use_gray: bool = False, use_canny: bool = False, scale_range: Optional[Tuple[float, float]] = None, scale_steps: int = 10, rotation_range: Optional[Tuple[int, int]] = None, rotation_steps: int = 10) -> Optional[Tuple[int, int, int, int, float]]`:**
    *   **Description:** Searches for a template image (from a local file) on the device's current screen.
    *   **Parameters:**
        *   `template_path`: Path to the template image file on the host computer.
        *   `threshold` (float): Confidence threshold (0.0 to 1.0) for matching. Higher values mean stricter matching (default 0.8).
        *   `region` (Optional): A tuple `(x, y, width, height)` defining the screen area to search within. If `None`, searches the entire screen.
        *   `save_screenshot` (Optional): Path to save the device screenshot used for the search (useful for debugging).
        *   `use_gray` (bool): Convert both screenshot and template to grayscale before matching (can improve robustness to color variations).
        *   `use_canny` (bool): Apply Canny edge detection before matching (can be useful for icons or elements with clear outlines, may ignore color/texture).
        *   `scale_range` (Optional): Tuple `(min_scale, max_scale)` to search for the template at different sizes (e.g., `(0.8, 1.2)`).
        *   `scale_steps` (int): Number of scales to check within the `scale_range`.
        *   `rotation_range` (Optional): Tuple `(min_angle, max_angle)` to search for rotated versions of the template.
        *   `rotation_steps` (int): Number of angles to check within the `rotation_range`.
    *   **Returns:** A tuple `(x, y, width, height, confidence)` representing the bounding box and confidence score of the best match found, or `None` if no match exceeds the threshold.
    *   **Raises:** `ImageNotFoundError` if the template file doesn't exist, `ADBError` if screenshot fails.

*   **`wait_for_image(template_path: str, timeout: int = 10, interval: float = 0.5, **kwargs) -> Optional[Tuple[int, int, int, int, float]]`:**
    *   **Description:** Repeatedly searches for a template image until it's found or a timeout occurs.
    *   **Parameters:**
        *   `template_path`: Path to the template image file.
        *   `timeout` (int): Maximum time (in seconds) to wait for the image.
        *   `interval` (float): Time (in seconds) to wait between search attempts.
        *   `**kwargs`: Additional keyword arguments passed directly to `find_image` (e.g., `threshold`, `region`).
    *   **Returns:** The result tuple from `find_image` if found, `None` if timed out.

*   **`tap_image(template_path: str, **kwargs) -> bool`:**
    *   **Description:** Finds a template image on the screen and simulates a tap at its center.
    *   **Parameters:**
        *   `template_path`: Path to the template image file.
        *   `**kwargs`: Additional keyword arguments passed directly to `find_image` (e.g., `threshold`, `region`).
    *   **Returns:** `True` if the image was found and tapped, `False` otherwise.

*   **`swipe_image(start_template_path: str, end_template_path: str, duration: int = 300, **kwargs) -> bool`:**
    *   **Description:** Finds two template images (start and end points) and simulates a swipe gesture between their centers.
    *   **Parameters:**
        *   `start_template_path`: Path to the template image for the swipe start point.
        *   `end_template_path`: Path to the template image for the swipe end point.
        *   `duration` (int): Duration of the swipe (milliseconds).
        *   `**kwargs`: Additional keyword arguments passed directly to `find_image` for *both* images.
    *   **Returns:** `True` if both images were found and the swipe was performed, `False` otherwise.

*   **`swipe_image_relative(template_path: str, dx: int, dy: int, duration: int = 300, **kwargs) -> bool`:**
    *   **Description:** Finds a template image and performs a swipe starting from its center by a relative offset (`dx`, `dy`).
    *   **Parameters:**
        *   `template_path`: Path to the template image.
        *   `dx`: Horizontal offset for the swipe end point.
        *   `dy`: Vertical offset for the swipe end point.
        *   `duration` (int): Duration of the swipe (milliseconds).
        *   `**kwargs`: Additional keyword arguments passed to `find_image`.
    *   **Returns:** `True` if the image was found and the swipe was performed, `False` otherwise.

**Usage Example:**

```python
from oiadb import MyADB
from oiadb.commands import image_interaction
import time
import os

# Assume you have template images like 'settings_icon.png', 'wifi_icon.png'
# in a directory './templates/'
TEMPLATE_DIR = "./templates"
SETTINGS_ICON = os.path.join(TEMPLATE_DIR, "settings_icon.png")
WIFI_ICON = os.path.join(TEMPLATE_DIR, "wifi_icon.png")

# Create dummy template files for example to run
if not os.path.exists(TEMPLATE_DIR):
    os.makedirs(TEMPLATE_DIR)
if not os.path.exists(SETTINGS_ICON):
    with open(SETTINGS_ICON, "w") as f: f.write("dummy") 
if not os.path.exists(WIFI_ICON):
    with open(WIFI_ICON, "w") as f: f.write("dummy")

try:
    adb = MyADB()
    adb.home() # Go to home screen
    time.sleep(1)

    # Find the settings icon (replace with a real icon path)
    print(f"Searching for {SETTINGS_ICON}...")
    # Note: This will likely fail without a real screenshot/template setup
    # match = image_interaction.find_image(SETTINGS_ICON, threshold=0.7, save_screenshot="./debug_screen.png")
    match = None # Simulate not found for now

    if match:
        x, y, w, h, conf = match
        print(f"Found settings icon at ({x}, {y}) with confidence {conf:.2f}")
        
        # Tap the settings icon
        print("Tapping settings icon...")
        if image_interaction.tap_image(SETTINGS_ICON, threshold=0.7):
            print("Tapped successfully.")
            time.sleep(2)

            # Wait for Wi-Fi icon inside settings (replace with real icon)
            print(f"Waiting for {WIFI_ICON}...")
            # wifi_match = image_interaction.wait_for_image(WIFI_ICON, timeout=5, threshold=0.75)
            wifi_match = None # Simulate not found
            
            if wifi_match:
                print("Found Wi-Fi icon.")
                # Tap Wi-Fi icon
                image_interaction.tap_image(WIFI_ICON, threshold=0.75)
            else:
                print("Wi-Fi icon not found within timeout.")
        else:
            print("Failed to tap settings icon.")
    else:
        print("Settings icon not found. (Note: Example requires real images)")

    adb.home()

except FileNotFoundError as e:
    print(f"Error: Template image not found - {e}. Please create template images.")
except Exception as e:
    print(f"An error occurred: {e}")

# Clean up dummy files
# os.remove(SETTINGS_ICON)
# os.remove(WIFI_ICON)
# if os.path.exists("./debug_screen.png"): os.remove("./debug_screen.png")
# if os.path.exists(TEMPLATE_DIR): os.rmdir(TEMPLATE_DIR)
```

**Important Considerations for Image Recognition:**

*   **Performance:** Image recognition is computationally intensive. It involves taking a screenshot, transferring it, and performing image processing. Use it judiciously.
*   **Reliability:** Matches can be affected by screen resolution changes, themes, notifications popping up, animations, or slight variations in icons/UI elements.
*   **Template Quality:** Use clear, unique, and appropriately sized template images. Avoid templates that are too small or too generic.
*   **Threshold Tuning:** Finding the right `threshold` is key. Too high, and you miss valid matches; too low, and you get false positives.
*   **Alternatives:** For more robust UI automation, consider using UI inspection tools (like `uiautomatorviewer` or `adb shell uiautomator dump`) combined with OIADB's XML dump features (if available) or coordinate-based interaction when possible.

---

## 6. Utilities Module - Advanced Features and Helpers

The `utils` module provides various helper classes and functions that support the core functionality of OIADB or offer advanced capabilities.

**Location:** `oiadb/utils/`

### 6.1. `image_recognition`: Image Search Engine

This is the core engine used by `image_interaction` commands. It leverages the `opencv-python` library (specifically `cv2`) to perform template matching on screenshots.

**Location:** `oiadb/utils/image_recognition.py`

**Main Class:** `ImageRecognition`

*   **`__init__(adb_instance: MyADB)`:** Initializes with a `MyADB` instance to take screenshots.
*   **`find_template(...)`:** The primary method that takes a screenshot, loads the template, performs `cv2.matchTemplate` (using `TM_CCOEFF_NORMED`), finds the location of the best match, and returns coordinates and confidence if the threshold is met. It also handles grayscale conversion, Canny edge detection, scaling, and rotation based on input parameters.
*   **Helper methods:** Include functions for taking screenshots, loading/preprocessing images, applying transformations (scale, rotate), and finding the best match location from the result matrix.

### 6.2. `advanced`: Asynchronous Execution, Monitoring, Caching

This module contains utilities for more complex scenarios like running commands in the background, monitoring device connections, and caching command results.

**Location:** `oiadb/utils/advanced.py`

**Key Classes:**

*   **`CommandResult`:** A simple data class (or named tuple) to store the results of an executed command, including `command` (list), `success` (bool), `return_code` (int), `stdout` (str), and `stderr` (str).

*   **`AsyncCommandExecutor`:**
    *   **Description:** Manages the execution of ADB commands asynchronously using Python's `threading` and `subprocess.Popen`. Allows running multiple commands concurrently without blocking the main program flow.
    *   **Main Methods:**
        *   `execute(command_id: str, command: List[str], callback: Optional[Callable[[CommandResult], None]] = None)`: Starts executing a command in a separate thread. Takes a unique `command_id`, the command as a list of strings, and an optional `callback` function to be called upon completion.
        *   `is_running(command_id: str) -> bool`: Checks if the command with the given ID is still running.
        *   `get_result(command_id: str) -> Optional[CommandResult]`: Retrieves the `CommandResult` for a completed command. Returns `None` if the command is still running or the ID is invalid.
        *   `stop_command(command_id: str)`: Attempts to terminate the running process associated with the command ID.
        *   `stop_all()`: Stops all currently running asynchronous commands.

*   **`DeviceMonitor`:**
    *   **Description:** Runs a background thread to periodically check the list of connected devices (`adb devices`) and notifies about newly connected or disconnected devices.
    *   **Main Methods:**
        *   `start()`: Starts the monitoring thread.
        *   `stop()`: Stops the monitoring thread.
        *   `add_callback(callback)`: Registers a callback function to be invoked on device change events. The callback receives two arguments: `device_id` (str) and `event_type` (str, either `'connected'` or `'disconnected'`).

*   **`ResultCache`:**
    *   **Description:** A simple in-memory cache to store results of frequently used ADB commands (e.g., `getprop`). Helps reduce redundant command executions and improve performance.
    *   **Main Methods:**
        *   `__init__(max_size=100, ttl=60)`: Initializes the cache with a maximum number of items (`max_size`) and a time-to-live (`ttl`, in seconds) for each entry.
        *   `get(key)`: Retrieves a value from the cache based on the `key`. Returns `None` if the key is not found or the entry has expired.
        *   `set(key, value)`: Stores a `key-value` pair in the cache.
        *   `clear()`: Removes all entries from the cache.
        *   `remove(key)`: Removes a specific entry from the cache.

**Usage Example (AsyncCommandExecutor):**

```python
from oiadb import MyADB
from oiadb.utils.advanced import AsyncCommandExecutor, CommandResult
import time
import uuid

def my_callback(result: CommandResult):
    print(f"\n--- Command '{' '.join(result.command)}' finished --- ({result.command_id})")
    if result.success:
        print(f"Output:\n{result.stdout[:200]}...") # Print first 200 chars
    else:
        print(f"Error:\n{result.stderr}")

executor = AsyncCommandExecutor()
try:
    adb = MyADB() # Assumes device is connected

    # Run ls command asynchronously
    cmd_id_ls = str(uuid.uuid4())
    print(f"Running ls (ID: {cmd_id_ls})...")
    # Note: Pass command as a list for subprocess
    executor.execute(cmd_id_ls, 
                     ["adb", "-s", adb.device_id, "shell", "ls", "-l", "/sdcard/"], 
                     callback=my_callback)

    # Run screenrecord asynchronously for 5 seconds
    cmd_id_rec = str(uuid.uuid4())
    remote_video_path = "/sdcard/async_record.mp4"
    print(f"Running screenrecord 5s (ID: {cmd_id_rec})...")
    executor.execute(cmd_id_rec, 
                     ["adb", "-s", adb.device_id, "shell", "screenrecord", "--time-limit", "5", remote_video_path],
                     callback=my_callback)

    # Do other work while commands run...
    print("Waiting for commands to complete...")
    start_time = time.time()
    while executor.is_running(cmd_id_ls) or executor.is_running(cmd_id_rec):
        print("." if executor.is_running(cmd_id_ls) else " ", end="", flush=True)
        print("+" if executor.is_running(cmd_id_rec) else " ", end="", flush=True)
        time.sleep(0.5)
        if time.time() - start_time > 15: # Add a timeout for the wait loop
            print("\nWait loop timed out!")
            break

    print("\nAll async commands finished (or were stopped/timed out).")

    # Get results (if needed)
    ls_result = executor.get_result(cmd_id_ls)
    rec_result = executor.get_result(cmd_id_rec)

    # Clean up video file on device
    if rec_result and rec_result.success:
        try:
            adb.run(f"shell rm {remote_video_path}")
            print(f"Deleted {remote_video_path}")
        except Exception as e:
            print(f"Error deleting video: {e}")

finally:
    # Ensure all processes are stopped on exit
    executor.stop_all()
    print("Stopped async executor.")

```

**Usage Example (DeviceMonitor):**

```python
from oiadb.utils.advanced import DeviceMonitor
import time

def device_event_handler(device_id, event_type):
    print(f"Event: Device {device_id} just {event_type}.")

monitor = DeviceMonitor()
monitor.add_callback(device_event_handler)

print("Starting device monitoring (Press Ctrl+C to stop)...")
monitor.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopping monitoring...")
    monitor.stop()
    print("Stopped.")
```

### 6.3. Other Utilities

*   **`platform_utils`:** Contains functions to detect the host operating system (Windows, macOS, Linux) which helps in determining correct paths or commands (e.g., for finding/downloading ADB).
*   **`adb_manager`:** Handles finding the ADB executable in the system PATH, validating a user-provided path, or automatically downloading the platform-specific ADB tools if needed and permitted (`auto_install_adb=True`).
*   **`runner`:** A core utility responsible for actually executing the ADB commands using `subprocess.run` (for synchronous execution). It handles constructing the full command string (including `adb -s <device_id>`), setting the timeout, capturing stdout/stderr, checking the return code, and raising `ADBCommandError` on failure.

---

## 7. Contribution Guidelines

We welcome and encourage all contributions to improve OIADB! Whether it's reporting bugs, suggesting new features, improving documentation, or writing code, your involvement is valuable.

### 7.1. Reporting Bugs

If you encounter a bug while using OIADB, please check the existing Issues on the GitHub repository [https://github.com/tiendung2k03/oiadb/issues](https://github.com/tiendung2k03/oiadb/issues) to see if the bug has already been reported.

If not, please create a new Issue with the following information:

*   **Clear Title:** Briefly describe the bug.
*   **OIADB Version:** The version you are using (`pip show oiadb`).
*   **Python Version:** The Python version you are using (`python --version`).
*   **Operating System:** Your host OS (Windows, macOS, Linux).
*   **Android Device Info:** Device model, Android version.
*   **Steps to Reproduce:** Detail the exact steps needed to trigger the bug.
*   **Expected Behavior:** What should have happened.
*   **Actual Behavior:** What actually happened.
*   **Full Error Messages/Traceback:** Copy and paste the complete error message or traceback.
*   **Screenshots/Videos (if applicable):** Visual aids are very helpful.

### 7.2. Suggesting Enhancements

If you have an idea for a new feature or an improvement for OIADB:

1.  Check the open Issues and Pull Requests to see if the idea has already been suggested or is being worked on.
2.  If not, create a new Issue with the `enhancement` label.
3.  Describe the proposed feature in detail:
    *   The problem the feature solves.
    *   How the feature would work (desired behavior).
    *   Usage examples (if possible).
    *   Why you think this feature would be beneficial to the community.

### 7.3. Contributing Code

If you'd like to contribute code, please follow this process:

1.  **Fork the Repository:** Create a fork of the `tiendung2k03/oiadb` repository to your GitHub account.
2.  **Clone Your Fork:** Clone your fork to your local machine:
    ```bash
    git clone https://github.com/YOUR_USERNAME/oiadb.git
    cd oiadb
    ```
3.  **Create a New Branch:** Create a new branch for your changes. Use a descriptive branch name, e.g., `feature/add-new-command` or `fix/resolve-issue-123`.
    ```bash
    git checkout -b feature/your-feature-name
    ```
4.  **Develop and Test:**
    *   Write the code for the new feature or bug fix.
    *   Adhere to the project's existing coding style (e.g., PEP 8 for Python).
    *   Add new tests for your changes if applicable.
    *   Ensure all existing tests pass.
    *   Update documentation (README, docstrings) as necessary.
5.  **Commit Changes:** Commit your changes with clear and descriptive commit messages.
    ```bash
    git add .
    git commit -m "feat: Add feature X that does Y" 
    # Or "fix: Resolve issue Z by doing W"
    ```
6.  **Push Branch to Fork:** Push your new branch to your fork on GitHub.
    ```bash
    git push origin feature/your-feature-name
    ```
7.  **Create a Pull Request (PR):**
    *   Go to your forked repository on GitHub.
    *   Click the "Compare & pull request" button.
    *   Set the base branch to `main` (or the primary development branch) of the `tiendung2k03/oiadb` repository.
    *   Set the compare branch to the one you just pushed (`feature/your-feature-name`).
    *   Write a clear title and description for the PR, explaining the changes and their purpose.
    *   If your PR addresses a specific Issue, link it (e.g., `Closes #123`).
    *   Submit the Pull Request.

8.  **Review and Merge:** Project maintainers will review your PR, potentially request changes, or discuss further. Once approved, the PR will be merged into the main repository.

### 7.4. Coding Style

*   **Python:** Follow the [PEP 8 Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/). Using formatters like `black` and linters like `flake8` is encouraged.
*   **Docstrings:** Use Google Style or reStructuredText format for docstrings to describe classes, methods, and functions.
*   **Commit Messages:** Write clear, concise commit messages, ideally following the [Conventional Commits](https://www.conventionalcommits.org/) specification.

Thank you for your interest in contributing to OIADB!

---

## 8. Troubleshooting & FAQ

This section provides solutions to common problems and answers frequently asked questions when using ADB and the OIADB library.

### 8.1. Device Connection Issues

*   **Problem:** `adb devices` shows the device as `offline` or `unauthorized`.
    *   **Solution (`offline`):**
        *   Check the USB cable and port. Try a different cable/port.
        *   Reboot the device and the computer.
        *   Run `adb kill-server` followed by `adb start-server`.
        *   On the device, go to Developer Options, toggle USB Debugging off and on again.
    *   **Solution (`unauthorized`):**
        *   Ensure you have authorized USB debugging from this computer on the device screen (a dialog should pop up asking to confirm the RSA fingerprint).
        *   If you don't see the dialog, go to Developer Options, select "Revoke USB debugging authorizations," then reconnect the device.
        *   Double-check the USB cable and port.

*   **Problem:** Cannot connect via Wi-Fi (`adb connect <ip>:<port>`).
    *   **Solution:**
        *   Ensure the device and computer are on the same Wi-Fi network.
        *   Verify that USB Debugging and Wireless Debugging (or `adb tcpip 5555` run via USB first) are enabled on the device.
        *   Confirm the device's IP address and port are correct.
        *   Firewalls on the computer or router might block the connection. Try temporarily disabling the firewall for testing.
        *   For Android 11+, use the pairing mechanism (`connect.connect_pair`) if direct connection fails (see section 5.4).

### 8.2. OIADB Command Execution Errors

*   **Problem:** Receiving `ADBCommandError` or `FileOperationError` exceptions.
    *   **Solution:**
        *   Read the error message (`e.stderr` or `e.error_message`) carefully to understand the cause.
        *   Check if the equivalent ADB command runs successfully directly in the terminal. E.g., if `file_ops.pull("/sdcard/file.txt", "./file.txt")` fails, try `adb pull /sdcard/file.txt ./file.txt`.
        *   Ensure file/directory paths on the device and host computer are correct.
        *   Check permissions. Some commands (`setprop`, `rm /system/...`) require root access (`adb root`). Some file operations might be blocked by app permissions or SELinux.
        *   For `FileOperationError` during `push` or `pull`, check available storage space on the device and computer.

*   **Problem:** Interaction commands (`tap`, `swipe`, `text_input`) don't work as expected.
    *   **Solution:**
        *   Coordinates (x, y) might be incorrect. Use Developer Options > Show pointer location to find the correct coordinates.
        *   `text_input` might not work with certain keyboards or apps. Try using `key_event` to simulate typing individual characters (more complex).
        *   Ensure the device screen is on and unlocked when executing interaction commands.

*   **Problem:** Image recognition (`find_image`, `tap_image`) fails to find the template image.
    *   **Solution:**
        *   **Template Quality:** Ensure the template image is clear, not blurry, and accurately matches the element on the screen.
        *   **Threshold (`threshold`):** Try lowering the `threshold` value (e.g., 0.7 or 0.65) if the on-screen image might slightly differ from the template. However, setting it too low can cause false positives.
        *   **Search Region (`region`):** If you know the image only appears in a specific area, specify the `region` to speed up the search and improve accuracy.
        *   **Scaling (`scale_range`):** If the on-screen image size might vary, adjust `scale_range` and `scale_steps`.
        *   **Rotation (`rotation_range`):** If the image might be rotated, experiment with `rotation_range`.
        *   **Grayscale (`use_gray`) and Canny (`use_canny`):** Try toggling these options. `use_canny=True` can be helpful for blurry images or icons with distinct edges.
        *   **Debug Screenshot:** Use the `save_screenshot` parameter in `find_image` to capture the device screen at the time of the search and manually compare it with your template.

### 8.3. Frequently Asked Questions (FAQ)

*   **Q:** How do I run ADB commands for a specific device if multiple are connected?
    *   **A:** Initialize the `MyADB` object with the specific `device_id`: `adb = MyADB(device_id="YOUR_DEVICE_SERIAL_OR_IP")`. All subsequent commands from this instance will target that device. Alternatively, use `basic.custom_command(device_id, command)`.

*   **Q:** Does OIADB support Fastboot commands?
    *   **A:** Based on the current documentation, OIADB primarily focuses on ADB commands. While it has `reboot_bootloader` (or `reboot_fastboot`), the library doesn't provide dedicated Fastboot commands (like `fastboot devices`, `fastboot flash`, `fastboot boot`). You would need to use the separate `fastboot` tool for those.

*   **Q:** How to handle ADB commands that require user interaction (e.g., confirming backup on screen)?
    *   **A:** OIADB (and ADB in general) cannot automate interactions that require physical confirmation on the device screen. You need to manually confirm on the device when commands like `backup` or `restore` are running.

*   **Q:** Is the library compatible with all Android versions?
    *   **A:** Most basic ADB commands work across many Android versions. However, some commands (`dumpsys`, `wm`, `pm grant/revoke`, Wireless Debugging) might have different syntax or behavior between versions. Always test on your target devices.

*   **Q:** How do I install OIADB?
    *   **A:** Use pip: `pip install oiadb`.

---

