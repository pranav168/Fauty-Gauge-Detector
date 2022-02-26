import unittest
from detector import detector

class test_detector(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def testing_stable_gauge(self):
        val1=detector('stable-needle2.mp4', cropX1=340, cropY1=380, cropX2=530, cropY2=570).detect() 
        val2=detector('stable-needle.mp4', cropX1=180, cropY1=350, cropX2=350, cropY2=550).detect() 
        self.assertEqual(val1, 1)
        self.assertEqual(val2, 1)

    def testing_defected_gauge(self):
        val1=detector('needle2.mp4', 1, 42, 1180, 1290).detect() 
        val2=detector('needle.mp4', cropX1=1, cropY1=100, cropX2=900, cropY2=1000).detect() 
        self.assertEqual(val1, 0)
        self.assertEqual(val2, 0)
       
if __name__=='__main__':
    unittest.main()