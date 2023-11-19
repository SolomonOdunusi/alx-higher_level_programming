# 0x0F. Python - Object-relational Mapping

## Overview

In this project, you will work on linking Python with databases using Object-Relational Mapping (ORM). Specifically, you will use the `MySQLdb` module to connect to a MySQL database and execute SQL queries. Additionally, you will use the `SQLAlchemy` module, which is an Object-Relational Mapper (ORM). The purpose of an ORM is to abstract the storage to the usage, eliminating the need to write SQL queries directly in your code.

## Table of Contents

1. [Project Description](#project-description)
2. [Requirements](#requirements)
3. [Tasks](#tasks)
    - [0. Get all states](#0-get-all-states)
    - [1. Filter states](#1-filter-states)
    - [2. Filter states by user input](#2-filter-states-by-user-input)
    - [3. SQL Injection...](#3-sql-injection)
    - [4. Cities by states](#4-cities-by-states)
    - [5. All cities by state](#5-all-cities-by-state)
    - [6. First state model](#6-first-state-model)
    - [7. All states via SQLAlchemy](#7-all-states-via-sqlalchemy)
    - [8. First state](#8-first-state)
    - [9. Contains `a`](#9-contains-a)
    - [10. Get a state](#10-get-a-state)
    - [11. Add a new state](#11-add-a-new-state)
    - [12. Update a state](#12-update-a-state)
    - [13. Delete states](#13-delete-states)
    - [14. Cities in state](#14-cities-in-state)
4. [How to Use](#how-to-use)
5. [Credits](#credits)

## Project Description

The project involves working with Python, Object-Relational Mapping (ORM), SQL, and MySQL. The focus is on using `MySQLdb` to connect to a MySQL database and execute SQL queries. Additionally, you will utilize `SQLAlchemy`, an ORM, to abstract the storage and work with Python objects instead of direct SQL queries.

### Learning Objectives

By the end of this project, you should be able to:

- Explain why Python programming is powerful.
- Connect to a MySQL database from a Python script.
- Perform SELECT operations on a MySQL table using Python.
- Perform INSERT operations on a MySQL table using Python.
- Understand the concept of Object-Relational Mapping (ORM).
- Map a Python class to a MySQL table using SQLAlchemy.
- Create a Python Virtual Environment.
  
### Requirements

- Allowed editors: vi, vim, emacs.
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
- MySQLdb version 2.0.x will be used.
- SQLAlchemy version 1.4.x will be used.
- Pycodestyle version 2.8.x should be used for code formatting.
- All files must be executable.

## Tasks

### 0. Get all states

Write a script that lists all states from the database `hbtn_0e_0_usa`. The script should connect to a MySQL server and display results sorted by `states.id`.

**Example:**
```bash
$ cat 0-select_states.sql | mysql -uroot -p
$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
```

### 1. Filter states

Write a script that lists all states with a name starting with 'N' (uppercase) from the database `hbtn_0e_0_usa`. The script should connect to a MySQL server and display results sorted by `states.id`.

**Example:**
```bash
$ cat 0-select_states.sql | mysql -uroot -p
$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
```

### 2. Filter states by user input

Write a script that takes a state name as an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where the name matches the argument. The script should connect to a MySQL server and display results sorted by `states.id`.

**Example:**
```bash
$ cat 0-select_states.sql | mysql -uroot -p
$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
```

### 3. SQL Injection...

Enhance the previous script to handle SQL injection securely.

**Example:**
```bash
$ cat 0-select_states.sql | mysql -uroot -p
$ ./3-my_safe
