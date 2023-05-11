from typing import List

from models import Job
from print import Logger
from file import FileHandler

from env import Env


class JobLogger:
    def log_jobs(self, jobs):
        headers = ["id", "Empresa", "Cargo", "Senioridade", "Link"]
        rows = self._job_info_list_to_table_data(jobs)

        Logger.print_table(headers=headers, rows=rows)
        Logger.write_table_to_file(headers=headers,
                                   rows=rows,
                                   file=FileHandler(Env.get_result_path()))

    def _job_info_list_to_table_data(self, job_info_list: List[Job]) -> List[List[str]]:
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
