import joblib
import pandas as pd
from typing import Literal
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

model = joblib.load("Mental_health_model.pkl")
top_country = ['Other', 'India', 'USA', 'Canada', 'Australia', 'UK', 'Germany', 'Mexico', 'Turkey', 'France']

app = FastAPI(title="Student Mental Health Predictor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StudentData(BaseModel):
    age: int = Field(..., ge=10, le=100, alias="Age")
    gender: Literal["Male", "Female"] = Field(..., alias="Gender")
    country: str = Field(..., alias="Country")
    academic_level: Literal['Undergraduate', 'Graduate', 'High School'] = Field(..., alias="Academic_Level")
    most_used_platform: Literal['Facebook', 'LinkedIn', 'Instagram', 'Snapchat', 'Twitter', 'YouTube', 'TikTok', 'LINE', 'KakaoTalk', 'VKontakte', 'WhatsApp', 'WeChat'] = Field(..., alias="Most_Used_Platform")
    purpose_of_use: Literal['Networking', 'Education', 'Entertainment', 'News'] = Field(..., alias="Purpose_Of_Use")

    avg_daily_usage_hours: float = Field(..., ge=0, le=24, alias="Avg_Daily_Usage_Hours")
    daily_unlocks: int = Field(..., ge=0, alias="Daily_Unlocks")
    study_hours: float = Field(..., ge=0, le=24, alias="Study_Hours")
    physical_activity_hours: float = Field(..., ge=0, le=24, alias="Physical_Activity_Hours")
    sleep_hours_per_night: float = Field(..., ge=0, le=24, alias="Sleep_Hours_Per_Night")

    stress_level: Literal['Medium', 'Low', 'Very High', 'High'] = Field(..., alias="Stress_Level")

    model_config = {
        "populate_by_name": True,
        "extra": "ignore"
    }

class PredictionResponse(BaseModel):
    predicted_mental_health_score: float
    predict_mental_health_score: float

# Backwards compatibility alias
PredictionResponce = PredictionResponse

@app.get('/')
def greet():
    return {"message": "Welcome to Student Mental Health Predictor API"}

@app.post('/predict', response_model=PredictionResponse)
@app.get('/predict', response_model=PredictionResponse)
def predict(data: StudentData):
    country_group = data.country if data.country in top_country else "Other"
    input_row = pd.DataFrame([{
        'Study_Hours': data.study_hours,
        'Age': data.age,
        'Avg_Daily_Usage_Hours': data.avg_daily_usage_hours,
        'Daily_Unlocks': data.daily_unlocks,
        'Physical_Activity_Hours': data.physical_activity_hours,
        'Sleep_Hours_Per_Night': data.sleep_hours_per_night,
        'Stress_Level': data.stress_level,
        'Gender': data.gender,
        'Academic_Level': data.academic_level,
        'Most_Used_Platform': data.most_used_platform,
        'Purpose_Of_Use': data.purpose_of_use,
        'group_country': country_group,
    }])

    prediction = round(float(model.predict(input_row)[0]), 2)
    return PredictionResponse(
        predicted_mental_health_score=prediction,
        predict_mental_health_score=prediction
    )

