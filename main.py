import joblib
from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Literal
import pandas as pd

model = joblib.load("Mental_health_model.pkl")

app = FastAPI()

from pydantic import BaseModel, Field

class StudentData(BaseModel):
    Age: int = Field(..., ge=10, le=100)
    Gender: Literal["Male", "Female"]
    Country:str 
    Academic_Level: Literal['Undergraduate', 'Graduate', 'High School']
    Most_Used_Platform:Literal['Facebook','LinkedIn','Instagram','Snapchat','Twitter','YouTube','TikTok','LINE','KakaoTalk','VKontakte','WhatsApp','WeChat']
    Purpose_Of_Use: Literal['Networking', 'Education', 'Entertainment', 'News']

    Avg_Daily_Usage_Hours: float = Field(..., ge=6, le=24)
    Daily_Unlocks: int = Field(..., ge=0)
    Study_Hours: float = Field(..., ge=0, le=24)
    Physical_Activity_Hours: float = Field(..., ge=0, le=24)
    Sleep_Hours_Per_Night: float = Field(..., ge=0, le=24)

    Stress_Level: Literal['Medium', 'Low', 'Very High', 'High']
@app.get('/')   
def greed():
    return{"welcome kp"}

top_country=['Other','India','USA','Canada','Australia','UK','Germany','Mexico','Turkey','France']

@app.get('/predict')
def predict(data: studentdata):
    country_group = data.Country if data.Country in top_country else "Other"
    input_row =pd.DataFrame([{
        'Age':data.Age,
        'Gender':data.Gender,
        'Country':data.Country,
        'Academic_Level':data.Academic_Level,
        'Most_Used_Platform':data.Most_Used_Platform,
        'Purpose_Of_Use':data.Purpose_Of_Use,
        'Avg_Daily_Usage_Hours':data.Avg_Daily_Usage_Hours,
        'Daily_Unlocks':data.Daily_Unlocks,
        'Study_Hours':data.Study_Hours,
        'Physical_Activity_Hours':data.Physical_Activity_Hours,
        'Sleep_Hours_Per_Night':data.Sleep_Hours_Per_Night,
        'Stress_Level':data.Stress_Level,
        'group_country':country_group,
    }])

    prediction = model.predict(input_row)[0]

