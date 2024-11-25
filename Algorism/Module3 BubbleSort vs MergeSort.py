
import random
from datetime import datetime, timedelta
import time 
class Patient:
    def __init__(self, patient_id, name, age, diagnosis=None, admission_date=None):
        self.patient_id = patient_id
        self.name = name
        self.age = age 
        self.diagnosis = diagnosis
        self.admission_date = admission_date 

    def to_dict(self):
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "age": self.age, 
            "diagnosis": self.diagnosis,
            "admission_date": self.admission_date 
        }
next_id = 1
patients=[]
def add_patient(name, age, diagnosis, admission_date):
    global next_id
    patient = Patient(next_id, name, age, diagnosis, admission_date)
    patients.append(patient)
    next_id += 1 

def generate_patients(num_patients=50):
    diagnoses= ["Flu", "Cold", "Fracture", "Diabetes", "Hypertension", "Asthma", "Allergy", "Migraine", "Anemia", "Arthritis"]
    names=['John','Rose','James','Leah','Randy','Pat','Tom']
    for _ in range(num_patients):
        name = random.choice(names)
        age = random.randint(0, 99)
        diagnosis = random.choice(diagnoses)
        admission_date = datetime.fromtimestamp(random.randint(0, int(datetime.now().timestamp()))).strftime('%Y-%m-%d')
        add_patient(name, age, diagnosis, admission_date) 

generate_patients(50)
patients_database = [patient.to_dict() for patient in patients]
#print(patients_database)


def bubble_sort(arr, key):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][key] > arr[j + 1][key]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def mergesort(arr, key):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid], key)
    right = mergesort(arr[mid:], key) 
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

bubble_times = []
merge_times = []
for i in range (10):
    DB1 = patients_database.copy()
    DB2 = patients_database.copy()
    start_time = time.time()
    bubble_sort(DB1, 'age')
    end_time = time.time()
    bubble_times.append(end_time - start_time)

    start_time2 = time.time()
    mergedResult=mergesort(DB2, 'age')
    end_time2 = time.time()
    merge_times.append(end_time2 - start_time2)
avg_bubble = sum(bubble_times) / len(bubble_times)
avg_merge = sum(merge_times) / len(merge_times)
print(f"BubbleSort TimeAvg: {avg_bubble:.5f} seconds for patient db of {len(DB1)} size")
print(f"MergeSort TimeAvg: {avg_merge:.5f} seconds for patient db of {len(DB2)} size")

print(f"bubbleSort result")
for patient in DB1:
    print(patient)

print(f"mergeSort result")
for patient in mergedResult:
    print(patient)
 
 
