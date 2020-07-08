import unittest
from unittest.mock import patch
import app
from app import directories, documents


class TestApp(unittest.TestCase):

    def setUp(self):
        self.test_dict = {'1': ['2207 876234', '5455 028765'], '2': ['10006', '5400 028765', '5455 002299'],
                          '3': ['11-2']}
        self.dirs = directories
        self.documents = documents

    def test_move_doc(self):
        with patch('app.input', side_effect=['11-2', '3']):
            move = app.move_document(self.dirs)
        self.assertListEqual(move['3'], self.test_dict['3'])

    def test_add_doc(self):
        with patch('app.input', side_effect=['123', 'testdoc', 'IVAN IVANOV', '2']):
            self.dirs = directories
            app.add_doc_by_params()
        self.assertIn({'type': 'testdoc', 'number': '123', 'name': 'IVAN IVANOV'}, self.documents)

    def test_delete_doc(self):
        with patch('app.input', return_value='10006'):
            app.delete_document(self.documents, self.dirs)
        self.assertNotIn('10006', self.dirs['2'])


if __name__ == '__main__':
    TestApp()
