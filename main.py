from typing import List

from env import Env
from linkedin.linkedin_dao import LinkedinDao
from print import Logger
from file import FileHandler
from models import Job


def get_links():
    file_handler = FileHandler(Env.get_links_path())
    return file_handler.read_lines()


def job_info_list_to_table_data(job_info_list: List[Job]) -> List[List[str]]:
    table_data = []
    for index, job_info in enumerate(job_info_list):
        row = [
            index + 1,
            job_info.company,
            job_info.title,
            job_info.seniority.value,
            job_info.link
        ]

        table_data.append(row)

    return table_data


def main():
    jobs = LinkedinDao().get_jobs_from_links(get_links())
    headers = ["id", "Empresa", "Cargo", "Senioridade", "Link"]
    rows = job_info_list_to_table_data(jobs)

    Logger.print_table(headers=headers, rows=rows)
    Logger.write_table_to_file(headers=headers, rows=rows, file=FileHandler(Env.get_result_path()))


if __name__ == '__main__':
    Env.init()
    main()
