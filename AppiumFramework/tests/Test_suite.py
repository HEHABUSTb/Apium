import unittest
from AppiumFramework.tests.Login_test import LoginPageTest
from AppiumFramework.tests.ContactUsForm_test_by_class import ContactFormTest

contact_form = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)
login_page = unittest.TestLoader().loadTestsFromTestCase(LoginPageTest)

regression_test = unittest.TestSuite([contact_form, login_page])

unittest.TextTestRunner(verbosity=1).run(regression_test)
