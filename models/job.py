from dataclasses import dataclass

from models.seniority import Seniority


@dataclass
class Job:
    company: str
    title: str
    link: str
    description: str = 'N/A'
    seniority: Seniority = Seniority.NA

    def __str__(self):
        return (f'\nEmpresa: {self.company}'
                f'\nTitulo: {self.title}'
                f'\nLink: {self.link}')
