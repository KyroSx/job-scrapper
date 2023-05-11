from typing import List

from cache import CacheHandler
from json_hash import JsonHash
from linkedin.linkedin_scrapper import LinkedinScrapper
from models import JobInfo


class LinkedinDao:
    def __init__(self):
        self.cache = CacheHandler()

    def get_jobs_from_links(self, links: List[str]) -> List[JobInfo]:
        jobs = []

        for link in links:
            job = self.cache.get(link)

            if job:
                job = JsonHash.decode(job)
            else:
                job = self._fetch_job_info(link)
                self.cache.set(key=link,
                               value=JsonHash.encode(job))

            jobs.append(job)

        return jobs

    def _fetch_job_info(self, link: str) -> JobInfo:
        scrapper = LinkedinScrapper(link)
        job = scrapper.get_job_info()
        return job
