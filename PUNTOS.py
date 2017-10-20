class PUNTO:
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __repr__(self):
        return "(%.1f, %.1f)" % (self.x, self.y)
