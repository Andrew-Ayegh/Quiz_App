from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo


import requests

# ____________PARAMETERS FOR API
parameters = {
    "amount":10,
    "type": "boolean"
}

# ---------CATEGORY NUMBERS FROM TRIVIA DATABASE FOR ALL CATEGORIES CORRESPONDIGN WITH THEIR SERIAL NUMBER---------------#
category_data = {
    "2":9,
    "3":10,
    "4":11,
    "5":12,
    "6":13,
    "7":14,
    "8":15,
    "9":16,
    "10":17,
    "11":18,
    "12":19,
    "13":20,
    "14":21,
    "15": 22,
    "16":23,
    "17":24,
    "18":25,
    "19":26,
    "20":27,
    "21":28,
    "22":29,
    "23":30,
    "24":31,
    "25":32
}



# --------------------USER SELECTING CATEGOORY TO PLAY-----------------------------#
user_choice = askstring('Choose Number', 
                '''1. Any
2. General Knowledge
3. Entertainment: Books
4. Entertainment:Film
5. Entertainment: Music
6. Entertainment:Musical And Theatres
7. Entertainment: Television
8. Entertainment:Video Games
9. Entertainment:Board Games
10. Science & Nature
11. Science: Computers
12. Science: Mathematics
13. Mythology
14. Sports
15. Geography 
16. History
17. Politics
18. Arts
19. Celebrities
20. Animals
21. Vehicles
22. Entertainment: Comics
23. Science: Gadgets
24. Entertainment:Japanese Anime & Manga
25. Entertainment: Cartoons & Animation
''')

try:
    # Checking if user choice is empty or 1 meaning the "Any" category should be used
    if user_choice !=" "or user_choice != "1" :
        parameters["category"] = category_data[user_choice]
        

except KeyError:
    # Checking if user input is below or above the serial number range in odrr to use the "Any" Category
    parameters = {
    "amount":10,
    "type": "boolean"
    }
    
finally:
    # Fetching Data from Trivia Database API 
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    question_data = response.json()["results"]

















# question_data = [
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The HTML5 standard was published in 2014.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The first computer bug was formed by faulty wires.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "FLAC stands for 'Free Lossless Audio Condenser'.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "Linus Torvalds created Linux and Git.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "The programming language 'Python' is based off a modified version of 'JavaScript'",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "AMD created the first consumer 64-bit processor.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "'HTML' stands for Hypertext Markup Language.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "In most programming languages, the operator ++ is equivalent to the statement '+= 1'.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "hard",
#         "question": "The IBM PC used an Intel 8008 microprocessor clocked at 4.77 MHz and 8 kilobytes of memory.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     }
# ]
