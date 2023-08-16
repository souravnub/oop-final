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
    
        

