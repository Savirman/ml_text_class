import unittest
import os

class TestMainFileExistence(unittest.TestCase):

    def test_main_file_existence(self):
        self.assertTrue(os.path.exists("src/main.py"), "Файл main.py не найден")

if __name__ == "__main__":
    unittest.main()
