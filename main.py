# main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from ner.skill_extractor import load_nlp_model, extract_skills
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
nlp = load_nlp_model()

class ResumeRequest(BaseModel):
    text: str


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/resume-extractor")
async def resume_extractor(data: ResumeRequest):
    skills = extract_skills(data.text, nlp)
    return { "skills": skills }
