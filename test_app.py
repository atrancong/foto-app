import os
import app
import unittest
import tempfile
from io import BytesIO

class appTestCase(unittest.TestCase):

    def setUp(self):
        #self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        #flaskr.init_db()

    def tearDown(self):
    	pass
        #os.close(self.db_fd)
        #os.unlink(flaskr.app.config['DATABASE'])

    def test_upload(self):
    	rv = self.app.post('/', data = {'file': (BytesIO('picture file contents'), 'testfile.txt')} )
    	#print rv.data
    	assert 'picture file contents' in rv.data 

if __name__ == "__main__":
	unittest.main()