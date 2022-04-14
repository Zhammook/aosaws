from faker import Faker
fake = Faker(locale='en_CA')
new_username = f'{fake.user_name()}{fake.pyint(111,999)}'[:15]
new_password = fake.password()
password = fake.password()[:12]
base_url = 'https://advantageonlineshopping.com/#/'
home_page_title = '\xa0Advantage Shopping'
aos_register = 'https://advantageonlineshopping.com/#/register'
aos_homepage = 'Advantage Shopping'
#confirm_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
phone = fake.phone_number()
country = fake.current_country()
city = fake.city()
province = fake.province_abbr()
address = f'{fake.street_address()}'
posta_code = fake.postcode()
email = fake.email()
order_number = ""
tracking_number = ""
product_name = ""
order_element = ""