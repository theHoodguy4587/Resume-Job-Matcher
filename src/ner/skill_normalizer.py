class SkillNormalizer:
    """ Normalizes skill names to a standard format.
    Example:
        'python3' -> 'python'
        'ml' -> 'machine learning'
        'sklearn' -> 'scikit-learn'
        """

    NORMALIZATION_MAP = {
        "python3": "python",
        "py": "python",
        "ml": "machine learning",
        "deep learning": "deep learning",
        "sklearn": "scikit-learn",
        "pytorch": "pytorch",
        "tensorflow": "tensorflow",
        "fastapi": "fastapi",
        "flask": "flask",
        "aws": "aws",
        "docker": "docker",
        "git": "git",
        "numpy": "numpy",
        "pandas": "pandas",
        "nlp": "nlp"
    }
    def __init__(self):
        self.map=self.NORMALIZATION_MAP

    def normalize(self,skills:list[str])->list[str]:
        normalized_skills=set()
        for skill in skills:
            normalized_skill=self.map.get(skill.lower(), skill.lower())
            normalized_skills.add(normalized_skill)
        return sorted(normalized_skills)
    
## quick test

if __name__=="__main__":
    skills=["Python3", "ML", "sklearn", "pytorch","Docker", "Git", "NLP"]   
    normalizer=SkillNormalizer()
    normalized_skills=normalizer.normalize(skills)
    print("Original Skills:", skills)
    print("Normalized Skills:", normalized_skills)