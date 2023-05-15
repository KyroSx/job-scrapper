
from lib.regexp import Regexp
from models.job import Job
from models.seniority import Seniority


class SeniorityGetter:
    @staticmethod
    def get_seniority(job: Job) -> Seniority:
        title = job.title.lower()

        if SeniorityGetter.__is_junior_pleno(title):
            return Seniority.JUNIOR_PLENO

        if SeniorityGetter.__is_junior(title):
            return Seniority.JUNIOR

        if SeniorityGetter.__is_pleno_senior(title):
            return Seniority.PLENO_SENIOR

        if SeniorityGetter.__is_pleno(title):
            return Seniority.PLENO

        if SeniorityGetter.__is_senior(title):
            return Seniority.SENIOR

        return Seniority.NA

    @staticmethod
    def __is_junior(title: str):
        return Regexp(r"jr\.?|j[uú]nior") \
            .search(title)

    @staticmethod
    def __is_junior_pleno(title: str) -> bool:
        return Regexp(r"\bj(?:r\.?|[uú]nior)/?(?:pl(?:eno)?)\b") \
            .search(title)

    @staticmethod
    def __is_pleno(title: str) -> bool:
        return Regexp(r"\bpl(?:eno)?\b|\bpl\b|\bPL\b") \
            .search(title)

    @staticmethod
    def __is_pleno_senior(title: str) -> bool:
        return Regexp(r"\b(?:pleno|pl).*\b(?:s[eê]nior|sr)\b|\b(?:senior|sr).*\b(?:pleno|pl)\b") \
            .search(title)

    @staticmethod
    def __is_senior(title: str):
        return Regexp(r'sr\.?|s[eê]ni[oô]r') \
            .search(title)
