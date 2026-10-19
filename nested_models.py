from pydantic import BaseModel, ValidationError, EmailStr, AnyUrl, Field,field_validator,model_validator,computed_field
from typing import Dict, Optional, Annotated, List
class Address(BaseModel):
    city : str
    state :str
    pin: str

class Patient(BaseModel):
    name : str
    gender : str 
    age : int
    address : Address

address_dict = {
    "city": "Bangalore",
    "state": "Karnataka",
    "pin": "560001"
}
address = Address(**address_dict)
patient_dict = {
    "name": "krishan",  
    "gender": "Male",
    "age": 30,
    "address": address
}
patient = Patient(**patient_dict)
print(patient)      
print(patient.address.city)
print(patient.address.state)
print(patient.address.pin)

temp = patient.model_dump(exclude={'address'})
temp1 = patient.model_dump_json()
print(temp1)
print(type(temp1))
#unset=true will remove the fields with value None from the output

with open("patient.json", "w") as f:
    f.write(temp1)