class Patient:
    def __init__(self, patient_id, name, age, gender, contact):
        self.__patient_id = patient_id
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__contact = contact
        self.__assigned_doctor = None

    def get_patient_info(self):
        return {
            'Patient ID': self.__patient_id,
            'Name': self.__name,
            'Age': self.__age,
            'Gender': self.__gender,
            'Contact': self.__contact
        }

    def assign_doctor(self, doctor):
        self.__assigned_doctor = doctor

    def get_assigned_doctor(self):
        return self.__assigned_doctor


class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.__doctor_id = doctor_id
        self.__name = name
        self.__specialization = specialization

    def get_doctor_info(self):
        return {
            'Doctor ID': self.__doctor_id,
            'Name': self.__name,
            'Specialization': self.__specialization
        }


class MedicalRecord:
    def __init__(self):
        self.__records = {}

    def add_record(self, patient, doctor, diagnosis, medication):
        self.__records[patient.get_patient_info()['Patient ID']] = {
            'Patient': patient.get_patient_info(),
            'Doctor': doctor.get_doctor_info(),
            'Diagnosis': diagnosis,
            'Medication': medication
        }

    def get_records(self):
        return self.__records


# Test the system
if __name__ == "__main__":
    # Create patients
    patient1 = Patient(1, 'John Doe', 30, 'Male', '123-456-7890')
    patient2 = Patient(2, 'Jane Smith', 25, 'Female', '987-654-3210')

    # Create doctors
    doctor1 = Doctor(101, 'Dr. Ahmed', 'Cardiologist')
    doctor2 = Doctor(102, 'Dr. Fatima', 'Pediatrician')

    # Create medical records
    medical_records = MedicalRecord()
    medical_records.add_record(patient1, doctor1, 'Heart condition', 'Aspirin')
    medical_records.add_record(patient2, doctor2, 'Common cold', 'Antibiotics')
    # Display records
    
    print(medical_records.get_records()[1])
