# Daily Maintenance Logger

A command-line Python automation tool that records kiosk maintenance activities into CSV log file.
The script is designed for field technician and IT operations staff who need simple, persistent maintenance log that can later be opened in Excel, LibreOfficeCal,
or Google Sheets.

## Features

* Record kiosk maintenance activities from the linux terminal
* Automatic timestamp generation
* CSV header creation on first run
* Append new records without overwriting existing logs
* Multiple maintenance entries in one session
* Uppercase normalization for maintenance type
* Lightweight and works offline

## Technologies used

* Python 3
* datetime
* os path
* Linux command line
