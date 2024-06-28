from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention
        self.assertIn('To-Do', self.browser.title)
        self.fail("Finish the test!")


# She is invited to enter a to-do item straight away

# She types ""Buy pea feathers" into a text box

# When she hits enter the page updatges and not thw page lists
# 1 Buy pea feather as an item in the list

# There is still a text box inviting her to add another item
# She enters "Use feather" as an item in to-do list

# The page updates again, and now shows both items on her list

# Edith wonders the site will remember her list
# Then she sees the site has generated a unique URL for her
# There is some explanatory text to that effect

# She visits that URL - her do-do list is still there

# Satisfied she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings="ignore")