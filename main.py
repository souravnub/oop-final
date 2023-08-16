#doctor class
class Doctor:
    def __init__(self, id, name, specialization, workingTime, qualification, roomNumber):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.workingTime = workingTime
        self.qualification = qualification
        self.roomNumber = roomNumber

    def getId(self):
        return self.id

    def changeRoom(self, newRoomNumber):
        self.roomNumber = newRoomNumber

    def __str__(self):
        return f'{self.id}_{self.name}_{self.specialization}_{self.workingTime}_{self.qualification}_{self.roomNumber}'

#doctor manager class
class DoctorManager:
    def __init__(self):
        self.doctors = []
    
    def format_dr_info(self, docObj):
        return docObj.__str__()
    
    def get_doctors_ids(self):
        self.read_doctors_file()
        
        doctors = self.doctors
        idsList = []
        for doctorObj in doctors:
            idsList.append((self.format_dr_info(doctorObj)).split('_')[0])
        
        return idsList
    def enter_dr_info(self):
        info_prompts = ['ID', 'name', 'specility', 'timing (e.g., 7am-10pm)', 'qualification', 'romm number']
        info = []
        
        for prompt in info_prompts: 
            answer = input(f"Enter the doctor’s {prompt}: ")
            info.append(answer)


        return Doctor(*info)

    def read_doctors_file(self):
        self.doctors = []
        doctors_file = open('doctors.txt', 'r')
        doctors_info = doctors_file.read().split('\n')


        # not selecting whole list, because first string element will be properties: id_name_specilization....
        for doctor_info in doctors_info[1:]:
            doctor_info_list = []
            
            for info_val in doctor_info.split('_'):
                doctor_info_list.append(info_val)

            self.doctors.append(Doctor(*doctor_info_list))  

        doctors_file.close()   

    def display_doctor_info(self, doctor):
        self.read_doctors_file()

        print ("\n{:<8} {:<15} {:<15} {:<15} {:<15} {:<15}".format('Id','Name','Speciality','Timing','Qualification','Room Number'))
        print ("\n{:<8} {:<15} {:<15} {:<15} {:<15} {:<15}\n".format(doctor.id,doctor.name,doctor.specialization,doctor.workingTime,doctor.qualification,doctor.roomNumber))
        

    def search_doctor_by_id(self):
        self.read_doctors_file()

        id = input('Enter the doctor Id: ')

        doctorFound = None
        for doctor in self.doctors:
            if(doctor.getId() == id):
                    doctorFound = doctor

        if(not doctorFound):
                print("Can't find the doctor....")
                return

        self.display_doctor_info(doctorFound)

    def search_doctor_by_name(self):
        self.read_doctors_file()

        name = input("Enter the doctor name: ")

        doctorFound = None
        for doctor in self.doctors:
            
            if(doctor.name.lower() == name.lower()):
                doctorFound = doctor
            
        if(not doctorFound):
            print("Can't find the doctor....")
            return
        self.display_doctor_info(doctorFound)

