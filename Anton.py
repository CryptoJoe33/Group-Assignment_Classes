# CPRG-216-L
# Project - Classes
# Author: Anton Koulikov

# Class 4: Patient
class Patient:

    # Patient properties
    def __init__(self):
        self.pid = " "
        self.name = " "
        self.disease = " "
        self.gender = " "
        self.age = " "

    # Patient methods
    # Formats patient information to be added to the file
    def formatPatientInfo(self, listToConvert):
        self.convertedString = "_".join(listToConvert)
        return self.convertedString + "\n"

    # Asks the user to enter the patient info
    def enterPatientInfo(self):
        self.id = input("Enter the patient's ID:\n")
        self.name = input("Enter the patient's Name:\n")
        self.disease = input("Enter the patient's Disease:\n")
        self.gender = input("Enter the patient's Gender:\n")
        self.age = input("Enter the patient's Age:\n")
        return [self.id, self.name, self.disease, self.gender, self.age]

    # Reads from file patients.txt
    def readPatientsFile(self):
        self.openFile = open("patients.txt", "r")
        self.testList = self.openFile.readlines()
        self.openFile.close()
        return self.testList

    # Searches for a patient using their ID
    def searchPatientById(self):
        self.patientList = self.readPatientsFile()
        self.newList = []

        for i in range(len(self.patientList)):
            self.newList.append([])
            self.newList[i] = self.patientList[i].split("_")

        self.patientId = input("\nEnter the patient's ID:\n")

        self.bool = False
        for i in range(len(self.newList)):
            if self.newList[i][0] == self.patientId:
                self.displayPatientInfo(self.newList[i])
                self.bool = True
        if self.bool == False:
            print("Cannot find any patient with the ID entered in the database.")

    # Displays patient info
    def displayPatientInfo(self, patientList):
        self.patientList = patientList
        print(f"{'ID': <5}{'Name': <15}{'Disease': <15}{'Gender': <15}{'Age': <0}" + '\n')
        print(f"{self.patientList[0]: <5}{self.patientList[1]: <15}{self.patientList[2]: <15}{self.patientList[3]: <15}{self.patientList[4]: <0}")

    # Asks the user to edit patient information
    def editPatientInfo(self):
        self.patientList = self.readPatientsFile()
        self.newList = []
        for i in range(len(self.patientList)):
            self.newList.append([])
            self.newList[i] = self.patientList[i].split("_")

        self.patientId = input("Enter the ID of the patient which requires their information to be edited:\n")

        self.bool = False

        for i in range(len(self.newList)):
            if self.newList[i][0] == self.patientId:
                self.newList[i][1] = input("Enter new Name: \n")
                self.newList[i][2] = input("Enter new Disease: \n")
                self.newList[i][3] = input("Enter new Gender: \n")
                self.newList[i][4] = input("Enter new Age (years): \n")
                self.patientList[i] = self.formatPatientInfo(self.newList[i])
                self.writeListOfPatientsToFile(self.patientList)
                self.bool = True
        if self.bool == False:
            print("Cannot find any patient with the ID entered in the database.")

    # Displays the list of patients
    def displayPatientsList(self):
        self.patientList = self.readPatientsFile()
        self.newList = []

        for i in range(len(self.patientList)):
            self.newList.append([])
            self.newList[i] = self.patientList[i].split("_")

        for i in range(len(self.newList)):
            print(f"{self.newList[i][0]: <5}{self.newList[i][1]: <15}{self.newList[i][2]: <15}{(self.newList[i][3]): <15}{self.newList[i][4]: <0}")

    # Writes a list of patients into the patients.txt file
    def writeListOfPatientsToFile(self, patientList):
        self.openFile = open("patients.txt", "w")
        self.index = 0

        for i in patientList:
            self.openFile.write(patientList[self.index])
            self.index += 1
        self.openFile.close()

    # Adds a new patient to the patients.txt file
    def addPatientToFile(self):
        self.patientToAdd = self.enterPatientInfo()
        self.patientToAdd = self.formatPatientInfo(self.patientToAdd)
        self.patientList = self.readPatientsFile()

        self.index = 0

        for i in self.patientList:
            if self.patientList[self.index].endswith("\n") == False:
                self.patientList[self.index] = self.patientList[self.index] + "\n"
            self.index += 1

        self.patientList.append(self.patientToAdd)
        self.writeListOfPatientsToFile(self.patientList)

Laboratory = 0
Doctor = 0
Facility = 0
# Class 5: Management
class Menu:

    def displayMenu(self):
        self.repeat = True
        while self.repeat:
            self.option = input("Welcome to Alberta Hospital (AH) Managment system\nSelect from the following options, or select 0 to stop:\n1 - Doctors\n2 - Facilities\n3 - Laboratories\n4 - Patients\n\n")

            if int(self.option) == 1:
                self.series = True
                self.obj_handle = Doctor()
                while self.series:
                    self.option = input("Doctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n\n")
                    if int(self.option) == 1:
                        self.obj_handle.displayDoctorsList()
                        print("\nBack to the previous Menu")
                    elif int(self.option) == 2:
                        self.obj_handle.searchDoctorById()
                        print("\nBack to the previous Menu")
                    elif int(self.option) == 3:
                        self.obj_handle.searchDoctorByName()
                        print("\nBack to the previous Menu")
                    elif int(self.option) == 4:
                        self.obj_handle.addDrToFile()
                        print("\nBack to the previous Menu")
                    elif int(self.option) == 5:
                        self.obj_handle.editDoctorInfo()
                        print("\nBack to the previous Menu")
                    elif int(self.option) == 6:
                        self.series = False
                        print("")

            elif int(self.option) == 2:
                self.series = True
                self.obj_handle = Facility()
                while self.series:
                    self.option = input("Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n\n")
                    if int(self.option) == 1:
                        self.obj_handle.displayFacilities()
                        print("Back to the previous Menu")
                    elif int(self.option) == 2:
                        self.obj_handle.addFacility()
                        print("Back to the previous Menu")
                    elif int(self.option) == 3:
                        self.series = False
                    else:
                        self.repeat = False

            elif int(self.option) == 3:
                self.series = True
                self.obj_handle = Laboratory()
                while self.series:
                    self.option = input("Laboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu\n\n")
                    if int(self.option) == 1:
                        self.obj_handle.displayLabsList()
                    elif int(self.option) == 2:
                        self.obj_handle.addLabToFile()
                    elif int(self.option) == 3:
                        self.series = False
                    print("Back to the previous Menu\n")

            elif int(self.option) == 4:
                self.series = True
                self.obj_handle = Patient()
                while self.series:
                    self.option = input("Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n\n")
                    if int(self.option) == 1:
                        self.obj_handle.displayPatientsList()
                    elif int(self.option) == 2:
                        self.obj_handle.searchPatientById()
                    elif int(self.option) == 3:
                        self.obj_handle.addPatientToFile()
                    elif int(self.option) == 4:
                        self.obj_handle.editPatientInfo()
                    elif int(self.option) == 5:
                        self.series = False
                    print("Back to the previous Menu\n")

            elif int(self.option) == 0:
                print("Stopping.")
                break

            else:
                print("Error. Invalid input. Try again.")
                break


# Program
program = Menu()
program.displayMenu()