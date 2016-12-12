import os
import app
import unittest
import tempfile
from io import BytesIO

class appTestCase(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def tearDown(self):
    	pass

    def test_upload(self):
        """
        Test: file upload correctly returns uploaded file.
        
        Compares uploaded file contents sent in POST request to response contents.
        """
    	rv = self.app.post('/', data = {'file': (BytesIO('picture file contents'), 'testfile.txt')} )
    	assert 'picture file contents' in rv.data 

if __name__ == "__main__":
	unittest.main()