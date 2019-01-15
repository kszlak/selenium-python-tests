import unittest
from selenium import webdriver

class MainTests(unittest.TestCase):

    def setUp(self):
        print('Początek testu')

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path='C:\TestFiles\chromedriver.exe')



    def test_strona_glowna(self):
        driver = self.driver
        driver.get('https://asoftmurmur.com/?ref=discuvver')
        title = driver.title
        print(title)
        assert title == 'A Soft Murmur'

    def test_blog(self):
        driver = self.driver
        driver.get('https://asoftmurmur.com/blog/')
        title = driver.title
        print(title)
        assert title == 'A Soft Murmur'

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def tearDown(self):
        print('Koniec testu')