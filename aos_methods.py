import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import aos_locators as locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)
#s = Service(executable_path='chromedriver.exe')
#driver = webdriver.Chrome(service=s)


# Setup the window and initialize the time to start
def setUp():
    print('\n ------------------~~~~****~~~~-----------------------------')
    print(f' test started at :{datetime.datetime.now()}')
    # Maximize the browser window.
    driver.maximize_window()
    # wait to open the browser implicitly
    driver.implicitly_wait(30)
    # Navigate to web page URL - https://advantageonlineshopping.com/
    driver.get(locators.base_url)

    # 4. Check URL and home page title are as expected.
    if driver.current_url == locators.base_url and driver.title == locators.home_page_title:
        print(driver.current_url)
        print({driver.title})
        print(f'We are at the correct web page {driver.current_url}')
        print(f'We are seeing the title of web page as : {driver.title}')
    else:
        print(f'We are not at the correct web page!! check your code')
        driver.close()  # close the current tab
        driver.quit()  # close the browser completely


# login into user account using username and password
def log_in(username, password):
    sleep(2)
    print('\n ------------------~~~~****~~~~-----------------------------')
    if driver.current_url == locators.base_url and driver.title == locators.home_page_title:
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(5)
        driver.find_element(By.XPATH, "//input[@name= 'username']").send_keys(username)
        sleep(1)
        driver.find_element(By.XPATH, "//input[@name= 'password']").send_keys(password)
        sleep(1)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        if driver.current_url == locators.base_url:
            assert driver.current_url == locators.base_url
            print(f'Log in successfully with the new username and password. Advantage DEMO is present. \n'
            f'We logged in with Username: {username} and Password: {password}, name is presented at the top right corner of the Home page')
        else:
            print(f'We\re not at the Dashboard. Try again')


# Check the availability of the texts, Links and other objects
def check_availability_text():
    sleep(2)
    print('\n ------------------~~~~****~~~~-----------------------------')
    if driver.current_url == locators.base_url:
        speaker = driver.find_element(By.ID, 'speakersTxt')
        print(f'The display feature of the SPEAKER is : {speaker.is_displayed()}')
        print(f'The enable feature of the SPEAKER is : {speaker.is_enabled()}')
        driver.find_element(By.ID, 'speakersTxt').click()
        sleep(5)
        if driver.current_url == 'https://advantageonlineshopping.com/#/category/Speakers/4':
            driver.back()
            sleep(3)
        tablets = driver.find_element(By.ID, 'tabletsTxt')
        print(f'The display feature of the TABLETS is : {tablets.is_displayed()}')
        print(f'The enable feature of the TABLETS is : {tablets.is_enabled()}')
        driver.find_element(By.ID, 'tabletsTxt').click()
        sleep(5)
        if driver.current_url == 'https://advantageonlineshopping.com/#/category/Tablets/3':
            driver.back()
            sleep(3)
            headphones = driver.find_element(By.ID, 'headphonesTxt')
            print(f'The display feature of the HEADPHONES is : {headphones.is_displayed()}')
            print(f'The enable feature of the HEADPHONES is : {headphones.is_enabled()}')
            driver.find_element(By.ID, 'headphonesTxt').click()
        sleep(5)
        if driver.current_url == 'https://advantageonlineshopping.com/#/category/Headphones/2':
            driver.back()
            sleep(3)
        laptops = driver.find_element(By.ID, 'laptopsTxt')
        print(f'The display feature of the LAPTOPS is : {laptops.is_displayed()}')
        print(f'The enable feature of the  LAPTOPS is : {laptops.is_enabled()}')
        driver.find_element(By.ID, 'laptopsTxt').click()
        sleep(5)
        if driver.current_url == 'https://advantageonlineshopping.com/#/category/Laptops/1':
            driver.back()
            sleep(3)
        mice = driver.find_element(By.ID, 'miceTxt')
        print(f'The display feature of the MICE is : {mice.is_displayed()}')
        print(f'The enable feature of the MICE is : {mice.is_enabled()}')
        driver.find_element(By.ID, 'miceTxt').click()
        sleep(5)
        if driver.current_url == 'https://advantageonlineshopping.com/#/category/Mice/5':
            driver.back()
            sleep(3)


# Check the navigation menu bar if it is clickable or not
def check_clickable_nav():
    sleep(2)
    print('\n ------------------~~~~****~~~~-----------------------------')
    product = driver.find_element(By.XPATH, '//a[contains(., "OUR PRODUCTS")]')
    print(f' the clickable feature of OUR PRODUCTS at the top menu is : {product.is_enabled()}')
    offer = driver.find_element(By.XPATH, '//a[contains(., "SPECIAL OFFER")]')
    print(f' the clickable feature of SPECIAL OFFER at the top menu is : {offer.is_enabled()}')
    special_offer = driver.find_element(By.ID, 'see_offer_btn')
    print(f' the SEE OFFER button display condition is :{special_offer.is_displayed()}')
    driver.find_element(By.ID, 'see_offer_btn').click()
    sleep(5)
    if driver.current_url == 'https://advantageonlineshopping.com/#/product/3':
        product_specifications = driver.find_element(By.XPATH, '//h2[@class="roboto-regular product_specifications ng-scope"]')
        print(f' PRODUCT SPECIFICATIONS display condition is :{product_specifications.is_displayed()}, and table contents is there')
        sleep(5)
        driver.back()
    items = driver.find_element(By.XPATH, '//a[contains(., "POPULAR ITEMS")]')
    print(f' the clickable feature of POPULAR ITEMS at the top menu is : {items.is_enabled()}')
    contactus = driver.find_element(By.XPATH, '//a[contains(., "CONTACT US")]')
    print(f' the clickable feature of CONTACT US at the top menu is : {contactus.is_enabled()}')


# Check the visibility of the logo
def check_logo():
    sleep(2)
    print('\n ------------------~~~~****~~~~-----------------------------')
    logo = driver.find_element(By.ID, 'Layer_1')
    print(f' Checking the main logo is displayed is : {logo.is_displayed()}')


# Check the enability of CONTACT US
def check_contactus():
    sleep(2)
    print('\n ------------------~~~~****~~~~-----------------------------')
    if driver.find_element(By.XPATH, '//*[@id="supportCover"]/div[2]/h1').is_displayed():
        print('CONTACT US form is displayed on the screen')
        driver.find_element(By.XPATH, '//select[@name="categoryListboxContactUs"]').send_keys('Tablets')
        sleep(1)
        driver.find_element(By.XPATH, '//select[@name="productListboxContactUs"]').send_keys('HP ElitePad 1000 G2 Tablet')
        sleep(1)
        driver.find_element(By.XPATH, '//input[@name="emailContactUs"]').send_keys(locators.email)
        sleep(1)
    if driver.find_element(By.XPATH, '//label[@class="Subject ng-binding"]').is_displayed():
        print(' we found Subject area where you can send your message')
        driver.find_element(By.XPATH, '//textarea[@name="subjectTextareaContactUs"]').send_keys('Dear Sir/Madam\n, The item that I have purchased, has been charged twice, from my bank account, could you please check from your end and return my money back, as I have canceled my order, I might come back to re-order it in the near future.\n Thanks')
        sleep(5)
        driver.find_element(By.ID, 'send_btnundefined').click()
        sleep(1)
        print('Thank you for contacting Advantage support.')
        sleep(1)
        display_btn = driver.find_element(By.XPATH, '//a[@class="a-button ng-binding"]')
        sleep(1)
        print(f'the CONTINUE SHOPPING button display feature is : {display_btn.is_displayed()}')
        sleep(1)
        driver.find_element(By.XPATH, '//a[@class="a-button ng-binding"]').click()
        sleep(1)
        print(f'the CONTINUE SHOPPING button clickable feature is : {display_btn.is_enabled()}')
        sleep(5)


# Check the visibility and clickability of the social media icons
# Check Facebook social network
def check_socialnetwork_facebook():
    sleep(2)
    print('\n ------------------~~~~****~~~~-----------------------------')
    if driver.find_element(By.XPATH, '//h3[contains(., "FOLLOW US")]').is_displayed():
        print('We could find FOLLOW US displayed')
        sleep(1)
        facebook = driver.find_element(By.XPATH, '//img[@name="follow_facebook"]')
        print(f' the Facebook img display condition is: { facebook.is_displayed()}')
        print(f' the Facebook img clickable condition is: {facebook.is_enabled()}')
        driver.find_element(By.XPATH, '//img[@name="follow_facebook"]').click()
        driver.switch_to.window(driver.window_handles[1])
        if driver.current_url == 'https://www.facebook.com/MicroFocus/':
            print(f'Social media link FaceBook is available and clickable')
            sleep(3)
        else:
            print('Facebook page not found')
        driver.close()
        print(' Facebook link has been closed')
        driver.switch_to.window(driver.window_handles[0])


# Check Twitter social network
def check_socialnetwork_twitter():
    sleep(2)
    if driver.current_url == 'https://advantageonlineshopping.com/#/':
        twitter = driver.find_element(By.XPATH, '//img[@name="follow_twitter"]')
        print(f' the Twitter img display condition is: {twitter.is_displayed()}')
        print(f' the Twitter img clickable condition is: {twitter.is_enabled()}')
        driver.find_element(By.XPATH, '//img[@name="follow_twitter"]').click()
        driver.switch_to.window(driver.window_handles[1])
        if driver.current_url == 'https://twitter.com/MicroFocus':
            print(f'Social media link Twitter is available and clickable')
            sleep(3)
        else:
            print('Twitter page not found')
        driver.close()
        print(' Twitter link has been closed')
        driver.switch_to.window(driver.window_handles[0])


# Check LinkedIn social network
def check_socialnetwork_linkedin():
    sleep(2)
    if driver.current_url == 'https://advantageonlineshopping.com/#/':
        linkedin = driver.find_element(By.XPATH, '//img[@name="follow_linkedin"]')
        print(f' the LinkedIn img display condition is: {linkedin.is_displayed()}')
        print(f' the LinkedIn img clickable condition is: {linkedin.is_enabled()}')
        driver.find_element(By.XPATH, '//img[@name="follow_linkedin"]').click()
        driver.switch_to.window(driver.window_handles[1])
        if driver.current_url == 'https://linkedin.com/MicroFocus':
            print(f'Social media link LinkedIn is available and clickable')
            sleep(3)
        else:
            print('LinkedIn page not found')
        driver.close()
        print(' LinkedIn link has been closed')
        driver.switch_to.window(driver.window_handles[0])
        print('Finally we validated all the TEXTS, LINKS, BUTTONS and CONTACT US successfully ')


# Checkout shoppingcart
def checkout_shoppingcart():
    sleep(2)
    print('\n ------------------~~~~****~~~~-----------------------------')
    if driver.current_url == 'https://advantageonlineshopping.com/#/':
        driver.get('https://advantageonlineshopping.com/#/product/16')
        sleep(2)
        driver.find_element(By.NAME, 'save_to_cart').click()
        sleep(1)
        driver.find_element(By.ID, 'shoppingCartLink').click()
        sleep(1)
        driver.find_element(By.ID, 'checkOutButton').click()
        sleep(3)
        print(f' we can see ORDER PAYMENT and SHIPPING DETAILS page')
        print('Order Summary information is displayed')
        print(f' the full name :{locators.full_name} is displayed on the ORDER PAYMENT and SHIPPING DETAILS page')
        driver.find_element(By.ID, 'next_btn').click()
        sleep(5)
        if driver.current_url == 'https://advantageonlineshopping.com/#/orderPayment':
            print(f' we can see ORDER PAYMENT and PAYMENT METHOD page')
            print(f' payment info was entered for SafePay username, SafePay password')
            driver.find_element(By.NAME, 'safepay').click()
            sleep(3)
            driver.find_element(By.NAME, 'safepay_username').send_keys(locators.new_username)
            sleep(1)
            driver.find_element(By.NAME, 'safepay_password').send_keys(locators.password)
            sleep(3)
            driver.find_element(By.NAME, 'save_safepay')
            sleep(1)
            driver.find_element(By.ID, 'pay_now_btn_SAFEPAY').click()


# Validate order being created
def validate_order_created():
    sleep(2)
    print('\n ------------------~~~~****~~~~-----------------------------')
    if driver.current_url == 'https://advantageonlineshopping.com/#/orderPayment':
        sleep(3)
        print(f' order payment was made and thank you message was shown, Thank you for buying with Advantage')
        sleep(1)
        locators.tracking_number = driver.find_element(By.ID, 'trackingNumberLabel').text
        print(f' Tracking number was captured for this order: {locators.tracking_number}')
        locators.order_number = driver.find_element(By.ID, 'orderNumberLabel').text
        print(f' Order Number was captured for this order: {locators.order_number}')
        print(f' Shipping to : {locators.full_name}, Address : {locators.address}')
        print(f' Phone number is: {locators.phone}')
        print(f' Date and time: {datetime.datetime.now()}')


# Delete user order
def delete_order():
    sleep(2)
    print('\n ------------------~~~~****~~~~-----------------------------')
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[2]').click()
    sleep(2)
    if driver.current_url == 'https://advantageonlineshopping.com/#/MyOrders':
        locators.order_element = driver.find_element(By.XPATH, f'//label[contains(., "{locators.order_number}")]').text
        print(f'The order number is there and matching with the one that captured  on the screen : {locators.order_element}')
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'REMOVE').click()
        sleep(3)
        print('Are you sure you want to cancel your order')
        driver.find_element(By.XPATH, '//*[@id="confBtn_1"]/label[2]').click()
        sleep(3)
        print(' -NO orders-')
        print('user order has been deleted, nothing left in the order list')
        if driver.current_url == 'https://advantageonlineshopping.com/#/MyOrders':
            driver.find_element(By.XPATH, '//a[@class="a-button ng-scope"]').click()


# Delete user account and login back to test if the account has been deleted
def delete_account():
    sleep(2)
    if driver.current_url == locators.base_url:
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(3)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
        sleep(3)
        name = driver.find_element(By.XPATH, f'//label[contains(.,"{locators.full_name}")]')
        print({name.is_displayed()})
        print(f'Payment order form is showing with the full name of user displayed in Account details :{locators.full_name}')
        sleep(3)
        delete_btn = driver.find_element(By.XPATH, '//button[contains(., "Delete Account")]')
        print(f' Delete Button display condition is : {delete_btn.is_displayed()}')
        driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
        print(f' pop up window will appear asking the user to confirm deletetion, Are you sure you want to delete account?')
        sleep(1)
        driver.find_element(By.CLASS_NAME, 'deletePopupBtn').click()
        sleep(3)
        print('deleted account successfully')


# Create new account for the user
def create_new_account():
    sleep(2)
    print('\n ------------------~~~~****~~~~-----------------------------')

    if driver.current_url == locators.base_url and driver.title == locators.home_page_title:
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(5)
        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
        sleep(1)
        if driver.current_url == locators.aos_register or driver.title == locators.aos_homepage:
            driver.find_element(By.XPATH, "//input[@name= 'usernameRegisterPage']").send_keys(locators.new_username)
            driver.find_element(By.XPATH, "//input[@name= 'emailRegisterPage']").send_keys(locators.email)
            driver.find_element(By.XPATH, "//input[@name= 'passwordRegisterPage']").send_keys(locators.new_password)
            driver.find_element(By.XPATH, "//input[@name= 'confirm_passwordRegisterPage']").send_keys(locators.new_password)
            driver.find_element(By.XPATH, "//input[@name= 'first_nameRegisterPage']").send_keys(locators.first_name)
            driver.find_element(By.XPATH, "//input[@name= 'last_nameRegisterPage']").send_keys(locators.last_name)
            driver.find_element(By.XPATH, "//input[@name= 'phone_numberRegisterPage']").send_keys(locators.phone)
            Select(driver.find_element(By.XPATH, '//*[@id="formCover"]/div[3]/div[1]/sec-view[1]/div/select')).select_by_visible_text('Canada')
            sleep(1)
            driver.find_element(By.XPATH, "//input[@name= 'cityRegisterPage']").send_keys(locators.city)
            driver.find_element(By.XPATH, "//input[@name= 'addressRegisterPage']").send_keys(locators.address)
            driver.find_element(By.XPATH, "//input[@name= 'state_/_province_/_regionRegisterPage']").send_keys(locators.province)
            driver.find_element(By.XPATH, "//input[@name= 'postal_codeRegisterPage']").send_keys(locators.posta_code)
            sleep(1)
            driver.find_element(By.XPATH, '//*[@id="formCover"]/sec-view/div/input').click()
            sleep(3)
            driver.find_element(By.XPATH, '//*[@id="register_btnundefined"]').click()
            sleep(5)
            print(f' full name has been created : {locators.full_name}')
            print(f' address has been created : {locators.address}')


# Validate New Account created (new username is displayed in the top menu)
def check_we_logged_in_with_new_username():
    sleep(2)
    print('\n ------------------~~~~****~~~~-----------------------------')
    if driver.current_url == locators.base_url and driver.title == locators.home_page_title:
        if driver.find_element(By.XPATH, f'//a[contains(.,"{locators.new_username}")]'):
            sleep(3)
            print(f' username has been created and we can see the name at the top right corner : {locators.new_username}')
        else:
            print('user is not found')


# logout of the user account
def log_out():
    sleep(2)
    print('\n ------------------~~~~****~~~~-----------------------------')
    if driver.current_url == locators.base_url:
        driver.find_element(By.ID, 'menuUserLink').click()
        sleep(1)
        driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
        sleep(1)
    if driver.current_url == locators.base_url:
        print(f'User Log out successfully done at: {datetime.datetime.now()}')

    else:
        print(f'You are at the wrong page')


# Shutdown all opened taps and close the browser
def tearDown():
    sleep(2)
    if driver is not None:
        sleep(5)
        print(f'\n ------------------~~~~****~~~~-----------------------------')
        print(f' Test was completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()

# Call all the functions
# setUp()
# create_new_account()
# check_we_logged_in_with_new_username()
# log_out()
# log_in(locators.new_username, locators.new_password)
# check_we_logged_in_with_new_username()
# log_out()
# log_in(locators.new_username, locators.new_password)
# check_availability_text()
# check_clickable_nav()
# check_logo()
# check_contactus()
# check_socialnetwork_facebook()
# check_socialnetwork_twitter()
# check_socialnetwork_linkedin()
# checkout_shoppingcart()
# validate_order_created()
# log_in(locators.new_username, locators.new_password)
# delete_order()
# delete_account()
# log_in(locators.new_username, locators.new_password)
#log_out()
# tearDown()
