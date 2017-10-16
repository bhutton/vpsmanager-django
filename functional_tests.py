import warnings
import unittest

from selenium import webdriver

class FunctionalTests(unittest.TestCase):

    def setUp(self):
        warnings.filterwarnings("ignore", category=ResourceWarning)
        options = webdriver.ChromeOptions()
        options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
        options.add_argument('headless')
        options.add_argument('window-size=1200x600, chrome.verbose=true')
        self.browser = webdriver.Chrome(chrome_options=options)
        self.browser.implicitly_wait(10)

    def test_app(self):
        self.browser.get('http://localhost:8000')
        assert 'VPS Manager' in self.browser.title

    def test_create_vps_form(self):
        self.browser.get('http://localhost:8000/vps/create/')
        assert 'VPS' in self.browser.title
        assert self.browser.find_element_by_name('item_name')
        assert self.browser.find_element_by_name('item_description')
        assert self.browser.find_element_by_name('item_image')
        assert self.browser.find_element_by_name('item_memory')
        assert self.browser.find_element_by_name('item_disk')
        assert self.browser.find_element_by_name('item_bridge')
        assert self.browser.find_element_by_name('item_create_disk')
        assert self.browser.find_element_by_name('item_create_path')

    def test_create_vps_form_submit(self):
        self.browser.get('http://localhost:8000/vps/create/')
        self.browser.find_element_by_name('item_name').send_keys('item1')
        self.browser.find_element_by_name('item_description').send_keys('description')
        return_value = self.browser.find_element_by_name('vps').submit()
        url = self.browser.current_url
        self.browser.get_screenshot_as_file('item1.png')
        assert 'http://localhost:8000/' == url

    # def test_create_user(self):
    #     self.browser.get('http://localhost:8000/createuser/')
    #     assert 'Create User' in self.browser.title


if __name__ == '__main__':
    unittest.main()