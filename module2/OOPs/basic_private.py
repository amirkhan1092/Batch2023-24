# Hospital Manegament System 

class patient:
    def __init__(self, patient_id, patient_name, age, gender, contact):
        self.__patient_id = patient_id
        self.__patient_name = patient_name
        self.__age = age
        self.__gender = gender
        self.__contact = contact

    def get_patientInfo(self):
        return {
            'patient_id': self.__patient_id,
            'patient_name': self.__patient_name,
            'age': self.__age,
            'gender': self.__gender,
            'contact': self.__contact
        }

class doctor:
    def __init__(self, doctor_id, doctor_name, specialization):
        self.__doctor_id = doctor_id
        self.__doctor_name = doctor_name
        self.__specialiazation = specialization
    def get_doctorInfo(self):
        return{
            'doctor_name':self.__doctor_name,
            'doctor_id':self.__doctor_id,
            'specialization':self.__specialiazation
        }

class medical_records:
    def __init__(self) -> None:
        self.__records = {}

    def add_record(self, pt, dt, diagosys, medication):
        self.__records[pt.get_patientInfo()['patient_id']] = {
            'Patient': pt.get_patientInfo(),
            'Doctor': dt.get_doctorInfo(),
            'Diagosys': diagosys,
            'Medication': medication
        }
    def get_records(self):
        return self.__records

# main code 
patient1 = patient(1, 'Ravi Kumar', 23, 'Male', '+91983373784')
patient2 = patient(2, 'Saket', 34, 'Male', '+9187464632')
doctor1 = doctor(100,'Achintya','Cardiologist')
doctor2 = doctor(200,'Akshat','Neurologist')

record_reg = medical_records()
record_reg.add_record(patient1, doctor1, 'Heart Problem', 'Asprin')

print(record_reg.get_records()[1]['Patient']['patient_name'])





