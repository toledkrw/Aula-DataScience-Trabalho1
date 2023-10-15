import unittest, sys, os, shutil
sys.path.append(os.getcwd())

from utils.PathUtils import PathUtils


class tests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = "../DATA/test"


    def cleanUp(self):
        if (not os.path.exists(self.path)):
            return

        shutil.rmtree(self.path)


    def setUp(self):
        self.cleanUp()

    def tearDown(self):
        self.cleanUp()

    
    def test_checkPath(self):
        self.assertFalse(PathUtils.checkPath(self.path))
        
        os.makedirs(self.path)
        
        self.assertTrue(PathUtils.checkPath(self.path))

    def test_createPath(self):
        self.assertFalse(PathUtils.checkPath(self.path))
        
        PathUtils.createPath(self.path)
        
        self.assertTrue(PathUtils.checkPath(self.path))
        
        

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(tests)
    unittest.TextTestRunner(verbosity=2).run(suite)


main()