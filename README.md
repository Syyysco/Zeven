<p align="center">
  <img src="src/doc/banner.png" alt="Zeven - A powerful code booster"><br>
  <img src="https://img.shields.io/badge/%20-python-blue?logo=python&logoColor=white&labelColor=2c2c2c" alt="Build Status"></a>
  <img src="https://img.shields.io/badge/license-GPL-purple?logo=gnuprivacyguard" alt="license">
  <img src="https://img.shields.io/github/last-commit/Syyysco/Zeven?colorB=319e8c" alt="Last Commit">
  <img src="https://img.shields.io/badge/platforms-MacOS%20%7C%20Linux%20%7C%20Windows-white" alt="Available on all Platforms">
  <img src="https://img.shields.io/badge/console%20tool-text?logo=zsh&logoColor=lightblue&label=&labelColor=gray&color=2c2c2c" alt="Tool Type"><br>
  A <i>Zeven</i> lifes for advanced developers.
</p>

<p align="center">
  [English]
  [<a href="doc/README-zh.md">中文</a>]
  [<a href="doc/README-ja.md">日本語</a>]
  [<a href="doc/README-ko.md">한국어</a>]
  [<a href="doc/README-ru.md">Русский</a>]<br><br>

</p>
<p align="center">
  <a href="#key-features-and-overview">Key features and overview</a><br>
  <a href="#installation-for-windows">Installation for Windows</a><br>
  <a href="#installation-for-linux-and-macos">Installation for Linux and MacOS</a><br>
  <a href="#how-to-use">How to use</a><br>
  <a href="#using-setting-mode">Using setting mode</a><br>
  <a href="#setting-mode-configuration">Setting mode: Configuration</a><br>
  <a href="#setting-mode-customization">Setting mode: Customization</a><br>
  <a href="#available-languages">Available languajes</a><br>
  <a href="#parameters-cheatsheet">Parameters cheatsheet</a><br>
  <a href="#possible-errors">Possible errors</a><br>
  <a href="#about-compacting-projects">About compacting projects</a><br>
  <a href="#about-formatting-projects">About formatting projects</a><br>
  <a href="#for-developers-and-contributors">For developers and contributors</a><br>
  <a href="#project-goals-and-future-ideas">Project goals and future ideas</a><br>
  <a href="src/doc/license.html">License</a><br>
</p><br>

---

<br>


# Key Features and Overview
**Zeven** is a command-line tool designed to efficiently format and/or compact code, making it more readable and maintainable, or alternatively reducing its size and processing time.

- Compatible with Windows, Linux, and macOS
- Supports multiple specific formats
- Allows custom configurations
- Extremely fast for large projects
- Parallel execution with threads to maximize performance
- Includes an interactive configuration mode for ease of use
- Particularly useful for web projects

> Designed as an open-source project, focused on optimization and accessibility for developers and teams.
> 
> 100% Built with Python

<br>

# Install
> As a first step it is important to emphasize that you need to have **git installed**, you can install it from <a href="https://git-scm.com/downloads">here</a>. After that you simply have to clone this repository:
   ```powershell
   git clone https://github.com/Syyysco/Zeven.git
   ```
## Installation for Windows
1. You need to have **python3 installed**, if you don't have it installed you can do it from the <a href="https://apps.microsoft.com/detail/9nrwmjp3717k?hl=us-us&gl=US">Microsoft Store</a> or by running the following command on your terminal (CMD or PowerShell):
   ```powershell
   winget install -e --id Python.Python.3.9 --scope machine
   ```
   
2. If you installed a version later than or equal to python3.4, pip will already be installed by default (it will be necessary for this step), if you have another version you can install pip very easily with <a href="https://phoenixnap.com/kb/install-pip-windows">this guide</a> (two steps).
In case **pip is installed** (check it with `pip --version`), you can continue **installing the requirements** for windows with this command:
   ```powershell
   pip install win-requirements.txt
   ```
3. And that's it! Now if you want to be able to run it without having to indicate the absolute path and/or put python3 in each command you can **add it to the system PATH or create an alias**.
Remember to report any bugs, or suggest any changes or additions in the <a href="https://github.com/Syyysco/Zeven/issues">issues</a> section.

<br>

## Installation for Linux and MacOS
1. You need to have **python3 installed**, if you don't have it installed you can look at this guide to have a more complete view <a href="https://www.geeksforgeeks.org/how-to-install-python-on-linux/">here</a> or by running the following command on your terminal:
   ```bash
   sudo apt update
   sudo apt install python3
   ```
   
2. If you installed a version later than or equal to python3.4, pip will already be installed by default (it will be necessary for this step), if you have another version you can install pip very easily with <a href="https://robots.uc3m.es/installation-guides/install-pip.html">this guide</a> (one step).
In case **pip is installed** (check it with `pip3 --version`), you can continue **installing the requirements** with this command:
   ```bash
   pip3 install requirements.txt
   ```
3. And that's it! Now if you want to be able to run it without having to indicate the absolute path and/or put python3 in each command you can **add it to the system PATH or create an alias**.
Remember to report any bugs, or suggest any changes or additions in the <a href="https://github.com/Syyysco/Zeven/issues">issues</a> section.

<br>

## How To Use
> **IMPORTANT NOTE**
>
> - If you have not added Zeven to the PATH, the execution will be as follows: `python3 zeven.py <options> <args>`
> - In this case, the use cases will be represented assuming that it was added to the PATH: `zeven <options> <args>`
### With Folders

- Compact all files contained in a folder (for entire projects) and save it as a new project:
  ```powershell
  zeven -i project -o proyect2
  ```
- Compact all files contained in a folder (for entire projects) and overwrite it:
  ```powershell
  zeven -i project -D
  ```
- Format only the "html" and "javascript" files of a project (folder) and overwrite it:
  ```powershell
  zeven -i project -dD -f "html,js"
  ```
- Format all files in a folder with a 4-space indentation and overwrite it:
  ```powershell
  zeven -i project -dD -I 4
  ```
- Compact only the "html" files in a project without modifying the content of the <style> and <script> tags:
  ```powershell
  zeven -i project -o proyect2 -f "html" -s
  ```
  
### With Files
- Compact a file into a single line and overwrite it:
  ```powershell
  zeven -i main.js
  ```
- Format a file and save it as a new file:
  ```powershell
  zeven -i index.php -o path/to/new/index.php
  ```
- Formatting a file correctly and print it without saving the result:
  ```powershell
  zeven -i index.html -dp
  ```
- Display the result of compacting a file with a non-autodetected format and save it in the same file:
  ```powershell
  zeven -i file -o file -p -f css
  ```
- Format with a 8-space indentation and overwrite the file:
  ```powershell
  zeven -i styles.css -I 8 
  ```
- Format a file without modifying the content of the <style> and <script> tags and save it on a new file:
  ```powershell
  zeven -i index.php -s -o new_index.php
  ```

### Settings mode
- Launches interactive configuration mode:
  ```powershell
  zeven -C
  ```

### Search for help on panels quickly
- Search for keywords in the compact help panel:
  ```powershell
  zeven -h output
  zeven -h -I
  zeven -h backups
  ```
- Search for keywords in the full help panel:
  ```powershell
  zeven -H --format
  zeven -H configuration
  zeven -H -s
  ```

### Update Zeven
- Update the app if there is a new version (connection required):
  ```powershell
  zeven -U
  ```

### Backups
- Delete all stored backups:
  ```powershell
  zeven --flush-backups
  ```

### Reconfigure
- Reset Zeven settings to default:
  ```powershell
  zeven --reconfigure
  ```

<br>

## Using Setting Mode
> In configuration mode you can change certain relevant settings regarding operation, information display and other aspects.

1. You will find **two panels at the top**, *configuration* on the left and **customization** on the right.
  
2. You can **switch panels** with the `left` and `right` **arrow keys**, and switch between their options with the `up` and `down` **arrow keys or the mouse wheel**.

3. Below is the **status panel** and by pressing `H` you can **show/hide the help panel**.

4. To **change the value** of any setting press `ENTER`:
 - If the setting is **ON/OFF** it will simply be changed.
 - If the setting is a **number** or a text field you will enter editing mode.
>> - For numeric values ​​you can increase or decrease the value with `up-down` **arrow keys**.
>> - For text input just type (the help panel will open which is where the typed text is displayed).
>> - Then simply press `ENTER` to **save** the changes or `ESC` to **cancel**.

5. Press `R` on any selected option to **restore it** to its default value.

6. If you press `Q` you will **exit** configuration mode **and save** the changes.

7. On the other hand, if you press `ESC` you will **exit without saving**.

### Setting Mode: Configuration

<br>

### Setting Mode: Customization

<br>

## Available Languages

<br>

## Parameters CheatSheet

<br>

## Possible Errors

<br>

## Notes: Compacting and Formatting
### About Compacting Projects

<br>

### About Formatting Projects

<br>

# For Developers and Contributors

<br>

## Project Goals and Future Ideas

<br>

---

<br>

## License
This project is licensed under the GPL License - see the <a href="LICENSE">LICENSE</a> file for details.
