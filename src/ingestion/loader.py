from pathlib import Path
import pdfplumber

class DataLoader:
    """
    Loads raw text data from supported file formats.
    Phase 1 supports: .txt, .pdf
    """

    def load(self,file_path:str)->str:
        path=Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        if path.suffix.lower()==".txt":
            return self._load_txt(path)
        elif path.suffix.lower()==".pdf":
            return self._load_pdf(path)
        else:
            raise ValueError(f"Unsupported file format: {path.suffix}")
    def _load_txt(self,path:Path)->str:
        with path.open("r", encoding="utf-8") as f:
            return f.read()
        
    def _load_pdf(self,path:Path)->str:
        text=""
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text+=page.extract_text()
        return "\n".join(text.splitlines())

## quick test
if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parents[2]  
    data_dir = BASE_DIR / "data"

    loader = DataLoader()
    resume_text = loader.load(data_dir / "Senitha_Gunathilaka_Data_Science_Intern.pdf")

    print(resume_text[:300])