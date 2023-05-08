from models import JobInfo, Seniority
from regexp import Regexp


class SeniorityGetter:
    @staticmethod
    def get_seniority(job: JobInfo) -> Seniority:
        if SeniorityGetter.__is_junior(job):
            return Seniority.JUNIOR

        if SeniorityGetter.__is_pleno(job):
            return Seniority.PLENO

        if SeniorityGetter.__is_senior(job):
            return Seniority.SENIOR

        return Seniority.NA

    @staticmethod
    def __is_junior(job: JobInfo):
        return Regexp(r"jr\.?|j[uú]nior") \
            .search(job.job_title.lower())

    @staticmethod
    def __is_pleno(job: JobInfo):
        return Regexp(r"\bpl(?:eno)?\b|\bpl\b|\bPL\b") \
            .search(job.job_title.lower())

    @staticmethod
    def __is_senior(job: JobInfo):
        return Regexp(r'sr\.?|s[eê]ni[oô]r') \
            .search(job.job_title.lower())