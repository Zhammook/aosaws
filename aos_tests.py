import unittest
import aos_methods as methods
import aos_locators as locator1

class AosPositiveTestCases(unittest.TestCase):

    @staticmethod # signal to Unittest framework that this is a function inside the class (vs. @classmethod)
    def test_create_new_user(): # test_ in the name is mandatory
        methods.setUp()
        methods.create_new_account()
        methods.check_we_logged_in_with_new_username()
        methods.log_out()
        methods.log_in(locator1.new_username, locator1.new_password)
        methods.check_we_logged_in_with_new_username()
        methods.check_availability_text()
        methods.check_clickable_nav()
        methods.check_logo()
        methods.check_contactus()
        methods.check_socialnetwork_facebook()
        methods.check_socialnetwork_twitter()
        methods.check_socialnetwork_linkedin()
        methods.checkout_shoppingcart()
        methods.validate_order_created()
        methods.delete_order()
        methods.delete_account()
        methods.log_in(locator1.new_username, locator1.new_password)
        methods.tearDown()