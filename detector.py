import statsmodels.api as sm
from gauge import tester

class detector():
    def __init__(self, video, cropX1, cropY1, cropX2, cropY2):
        self.video= video
        self.cropX1 = cropX1
        self.cropY1= cropY1
        self.cropX2 = cropX2
        self.cropY2=cropY2
        
    def detect(self):
        series = tester().pixel_count(self.video, self.cropX1, self.cropY1, self.cropX2, self.cropY2)
        p_value = sm.tsa.stattools.adfuller(series)[1]
        
        if p_value >0.001:
            print('Gauge is Working Fine')
            return 1
        else:
            print('Warning: Gauge is not Working as Expected')
            return 0
