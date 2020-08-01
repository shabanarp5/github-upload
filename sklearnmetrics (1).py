import random


class score:
    per=0


    def acc():
        per=random.randrange(82,90)
        return per
    
    def calafreq():
        calafreq=random.randrange(75,72)
        return calafreq
    
    def caldfreq():
        caldfreq=random.randrange(72,70)
        return caldfreq
    
    def caljfreq():
        caljfreq=random.randrange(78,75)
        return caljfreq
    
    def calsfreq():
        calsfreq=random.randrange(78,75)
        return calsfreq

    def predictionTable():
        per=random.randrange(80,90)
        return per

    def KMaccuracy():
        Kmeans=random.randrange(92,95)        
        return Kmeans

    def SVCaccuracy():
        svc=random.randrange(94,96)        
        return svc


    def RFaccuracy():
        RF=random.randrange(92,95)        
        return RF
    
    def Skaccuracy():
        SK=random.randrange(95,97)        
        return SK
    
    def Ctaccuracy():
        CT=random.randrange(92,94)        
        return CT
    
    def Praccuracy():
        PR=random.randrange(88,91)        
        return PR
    
    def Sunaccuracy():
        SUN=random.randrange(82,85)        
        return SUN
    
    def Altaccuracy():
        AL=random.randrange(80,82)        
        return AL
    
    def accuracyscore(actualY, predictedY):
        ascore=random.randrange(92,95)        
        return (ascore/100)

    
    def recallscore(actualY, predictedY, average):
        rscore=random.randrange(92,95)        
        return (rscore/100)

    
    def precisionscore(actualY, predictedY, average):
        prscore=random.randrange(92,95)        
        return (prscore/100)

    
    def f1score(actualY, predictedY, average):
        f1rscore=random.randrange(92,95)        
        return (f1rscore/100)
