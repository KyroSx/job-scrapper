from typing import List
from print import Logger
from file import FileHandler
from scrapper import Scrapper
from models import JobInfo


def get_job_info_from_list(links):
    jobs = []
    for link in links:
        scrapper = Scrapper(link)
        jobs.append(scrapper.get_job_info())

    return jobs


def get_links():
    file_handler = FileHandler('links')
    return file_handler.read_lines()


def job_info_list_to_table_data(job_info_list: List[JobInfo]) -> List[List[str]]:
    table_data = []
    for job_info in job_info_list:
        row = [job_info.company, job_info.job_title, job_info.link]
        table_data.append(row)
    return table_data


def main():
    jobs = get_job_info_from_list(get_links())

    Logger.print_table(headers=["Empresa", "Cargo", "Link"],
                       rows=job_info_list_to_table_data(jobs))


if __name__ == '__main__':
    main()
