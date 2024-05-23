class Math:

    @staticmethod # not changing , they dont have access to anything
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10
    
    @staticmethod
    def pr ():
        print("Run")

    
    
print(Math.add5(5))
print(Math.add5(10))
Math.pr()
