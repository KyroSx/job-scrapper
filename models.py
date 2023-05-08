from dataclasses import dataclass
from enum import Enum


@dataclass
class JobInfo:
    company: str
    title: str
    link: str
    description: str = 'N/A'

    def __str__(self):
        return (f'\nEmpresa: {self.company}'
                f'\nTitulo: {self.title}'
                f'\nLink: {self.link}')


class Seniority(Enum):
    JUNIOR = "Junior"
    JUNIOR_PLENO = "Junior/Pleno"
    PLENO = "Pleno"
    PLENO_SENIOR = "Pleno/Senior"
    SENIOR = "Senior"
    NA = "N/A"
