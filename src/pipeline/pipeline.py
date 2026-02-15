from pathlib import Path

from src.ingestion.loader import DataLoader
from src.preprocessing.text_cleaner import TextCleaner
from src.ner.skill_extractor import SkillExtractor
from src.ner.skill_normalizer import SkillNormalizer
from src.matching.matcher import Matcher


class pipeline:
    """
    End-To-End rule based NLP pipeline:
    Resume + Job Description ->Skill Match report
    """
    def __init__(self):
        self.loader=DataLoader()
        self.cleaner=TextCleaner()
        self.extractor=SkillExtractor()
        self.normalizer=SkillNormalizer()
        self.matcher=Matcher()
    
    def run(self,resume_path:str, job_desc_path:str)->dict:
        resume_text=self.loader.load(resume_path)
        job_desc_text=self.loader.load(job_desc_path)

        clean_resume=self.cleaner.clean(resume_text)
        clean_job_desc=self.cleaner.clean(job_desc_text)

        resume_skills=self.extractor.extract_skills(clean_resume)
        job_skills=self.extractor.extract_skills(clean_job_desc)

        norm_resume_skills=self.normalizer.normalize(resume_skills)
        norm_job_skills=self.normalizer.normalize(job_skills)

        match_result=self.matcher.match(norm_resume_skills, norm_job_skills)
        return match_result
    
## quick test

if __name__=="__main__":
    BASE_DIR = Path(__file__).resolve().parents[2]  
    data_dir = BASE_DIR / "data"

    resume_path=data_dir / "Senitha_Gunathilaka_Data_Science_Intern.pdf"
    job_desc_path=data_dir / "job_description.txt"

    pipeline_obj=pipeline()
    result=pipeline_obj.run(resume_path, job_desc_path)
    print("Final Match Result:", result)




