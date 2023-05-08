import unittest

from models import JobInfo, Seniority
from seniority.seniority_getter import SeniorityGetter


class SeniorityGetterTestCase(unittest.TestCase):
    def sut(self, job: JobInfo):
        return SeniorityGetter.get_seniority(job)

    def make_job(self, title: str, description: str = None) -> JobInfo:
        return JobInfo(company='Google',
                       job_title=title,
                       job_description=description,
                       link='http://google.com')

    def test_junior(self):
        jobs = [
            self.make_job(title='Desenvolvedor Junior'),
            self.make_job(title='Desenvolvedor júnior em react'),
            self.make_job(title='progamador junior'),
            self.make_job(title='Pessoa Desenvolvedora Front End Junior'),
            self.make_job(title='Pessoa Desenvolvedora Front-end Júnior (React)'),
            self.make_job(title='Desenvolvedor de Software Jr - Home Office'),
        ]

        for job in jobs:
            self.assertEqual(self.sut(job), Seniority.JUNIOR)

    def test_pleno(self):
        jobs = [
            self.make_job(title='Desenvolvedor React Pleno'),
            self.make_job(title='[Micro] Pessoa Desenvolvedora Front End React-Native | Pleno'),
            self.make_job(title='Front End Developer PL'),
            self.make_job(title='Pessoa Desenvolvedora Front-end React Pleno'),
        ]

        for job in jobs:
            self.assertEqual(self.sut(job), Seniority.PLENO)

    def test_senior(self):
        jobs = [
            self.make_job(title="Desenvolvedor Front End Sr.",
                          description="Modelo Hibrido - 2x por semana no escritório - Possibilidade de ser Home "
                                      "Office"),
            self.make_job(title="PESSOA DESENVOLVEDORA FRONT-END SENIOR"),
            self.make_job(title="[Interaction Plataform] Pessoa Desenvolvedora Front End React (Web)| Sênior")
        ]

        for job in jobs:
            self.assertEqual(self.sut(job), Seniority.SENIOR)


if __name__ == '__main__':
    unittest.main()