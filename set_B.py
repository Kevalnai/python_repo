class File_operation:
    def get_data(self,a,b):
        self.a=a
        self.b=b

    def file_write(self):
        self.f1=open("one.txt",'w')
        self.f2=open("two.txt",'w')
        self.f1.write(a)
        self.f2.write(b)
    def file_join(self):
        data=a+" "+b
        self.f3=open("data.txt",'w')
        self.f3.write(data)

    def display(self):
        self.f3=open("data.txt",'r')
        print(self.f3.read())

    def Current_position(self):
        print("Cursor Position of file 1:",self.f1.tell())
        print("Cursor Position of file 2:",self.f2.tell())
        print("Cursor Position of file 3:",self.f3.tell())


a=input("Enter second String")
b=input("Enter sencond String")
f=File_operation()
f.file_write()
f.file_join()
f.display()
f.Current_position()
