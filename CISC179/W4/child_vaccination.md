# initialize  dictionary to store all patient records

```python
patient = {}

# 1. Insert Function
def insert(first_name, last_name, birthday):
   
    record_number = 1 #get patient details as input and add them to dictionary.
    
    # looping to get next record
    while record_number in patient:
        record_number += 1
        
    # Create the nested dictionary for the new patient
    patient[record_number] = {
        'First Name': first_name,
        'Last Name': last_name,
        'Birth Month': birthday
    }
    
    print("New patient recorded number: {record_number}\n")


# Verification and execution
if __name__ == "__main__":
    
    # first patient
    print("First patient info")
    nome1 = input("Insert patient first name: ")
    cognome1 = input("Insert patient last name: ")
    mese1 = int(input("Insert birthday: "))
    
    insert(nome1, cognome1, mese1)
    
    # second patient
    print("Second patient info")
    nome2 = input("Insert patient first name: ")
    cognome2 = input("Insert patient last name: ")
    mese2 = int(input("Insert birthday: "))
    
    insert(nome2, cognome2, mese2)
    
    # Verify records
    print("Verify records")
```
    for record_id, details in patient.items():
        print("Record {record_id}: {details}")
