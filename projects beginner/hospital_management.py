# hospital Management System 

class Patient:
    def __init__(self, patient_id, name, age, gender, contact) -> None:
        self.__patient_id = patient_id
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__contact = contact
    def get_patientDetails(self):
        return {
            'patient_id': self.__patient_id,
            'name': self.__name,
            'age': self.__age,
            'gender': self.__gender,
            'contact': self.__contact
        }
    
class Doctor:
    def __init__(self, doctor_id, name, specialization) -> None:
        self.__doctor_id = doctor_id
        self.__name = name
        self.__specialization = specialization

    def get_doctorDetails(self):
        return {
            'Doctor ID': self.__doctor_id,
            'Name': self.__name,
            'Specialization': self.__specialization
        }
class 

patient1 = Patient(1, 'ravi', 23, 'male', '+9198756653')
