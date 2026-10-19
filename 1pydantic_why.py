from pydantic import BaseModel, ValidationError

def insert_patient_data(name : str, age : int):
    if type(name) == str and type(age) == int:
        print(f"Patient name:{name} and age:{age}")
        print("Inserted the database")
    else:
        raise TypeError("Invalid data type for name and age")

insert_patient_data("john", 30)


