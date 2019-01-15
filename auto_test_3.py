import unittest
from selenium import webdriver


class MainTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('Robię przygotowanie przed testami')
        self.driver = webdriver.Chrome(executable_path='C:\TestFiles\chromedriver.exe')

    def test_demo_login(self):
        driver = self.driver
        url = ('https://demobank.jaktestowac.pl')
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual(title, 'Demobank - Bankowość Internetowa - Logowanie',
                         f'Expected title differ from actual for page url: {url}')

    def test_demo_accounts(self):
        driver = self.driver
        url = ('https://demobank.jaktestowac.pl/konta.html')
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual(title, 'Demobank - Bankowość Internetowa - Konta',
                         f'Expected title differ from actual for page url: {url}')

    def test_demo_pulpit(self):
        driver = self.driver
        url = ('https://demobank.jaktestowac.pl/pulpit.html')
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual(title, 'Demobank - Bankowość Internetowa - Pulpit',
                         f'Expected title differ from actual for page url: {url}')

    def test_demo_transfer(self):
        driver = self.driver
        url = ('https://demobank.jaktestowac.pl/przelew_nowy_zew.html')
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual(title, 'Demobank - Bankowość Internetowa - Przelew',
                         f'Expected title differ from actual for page url: {url}')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
