import unittest, sys, os, shutil
sys.path.append(os.getcwd())

from utils.JsonUtils import JsonUtils


class tests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = "../DATA/test"


    def cleanUp(self):
        if (not os.path.exists(self.path)):
            return

        shutil.rmtree(self.path)

    def createPath(self):
        if (not os.path.exists(self.path)):
            os.makedirs(self.path)


    def setUp(self):
        self.createPath()

    def tearDown(self):
        self.cleanUp()
        

    def test_writeJson(self):
        test_data = {"test": "test"}
        
        JsonUtils.writeJson(test_data, self.path + "/test.json")
        
        file = os.listdir(self.path)
        self.assertEqual(len(file), 1)
        
        

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(tests)
    unittest.TextTestRunner(verbosity=2).run(suite)


main()