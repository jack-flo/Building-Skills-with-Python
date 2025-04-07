# Turning dates in a dd-MMM-yy format and respond with a tuple of (y, m, d)

monthConversions = {
    "JAN": 1,
    "FEB": 2,
    "MAR": 3,
    "APR": 4,
    "MAY": 5,
    "JUN": 6,
    "JUL": 7,
    "AUG": 8,
    "SEP": 9,
    "OCT": 10,
    "NOV": 11,
    "DEC": 12
}

# Function for splitting the date into 3 items using the "-" character


def convertDate(date):
    dateList = date.split("-")
    oldMonth = dateList[1]
    newMonth = str(monthConversions.get(oldMonth))
    dateList[1] = newMonth
    convertedDate = "-".join(dateList)
    return convertedDate

# Main


date = input("Please enter your date in the dd-MMM-yy format")
print(f"Here is your converted date: {convertDate(date)}")
