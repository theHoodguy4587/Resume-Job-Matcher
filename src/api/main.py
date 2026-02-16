from fastapi import FastAPI,UploadFile,File
from pathlib import Path
import shutil
import uuid

from src.pipeline.pipeline import pipeline

app=FastAPI(title="Resume-Job Matcher API", version="1.0")

pipeline_obj=pipeline()

TMP_DIR=Path("tmp_uploads")
TMP_DIR.mkdir(exist_ok=True)

@app.post("/match")
async def match_resume_job(resume:UploadFile=File(...), job_desc:UploadFile=File(...)):

    resume_path=TMP_DIR / f"{uuid.uuid4()}_{resume.filename}"
    job_desc_path=TMP_DIR / f"{uuid.uuid4()}_{job_desc.filename}"

    with resume_path.open("wb") as f:
        shutil.copyfileobj(resume.file, f)
    
    with job_desc_path.open("wb") as f:
        shutil.copyfileobj(job_desc.file, f)

    result=pipeline_obj.run(resume_path, job_desc_path)

    resume_path.unlink(missing_ok=True)
    job_desc_path.unlink(missing_ok=True)

    return result