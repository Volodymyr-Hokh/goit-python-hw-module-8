from collections import defaultdict
from datetime import datetime, timedelta

from faker import Faker


def generate_random_users(number_of_users: int) -> list[dict]:
    """Takes as input a number of users and returns a list 
    of dictionaries with the random user's name and birthday"""

    fake = Faker("uk-UA")
    Faker.seed(1)
    users = [
        {"name": fake.name(),
         "birthday": fake.date_of_birth()}
        for _ in range(number_of_users)]

    return users


def is_the_same_date(date1: datetime, date2: datetime) -> bool:
    """Compare two dates ignoring year"""

    return date1.day == date2.day and date1.month == date2.month


def get_birthdays_per_week(users: list[dict]) -> None:
    """Print names of people from the users list whose birthday is next week"""

    result = defaultdict(list)
    today = datetime.now()
    next_saturday = today.date() + timedelta(days=5-today.weekday())

    for day in range(7):
        day = next_saturday + timedelta(days=day)

        for user in users:
            if is_the_same_date(day, user["birthday"]):
                if day.weekday() in (5, 6):
                    result["Monday"].append(user["name"])
                else:
                    result[day.strftime("%A")].append(user["name"])

    for day_of_week, users_list in result.items():
        print(f"{day_of_week}: {', '.join(users_list)}")


def main():

    users = generate_random_users(100)
    get_birthdays_per_week(users)


if __name__ == "__main__":
    main()
