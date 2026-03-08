from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI(title="Student Placement Prediction API")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "placement_pipeline.pkl")

model = joblib.load(MODEL_PATH)

class StudentInput(BaseModel):
    branch: int
    college_tier: int
    cgpa: float
    backlogs: int
    coding_skills: float
    dsa_score: float
    aptitude_score: float
    communication_skills: float
    ml_knowledge: float
    system_design: float
    internships: int
    projects_count: int
    certifications: int
    hackathons: int
    open_source_contributions: int
    extracurriculars: int


@app.get("/")
def home():
    return {"message": "Student Placement Prediction API is running 🚀"}


@app.post("/predict")
def predict(data: StudentInput):

    features = np.array([[
        data.branch,
        data.college_tier,
        data.cgpa,
        data.backlogs,
        data.coding_skills,
        data.dsa_score,
        data.aptitude_score,
        data.communication_skills,
        data.ml_knowledge,
        data.system_design,
        data.internships,
        data.projects_count,
        data.certifications,
        data.hackathons,
        data.open_source_contributions,
        data.extracurriculars
    ]])

    prediction = model.predict(features)

    result = "Placed" if prediction[0] == 1 else "Not Placed"

    return {
        "prediction": int(prediction[0]),
        "result": result
    }