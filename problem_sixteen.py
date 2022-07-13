class namefromuser:
    def getstring(self):
        self.name=input("enter string from keyboard:")
    def printstring(self):
        print( self.name.upper())
obj1=namefromuser()
obj1.getstring()
obj1.printstring()
