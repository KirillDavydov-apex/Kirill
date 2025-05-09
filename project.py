# Program to display birthday information

def birthday_info(name, birthdate):
    """
    Function to display birthday information.
    :param name: Name of the person
    :param birthdate: Birthdate in 'YYYY-MM-DD' format
    """
    from datetime import datetime, timedelta
    
    # Parse the birthdate
    try:
        birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    except ValueError:
        return "Error: Please provide the birthdate in 'YYYY-MM-DD' format."
    
    # Calculate age
    today = datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    
    # Calculate next birthday
    next_birthday = birthdate.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    days_until_next_birthday = (next_birthday - today).days
    
    return f"{name} is {age} years old. Next birthday in {days_until_next_birthday} days."

# Function to get user input for birthday

def get_user_birthday():
    name = input("Enter your name: ")
    year = input("Enter your birth year (YYYY): ")
    month = input("Enter your birth month (MM): ")
    day = input("Enter your birth day (DD): ")
    birthdate = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
    return name, birthdate

# Main program
if __name__ == '__main__':
    user_name, user_birthdate = get_user_birthday()
    print(birthday_info(user_name, user_birthdate))