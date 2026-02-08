import spacy
from spacy.matcher import PhraseMatcher

class SkillExtractor:
    DEFAULT_SKILLS = ["python", "sql", "nlp", "machine learning", "deep learning",
        "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch",
        "docker", "git", "fastapi", "flask", "aws", "azure", "gcp", "kubernetes", "spark", "hadoop"]
    

    def __init__(self, skills=None):
        self.skills = skills if skills is not None else self.DEFAULT_SKILLS
        self.nlp = spacy.load("en_core_web_sm")
        self.matcher = PhraseMatcher(self.nlp.vocab,attr="LOWER")
        patterns=[self.nlp.make_doc(skill) for skill in self.skills]

        self.matcher.add("SKILLS", patterns)

    
    
    def extract_skills(self, text:str)->list[str]:
        doc=self.nlp(text)
        matches=self.matcher(doc)

        skills=set()
        for _, start, end in matches:
            skill=doc[start:end].text
            skills.add(skill)
        return sorted(skills)
    


