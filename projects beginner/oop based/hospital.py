# hospital management system 
class Patient:
    def __init__(self,PatientID,PatientName,PatientAge,PatientContact):
        self.__PatientID = PatientID
        self.__PatientName = PatientName
        self.__PatientAge = PatientAge
        self.__PatientContact = PatientContact
    def getDetails(self):
        return {
            'PatientID': self.__PatientID,
            'PatientName': self.__PatientName,
            'PatientAge': self.__PatientAge,
            'PatientContact': self.__PatientContact
        }
class Doctor:
    def __init__(self,id, name, Specialisation):
        self.__id = id
        self.__name = name
        self.__Specialisation = Specialisation
    def get_doctor_details(self):
       return{
           'doctor_id' : self.__id,
        'doctor_name' : self.__name,
        'doctor_Specialisation' : self.__Specialisation
    }
class MedicalReport:
    def __init__(self):
        self.__records = {}

    def AddRecords(self, Patient, doctor, diagnosys, medication):
        self.__records[Patient.getDetails()['PatientID']] = {

            'Patient': Patient.getDetails(),
            'Doctor': doctor.get_doctor_details(),
            'Diagnosys': diagnosys,
            'Medication': medication
        }
    
    def getRecords(self):
        return self.__records


# main code 
p1 = Patient('Nayti_23','Akshay',17,'+919068515580')
p2 = Patient('Nayti_14','Kartikey',18,'+9199996851980')
d1 = Doctor(4515,'Manish','Neuro_Surgeon')
d2 = Doctor(4516,'Jay','Heart_Surgeon')

res = MedicalReport()
res.AddRecords(p1, d1, 'heart Problem', 'asprin')
print(res.getRecords()['Nayti_23']['Doctor'])                                   
