import datetime

def print_header():
    print('-----------------------------------')
    print('       BIRTHDAY APP     ')
    print('-----------------------------------')
    print()


def get_birthday_from_user():
    print("When were you born")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    birthday = datetime.date(year, month, day)
    return birthday

def compute_days_between_days(original_date, target_date):
    this_year_date = datetime.date(target_date.year,original_date.month,original_date.day)
    date_diff = this_year_date - target_date
    return date_diff.days

def print_birthday_information(days):
    if days < 0:
        print("Your birthday just went by {0} days ago".format(-days))
    elif days > 0 :
        print("Your birthday is only {0} days away".format(days))
    else:
        print("Your birthday is today! Happy Birthday")




def main():
    print_header()
    bday = get_birthday_from_user()
    print(bday)
    today = datetime.date.today()
    number_of_days = compute_days_between_days(bday, today)
    print(number_of_days)
    print_birthday_information(number_of_days)


main()