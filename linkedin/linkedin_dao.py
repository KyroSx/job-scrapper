from typing import List

from models import JobInfo
from scrapper import Scrapper


class LinkedinDao:
    @staticmethod
    def get_jobs_from_links(links: List[str]) -> List[JobInfo]:
        jobs = []
        for link in links:
            scrapper = Scrapper(link)
            jobs.append(scrapper.get_job_info())

        return jobs
