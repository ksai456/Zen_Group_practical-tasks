import os


class Student:
    def __init__(self, first_name=None, last_name=None, standard=None, Class=None, emailid=None):
        self.first_name = first_name
        self.last_name = last_name
        self.standard = standard
        self.Class = Class
        self.emailid = emailid

    def addDetails(self, data_file):
        if not os.path.isfile(os.path.join(os.path.dirname(__file__), data_file)):
            print("in not create")
            roll_number = 1
            with open(os.path.join(os.path.dirname(__file__), data_file), 'w+') as file:
                file.write(str(roll_number))
                file.write(self.first_name+", ")
                file.write(self.last_name+", ")
                file.write(self.standard+", ")
                file.write(self.Class+", ")
                file.write(self.emailid+"\n")
        else:
            with open(os.path.join(os.path.dirname(__file__), data_file), 'r') as f:
                roll_number = len(f.readlines())
            with open(os.path.join(os.path.dirname(__file__), data_file), 'a') as f:
                roll_number += 1
                f.write(str(roll_number)+", ")
                f.write(self.first_name+", ")
                f.write(self.last_name+", ")
                f.write(self.standard+", ")
                f.write(self.Class+", ")
                f.write(self.emailid+"\n")

    def modify(self, data_file, roll_number, first_name = None, last_name = None, standard = None, Class=None, emailid =None):
        details = []
        with open(os.path.join(os.path.dirname(__file__), data_file), 'r+') as f1:
            for roll, detail in enumerate(f1.readlines()):
                detail = list(detail.replace("\n", "").split(", "))
                if roll_number == roll+1:
                    if first_name != None:
                        detail[1] = first_name
                    elif last_name != None:
                        detail[2] = last_name
                    elif standard != None:
                        detail[3] = str(standard)
                    elif Class != None:
                        detail[4] = Class
                    elif emailid != None:
                        detail[5]= emailid
                else:
                    print("roll number not found")
                details.append(detail)
        try:
            with open(os.path.join(os.path.dirname(__file__), data_file), 'w') as f:
                print("in modify write")
                for detail in details:
                    for i in detail:
                        f.write(i+", ")
                    f.write("\n")
        except  Exception:
            print(Exception)

            

        
    def getDetails(self, roll_number):
        with open(os.path.join(os.path.dirname(__file__), data_file), 'r') as f:
            for line in f.readlines():
                if str(roll_number) in line[:1]:
                    print(line, line[:1])

    def standard_file(self):
        standards = []
        with open(os.path.join(os.path.dirname(__file__), data_file), 'r') as f:
            for lines in f.readlines():
                standards.append(lines.split(", ")[4])
            standards = set(standards)
            for i in standards:
                i = i+".txt"
                with open(os.path.join(os.path.dirname(__file__), i), 'w+') as standfile:
                    with open(os.path.join(os.path.dirname(__file__), data_file), 'r') as f:
                        for lines in f.readlines():
                            if i[:1] == lines.split(", ")[4]:
                                standfile.write(lines)


    def class_file(self):
        classfile = []
        with open(os.path.join(os.path.dirname(__file__), data_file), 'r') as f:
            for lines in f.readlines():
                classfile.append(lines.split(", ")[3])
            classfile = set(classfile)
            for i in classfile:
                i = i+".txt"
                with open(os.path.join(os.path.dirname(__file__), i), 'w+') as standfile:
                    with open(os.path.join(os.path.dirname(__file__), data_file), 'r') as f:
                        for lines in f.readlines():
                            if i[:1] == lines.split(", ")[3]:
                                standfile.write(lines)


if __name__ == '__main__':
    data_file = "Master_file.txt"
    print(" 1 : Add student Details\n 2 : Modify Details\n 3 : Get Student Details")
    choice =int(input(" "))
    if  choice == 1:
        i = 1
        print("number of students details to add ")
        n = int(input())
        while i <=n:
            first_name = input('First Name : ')
            last_name =input('Last Name : ')
            standard =input('Standard : ')
            Class = input('Class : ')
            emailid = input('emailid : ')
            student = Student(first_name, last_name, standard, Class, emailid)
            student.addDetails(data_file)
            i+=1
    elif choice == 2:
        print("Enter roll no of student to modify")
        roll_number = int(input())
        print("Enter student details to  modify")
        first_name = input() if int(input("Change First name Yes : 1, No : 0 --> ")) else None
        last_name = input() if int(input("Change Last name Yes : 1, No : 0 --> ")) else None
        standard =  input() if int(input("Change standard Yes : 1, No : 0 --> ")) else None
        Class = input() if int(input("Change Class Yes : 1, No : 0 --> ")) else None
        emailid = input() if int(input("Change email Yes : 1, No : 0 --> ")) else None
        st = Student()
        st.modify(data_file, roll_number,first_name,last_name,standard,Class, emailid)
    elif choice == 3:
        s = Student()
        roll_number = int(input("Enter roll number :"))
        s.getDetails(roll_number)
        s.standard_file()
        s.class_file()
    else:
        print("Enter correct choice next time")

    
