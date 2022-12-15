# Ethan coutts 
# This project to create a program that manages a hospital easier


# THis is the class I am doing, Doctors


class Doctor:
    
    def __init__(self):
        self.id = "None"
        self.name = "None"
        self.spec = "None"
        self.hours = "None"
        self.qual = "None"
        self.room = "None"

# This function formats the DR info


    def formatDrInfo(self,list_to_convert):
        self.converted_string = '_'.join(list_to_convert)
        return self.converted_string + '\n'



# This function is the input for DR info

    def enterDrInfo(self):
        self.id = input("Enter the doctor's ID:\n\n")
        self.name = input("Enter the doctor's name:\n\n")
        self.spec = input("Enter the doctor's specility:\n\n")
        self.hours = input("Enter the doctor's time slot:\n\n")
        self.qual = input("Enter the doctor's qualification:\n\n")
        self.room = input("Enter the doctor's room number:\n\n")
        return [self.id,self.name,self.spec,self.hours,self.qual,self.room]


# This function reads the data on the Doctors file
    def readDoctorsFile(self):
        self.open_file = open("doctors.txt", "r")
        self.test_list = self.open_file.readlines()
        self.open_file.close()
        return self.test_list

    def searchDoctorById(self):
        self.doctor_list = self.readDoctorsFile()
        self.new_list = []
        
        for n in range(len(self.doctor_list)):
            self.new_list.append([])
            self.new_list[n] = self.doctor_list[n].split("_")

        self.query = input("\n Enter the doctors ID:\n\n")
        
        self.flag = False
        for n in range(len(self.new_list)):
            if self.new_list[n][0] == self.query:
                self.displayDoctorInfo(self.new_list[n])
                self.flag = True
        if self.flag == False:
            print("Cannot find doctor with that ID, try again")


# search DR by there name
    def searchDoctorByName(self):
        self.doctor_list = self.readDoctorsFile()
        self.new_list = []
        for n in range(len(self.doctor_list)):
            self.new_list.append([])
            self.new_list[n] = self.doctor_list[n].split("_")

        self.query = input("\n Enter the doctor name:\n\n")
        
        self.flag = False
        for n in range(len(self.new_list)):
            if self.new_list[n][1] == self.query:
                self.displayDoctorInfo(self.new_list[n])
                self.flag = True
        if self.flag == False:
            print("Can't find the doctor with the same name on the system")

# Displays the Doctors info from the text file 
    def displayDoctorInfo(self,doctor_list):
        self.doctor_list = doctor_list
        self.doctor_list[4] = self.doctor_list[4].upper() #capitalizes qualifications due to file inconsistancy
        print(f"{'Id': <5}{'Name': <20}{'Specialty': <15}{'Timing': <15}{'Qualification': <15}{'Room Number': <0}"+'\n')
        print(f"{self.doctor_list[0]: <5}{self.doctor_list[1]: <20}{self.doctor_list[2]: <15}{self.doctor_list[3]: <15}{self.doctor_list[4]: <15}{self.doctor_list[5]: <0}")


# edits the current Doctors info
    def editDoctorInfo(self):
        self.doctor_list = self.readDoctorsFile()
        self.new_list = []
        for n in range(len(self.doctor_list)):
            self.new_list.append([])
            self.new_list[n] = self.doctor_list[n].split("_")

        self.query = input("Please enter the id of the doctor that you want to edit their information:\n\n")
        
        self.flag = False
        for n in range(len(self.new_list)):
            if self.new_list[n][0] == self.query:
                self.new_list[n][1] = input("\nEnter new Name:\n\n")
                self.new_list[n][2] = input("\nEnter new Specilist in:\n\n")
                self.new_list[n][3] = input("\nEnter new Time slot: \n\n")
                self.new_list[n][4] = input("\nEnter new Qualification: \n\n")
                self.new_list[n][5] = input("\nEnter new Room number:\n\n")
                self.doctor_list[n] = self.formatDrInfo(self.new_list[n])
                self.writeListOfDoctorsToFile(self.doctor_list)
                self.flag = True
        if self.flag == False:
            print("Can't find the doctor with the same ID on the system\n")

    def displayDoctorsList(self):
        self.doctor_list = self.readDoctorsFile()
        self.new_list = []

        for n in range(len(self.doctor_list)):
            self.new_list.append([])
            self.new_list[n] = self.doctor_list[n].split("_")
        
        del self.new_list[0] 
    
        print(f"{'Id': <5}{'Name': <20}{'Specialty': <15}{'Timing': <15}{'Qualification': <15}{'Room Number': <0}"+'\n')
        for n in range(len(self.new_list)):
            print(f"{self.new_list[n][0]: <5}{self.new_list[n][1]: <20}{self.new_list[n][2]: <15}{(self.new_list[n][3].lower()): <15}{(self.new_list[n][4].upper()): <15}{self.new_list[n][5]: <0}")

    def writeListOfDoctorsToFile(self,doctor_list):
        self.open_file = open("doctors.txt", "w")
        self.index = 0
        for entries in doctor_list:
            self.open_file.write(doctor_list[self.index])
            self.index +=1
        self.open_file.close()

    def addDrToFile(self):
        self.doctor_to_add = self.enterDrInfo()
        self.doctor_to_add = self.formatDrInfo(self.doctor_to_add)
        self.doctor_list = self.readDoctorsFile()
        
        self.index = 0
        for entries in self.doctor_list:
            if self.doctor_list[self.index].endswith('\n') == False:
                self.doctor_list[self.index] = self.doctor_list[self.index] + '\n'
            self.index += 1

        self.doctor_list.append(self.doctor_to_add)
        self.writeListOfDoctorsToFile(self.doctor_list) 