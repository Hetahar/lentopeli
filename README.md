# **Karkuteillä - Game Project Documentation**

## **Overview**
Karkuteillä is a fun and interactive game built using Python. The game integrates a **MariaDB database** to manage in-game data, such as player information and scores. This project demonstrates database interaction, game logic implementation, and GUI development. This was my first group programming project.

To see a video demo of the game, follow this [link](https://drive.google.com/file/d/119xXjwAVxJbm-l_HId2AN8pGHddfZWnz/view?usp=sharing).
---

## **Features**
- Interactive gameplay with visual elements.
- Database integration for storing player information.
- Easy setup instructions for database configuration.

---

## **Technologies Used**
- **Programming Languages**: Python, JavaScript, HTML, CSS
- **Database**: MariaDB
- **Libraries**: 
  - mysql-connector-python
  - pygame

---

## **System Requirements**
- Python 3.8 or higher
- MariaDB or MySQL Server
- pip (Python package manager)

---

## 🔧 **Installation Guide**

### **1. Clone the Repository**
```bash
$ git clone <repository-url> karkuteilla
$ cd karkuteilla
```

---

## **Database Setup**

1. **Install MariaDB**
- Linux:
```bash
sudo apt install mariadb-server
```
- Windows/MacOS: Download from MariaDB [Downloads](https://mariadb.org/download/?t=mariadb&p=mariadb&r=11.6.2&os=windows&cpu=x86_64&pkg=msi&mirror=xtom_tal).

2. **Create Database**
```bash
$ mysql -u root -p
mysql> CREATE DATABASE karkuteilla;
```

3. **Import Database Schema**
```bash
$ mysql -u root -p karkuteilla < database/database_dump.sql
```
4. **Verify Database**
```bash
USE karkuteilla;
SHOW TABLES;
```

---
## **Launching the game**

- Launch the server:
```bash
python main.py
```
- In ``aloitus_sivuUUSI.html``, choose a browser to open the game in.

---

## **Usage Instructions**

1. Launch the game in your preferred browser.
2. Choose a continent.
3. Guess the countries based on the given hints. Try to score high by identifying all four countries correctly.
4. Scores are automatically saved to the database.
5. Close the game browser and stop the server (ctrl+c).