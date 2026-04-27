from fastapi import FastAPI
from pydantic import Basemodel , Field, computed_field
from typing import Literal,Annotated
import pickle
import pandas as pd 

#import the ml model
with open('model.pkl','rb') as f:
    model = pickle.load(f)

app = FastAPI

#pydantic model to validate incoming data
class UserInput(Basemodel):

    age: Annotated[int, Field(...,gt=0 ,lt=120, description='age of the user')]
    weight: Annotated[float,Field(..., gt=0,description='weight of the user')]
    height:Annotated[float,Field(..., gt=0,lt=2.5,description='height of the user')]
    income_lpa:Annotated[float,Field(..., gt=0,description='Annual salary of the user')]
    smoker:Annotated[bool,Field(..., description='is user a smoker')]
    city:Annotated[str ,Field(...,description='is user a smoker')]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description='Occupation of the user')]


@computed_field
@property
def bmi(self) -> float:
    return self.weitght/(self.height**2)

@computed_field
@property
def lifestyle_risk(self) -> str:
  if self.smoker["smoker"] and self.bmi["bmi"]> 30:
    return "high"
  elif self.smoker["smoker"] or self.bmi["bmi"]>27:
        return "medium"
  else:
    return "low"
  

@computed_field
@property 
def age_group(self) -> str:
   if self.age < 25:
      return "young"
   elif self.age < 50:
      return"Adult"
   elif self.age < 60:
      return "middle_aged"
   return "senior"

@computed_field
@property
      