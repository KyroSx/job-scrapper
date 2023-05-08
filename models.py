from dataclasses import dataclass
from enum import Enum


@dataclass
class JobInfo:
    company: str
    job_title: str
    link: str
    job_description: str = 'N/A'

    def __str__(self):
        return (f'\nEmpresa: {self.company}'
                f'\nTitulo: {self.job_title}'
                f'\nLink: {self.link}')


class Seniority(Enum):
    JUNIOR = "Junior"
    JUNIOR_PLENO = "Junior/Pleno"
    PLENO = "Pleno"
    PLENO_SENIOR = "Pleno/Senior"
    SENIOR = "Senior"
    NA = "N/A"
