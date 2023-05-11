import unittest
from parameterized import parameterized

from models import Job, Seniority
from seniority.seniority_getter import SeniorityGetter


class SeniorityGetterTestCase(unittest.TestCase):
    def sut(self, job: Job):
        return SeniorityGetter.get_seniority(job)

    def make_job(self, title: str, description: str = 'N/A') -> Job:
        return Job(company='Google',
                   title=title,
                   description=description,
                   link='http://google.com')

    @parameterized.expand([
        'Desenvolvedor Junior',
        'Desenvolvedor júnior em react',
        'progamador junior',
        'Pessoa Desenvolvedora Front End Junior',
        'Pessoa Desenvolvedora Front-end Júnior (React)',
        'Desenvolvedor de Software Jr - Home Office',
    ])
    def test_junior(self, title):
        job = self.make_job(title)
        self.assertEqual(self.sut(job), Seniority.JUNIOR)

    @parameterized.expand([
        'Desenvolvedor Junior/Pleno',
        'Desenvolvedor júnior/pleno em react',
        'progamador JR/PL'
    ])
    def test_junior_pleno(self, title):
        job = self.make_job(title)
        self.assertEqual(self.sut(job),
                         Seniority.JUNIOR_PLENO)

    @parameterized.expand([
        'Desenvolvedor React Pleno',
        '[Micro] Pessoa Desenvolvedora Front End React-Native | Pleno',
        'Front End Developer PL',
        'Pessoa Desenvolvedora Front-end React Pleno'
    ])
    def test_pleno(self, title):
        job = self.make_job(title)
        self.assertEqual(self.sut(job),
                         Seniority.PLENO)

    @parameterized.expand([
        'Desenvolvedor React Pleno/Senior',
        '[Micro] Pessoa Desenvolvedora Front End React-Native | PL/SR',
        'Front End Developer Pleno/Sênior'
    ])
    def test_pleno_senior(self, title):
        job = self.make_job(title)
        self.assertEqual(self.sut(job),
                         Seniority.PLENO_SENIOR)

    @parameterized.expand([
        'Desenvolvedor Front End Sr.',
        'PESSOA DESENVOLVEDORA FRONT-END SENIOR',
        'Pessoa Engenheira de Software Frontend Sênior - React'
    ])
    def test_senior(self, title):
        job = self.make_job(title)
        self.assertEqual(self.sut(job),
                         Seniority.SENIOR)


if __name__ == '__main__':
    unittest.main()
