from faker import Faker

fake = Faker()

print(fake.date_between(start_date='-2y', end_date='today'), type(fake.date_between(start_date='-2y', end_date='today')))