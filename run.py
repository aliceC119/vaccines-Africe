import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Vaccines - Africa (2020-2024)')



def get_livessaved_data():
    """
    Get lives saved figures input from the user.
    """
   
    print("Please enter lives saved data from the last year.")
    print("Data should be eight numbers, separated by commas.")
    print("Example: 100,200,300,400,500,600,700,800\n")

    data_str = input("Enter your lives saved data here: ")
    print(f"The data provided is {data_str}")

get_livessaved_data()
    
    








# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
