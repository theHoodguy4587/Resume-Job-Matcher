class Matcher:
    """
    Compares resume skills with job description and returns match score and missing skills.
    """

    def __init__(self):
        pass
    def match(self, resume_skills:list[str], job_skills:list[str])->tuple[float, list[str]]:
        resume_set=set([s.lower() for s in resume_skills])
        job_set=set([s.lower() for s in job_skills])

        matched=resume_set & job_set
        missing=job_set - resume_set
        matched_score=len(matched)/len(job_set) if job_set else 0.0

        return{
            "matched_score": round(matched_score, 2),
            "matched_skills": sorted(matched),
            "missing_skills": sorted(missing),
            "resume_skills": sorted(resume_set),
            "job_skills": sorted(job_set)
        }
    
## quick test

if __name__=="__main__":
    resume_skills=["Python", "SQL", "NLP", "Machine Learning", "Docker"]
    job_skills=["Python", "SQL", "Deep Learning", "AWS","FastAPI"]

    matcher=Matcher()
    result=matcher.match(resume_skills, job_skills)
    print("Match Result:", result)