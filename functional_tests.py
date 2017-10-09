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
        assert 'Django' in self.browser.title


if __name__ == '__main__':
    unittest.main()