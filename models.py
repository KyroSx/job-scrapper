from dataclasses import dataclass


@dataclass
class JobInfo:
    company: str
    job_title: str
    link: str

    def __str__(self):
        return (f'\nEmpresa: {self.company}'
                f'\nTitulo: {self.job_title}'
                f'\nLink: {self.link}')

