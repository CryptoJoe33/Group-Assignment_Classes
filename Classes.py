# CPRG-216-L
# Assignment - Classes
# Author: Joey Adam

class Facility:

    def __init__(self):
        self.fac_name = "None"

    def addFacility(self):
        self.new_file = open("facilities.txt", "r")
        self.fac_list = self.new_file.readlines()
        self.new_file.close()

        self.fac_name = input("Enter Facility name: \n\n")

        self.fac_list.append(self.fac_name)

        self.writeListOffacilitiesToFile(self.fac_list)

    def displayFacilities(self):
        self.new_file = open("facilities.txt", "r")
        self.fac_list = self.new_file.readlines()
        self.new_file.close()
        self.fac_list[0] = "The " + self.fac_list[0]

        for i in range(len(self.fac_list)):
            if self.fac_list[i].endswith('\n') == False:
                print(self.fac_list[i]+'\n')
            else:
                print(self.fac_list[i])

    def writeListOffacilitiesToFile(self, write):
        self.new_file = open("facilities.txt", "w")
        self.index = 0

        for entries in write:
            if write[self.index].endswith('\n') == False:
                write[self.index] = write[self.index] + '\n'
            self.new_file.write(write[self.index])
            self.index += 1
        self.new_file.close()

class Laboratory:

    def __init__(self):
        self.lab_name = "None"
        self.cost = "None"

    def formatLabInfo(self):
        return str(self.lab_name) + '_' + str(self.cost)
    
    def addLaboratory(self):
        self.new_file = open("laboratories.txt", "r")
        self.lab_list = self.new_file.readlines()
        self.new_file.close()

        self.lab_name = input("Enter lab name: \n")
        self.lab_list.append(self.lab_name)

        self.cost = input("Enter lab cost: \n")
        self.lab_list.append(self.lab_name)

        self.writeListOflabToFile(self.lab_list)

    def displaylab(self):
        self.new_file = open("laboratories.txt", "r")
        self.lab_list = self.new_file.readlines()
        self.new_file.close()
        self.lab_list[0] = "The " + self.lab_list[0]

        for i in range(len(self.lab_list)):
            if self.lab_list[i].endswith('\n') == False:
                print(self.lab_list[i]+'\n')
            else:
                print(self.lab_list[i])

    def readLabsFile(self):
        self.new_file = open("laboratories.txt", "r")
        self.test_list = self.new_file.readlines()
        self.new_file.close()
        return self.test_list

    def enterLabInfo(self):
        self.lab_name = input("Enter the doctor's ID:\n\n")
        self.cost = input("Enter the doctor's name:\n\n")
        return [self.id,self.name,self.spec,self.hours,self.qual,self.room]

    def writeListOflabToFile(self,write):
        self.new_file = open("laboratories.txt", "w")
        self.index = 0

        for entries in write:
            if write[self.index].endswith('\n') == False:
                write[self.index] = write[self.index] + '\n'
            self.new_file.write(write[self.index])
            self.index += 1
        self.new_file.close()
