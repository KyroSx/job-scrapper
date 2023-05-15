from typing import List

from lib.cache import CacheHandler
from lib.json_hash import JsonHash
from linkedin.linkedin_scrapper import LinkedinScrapper
from models.job import Job


class LinkedinDao:
    def __init__(self):
        self.cache = CacheHandler()

    def get_jobs_from_links(self, links: List[str]) -> List[Job]:
        jobs = []

        for link in links:
            job = self.get_job_from_link(link)
            jobs.append(job)

        return jobs

    def get_job_from_link(self, link: str) -> Job:
        job = self.cache.get(link)

        if job:
            return JsonHash.decode(job)

        job = self._fetch_job_info(link)
        self.cache.set(key=link,
                       value=JsonHash.encode(job))

        return job

    def _fetch_job_info(self, link: str) -> Job:
        return LinkedinScrapper(link)\
            .get_job_info()
