from abc import *
class School(ABC):
    @abstractmethod
    def Marks(self):
        pass
    def getPercentage(self):
        pass
        

class StudentA(School):
    def __init__(self,sub1,sub2,sub3):
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
        self.tot=self.sub1+self.sub2+self.sub3

    # overriding abstract method
    def Marks(self):
        print("marks of Subject 1:",self.sub1)
        print("marks of Subject 2:",self.sub2)
        print("marks of Subject 3:",self.sub3)
        print("Total:",self.tot)
            
		

class StudentB(School):
    def __init__(self,sub1,sub2,sub3,sub4):
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
        self.sub4=sub4
        self.tot=self.sub1+self.sub2+self.sub3+self.sub4
    def Marks(self):
        print("marks of Subject 1:",self.sub1)
        print("marks of Subject 2:",self.sub2)
        print("marks of Subject 3:",self.sub3)
        print("marks of Subject 4:",self.sub4)
        print("Total:",self.tot)
            

class DisplayA(StudentA):
    def getPercentage(self):
        per=self.tot/3
        print("Percentage:",per)

class DisplayB(StudentB):
    def getPercentage(self):
        per=self.tot/4
        print("Percentage:",per)

# Driver code
R = StudentA(90,90,90)
R.Marks()

K = DisplayA(90,90,90)
K.getPercentage()

R = StudentB(80,80,80,80)
R.Marks()

K = DisplayB(80,80,80,80)
K.getPercentage()
