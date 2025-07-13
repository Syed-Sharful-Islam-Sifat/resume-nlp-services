# ner/skill_extractor.py
import spacy
from spacy.pipeline import EntityRuler
import json
import os

def load_nlp_model():
    nlp = spacy.load("en_core_web_sm")
    ruler = nlp.add_pipe("entity_ruler", before="ner")
    

    # Load custom skill patterns
    patterns_path = os.path.join(os.path.dirname(__file__), "../skills.json")
    with open(patterns_path, "r") as f:
        patterns = json.load(f)

    ruler.add_patterns(patterns)

    return nlp

def extract_skills(text, nlp):
    doc = nlp(text)
    skills = list(set([ent.text.lower() for ent in doc.ents if ent.label_ == "SKILL"]))
    return skills
