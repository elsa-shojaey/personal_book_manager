# Personal Book Manager

![Static Badge](https://img.shields.io/badge/python-3.12-blue)

A simple book manager built with python

# Features
- add multiple books
- display books
- save books
- load seved books
- admin mode
- set book priority

## Book Priority
each book can have one of these priority levels:
- low
- medium
- high

## Requirments
- Python
- python-dotenv

## Installation
Install the required packages:

```bash
python -m pip -r requirements.txt
```

## Envoirment setup
creat a `.env` file in the project folder

Use `.env.example` as a template

Add your admin password 

```env
BOOK_MANAGER_ADMIN_PASSWORD=admin_password_here
```

replace `admin_password_here` with yuor own admin password

## Run the Program
run the main file:
```bash
python main.py
```

## Screenshot
![personal_book_manager_screenshot](images\screenshot.png)

## Demo
![personal_book_manager_demo](images\Animation.gif)

## Project Structure

```text
C:.
│   .env.example
│   .gitignore
│   main.py
│   books.py
│   README.md
│   requirements.txt
│
├───images
│   demo.gif
│   Screenshot.png
└───
```

| file | description |
| --- |---|
| `main.py` | main file used to run program|
| `books.py` | Contains book-related functions .|
| `requirements.txt` | Lists the external Python packages required by the project. |
| `.env.example` | Shows the environment variable required for Admin Mode .|
| `.gitignore` | tells git which files and folders shold not be tracked|
| `README.md` | contains the project documentation|
| `images/` | stores project screenshots and demo|
| `images/demo.gif` | shows the project demo|


## How it Works
1. The program starts by running `main.py` .
2. The user must enter the name .
3. it displays a welcome message .
4. The user can access admin mode by entering the correct password .
5. The user must enter how many books want .
6. The user must enter the names of the book .
7. Finally , the entered books are displayed .

## Troubleshooting
### FileNotError
   - Meaning : The program can't find a file .
   - Cause : The file is missing .
   - Check : Make sure the file is there .
### JSONDecodeError
   - Meaning : The program can't read the books.json file .
   - Cause : The file is empty or has wrong information .
   - Check : Check the books.json file .
### ModuleNotFoundError: No module named`dotenv`
   - Meaning : Python can't find a library .
   - Cause : The library is not installed .
   - Check : Check requirements.txt and install the library .
### Password Error
   - Meaning : The password is not correct .
   - Caus : The password is missing or wrong in the .env file .
   - Check : Check the password in the .env file .