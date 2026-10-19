from pydantic import BaseModel, ValidationError, EmailStr, AnyUrl, Field,field_validator,model_validator,computed_field
from typing import Dict, Optional, Annotated, List


class Patient(BaseModel):
    name: Annotated[
        str,
        Field(
            min_length=1,
            max_length=100,
            title="Name of the patient",
            description="Give the name of the patient in less than 100 characters",
            examples=["krishan"]
        )
    ]

    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: float = Field(gt=0)
    married: Annotated[
        bool,
        Field(default=False, description="Is the patient married?")
    ]
   
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]
    @computed_field
    @property
    def is_senior_citizen(self) -> bool:
        return self.age > 60
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency_contact' not in model.contact_details:
            raise ValueError("Emergency contact information is required for patients over 60 and under 5")
        return model

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'example.com']  
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("Invalid email domain")
        return value
    @field_validator('age', mode='before')
    @classmethod
    def age_validator(cls,value):
        if 0<value<120:
            return value
        else:
            raise ValueError("Age must be between 0 and 120")
    

def insert_patient_data(patient: Patient):
    print(f"Patient name: {patient.name} and age: {patient.age}")
    print("Inserted into the database")


def update_patient_data(patient: Patient):
    print(f"Patient name: {patient.name} and age: {patient.age}")
    print(f"Married: {patient.married}")
    print(f"Is senior citizen: {patient.is_senior_citizen}")
    print("Updated the database")


patient_info = {
    "name": "krishu",
    "email": "krishu@example.com",
    "linkedin_url": "https://www.linkedin.com/in/krishu",
    "age": 20,
    "weight": 70.5,
    "allergies": ["peanuts"],
    "contact_details": {
        "email": "krishu@example.com",
        "phone": "1234567890"
    }
}

try:
    patient1 = Patient(**patient_info)
    insert_patient_data(patient1)

except ValidationError as e:
    print(e)