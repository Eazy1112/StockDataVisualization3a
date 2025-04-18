import re
import datetime

##Ask the user to enter the stock symbol for the company they want data for.
def get_stock_symbol():
    symbol = input("Enter the stock symbol you are looking for: ")

    #Validate that symbol exists

    return symbol

##Ask the user for the chart type they would like.
def get_chart_type():
    print("Chart Types\n________________\n1. Bar\n2. Line\n\n")

    while(True):
        chart_type = input("Enter the chart type you want (1,2): ")

        if(chart_type == '1' or chart_type == '2'):
            break
        else:
            print("Please input valid chart type.\n")

    return chart_type

##Ask the user for the time series function they want the api to use.
def get_function():
    print("Select the Time Series of the chart you want to generate\n")
    print("___________________________________________________________\n")
    print("1. Intraday\n2. Daily\n3. Weekly\n4. Monthly\n")

    while(True):
        option = input("Enter time series option (1,2,3,4): ")

        if(option == '1' or option == '2' or option == '3' or option == '4'):
            break
        else:
            print("Please input valid function option.\n")

    function = "TIME_SERIES_"

    if(option == '1'):
        function += "INTRADAY"
    elif(option == '2'):
        function += "DAILY"
    elif(option == '3'):
        function += "WEEKLY"
    elif(option == '4'):
        function += "MONTHLY"

    return function

##Ask the user for the beginning date in YYYY-MM-DD format.
def get_start_date():
    while(True):
        start_date = input("Enter start date (YYYY-MM-DD): ")

        #Validate that input is correctly formatted
        match = re.search(r"\b\d{4}-\d{2}-\d{2}\b",start_date)

        if(match):
            if(is_date_valid(start_date) == False):
                print("Please enter valid date.\n")
                continue
            else:
                break
        else:
            print("Please enter valid date format.\n")

    return start_date

##Ask the user for the end date in YYYY-MM-DD format.
##The end date should not be before the begin date
def get_end_date(start_date):
    while(True):
        end_date = input("Enter end date (YYYY-MM-DD): ")

        #Validate that input is correctly formatted
        match = re.search(r"\b\d{4}-\d{2}-\d{2}\b",end_date)

        if(match):
            #Check that date exists and is current or past
            if(is_date_valid(end_date) == False):
                print("Please enter valid date\n")
                continue
            #Check that end date does not begin before start date
            elif(end_date < start_date):
                print("Please enter end date that occurs after start date.\n")
                continue
            #If no errors, break out of while loop
            else:
                break
        else:
            print("Please enter valid date format.\n")
 
    return end_date

#Check if date is valid
def is_date_valid(date_string):

    date_components = date_string.split("-")
    year = int(date_components[0])
    month = int(date_components[1])
    day = int(date_components[2]) 

    try:
        x = datetime.date(year,month,day)
    except:
        return False
    else:
        if(x > datetime.date.today()):
            return False
        return True
    