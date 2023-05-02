import requests
from bs4 import BeautifulSoup

from models import JobInfo


class Scrapper:
    def __init__(self, url: str):
        self.url = url
        self.html = self._fetch_html()
        self.page = BeautifulSoup(self.html, 'html.parser')

    def _fetch_html(self) -> str:
        response = requests.get(self.url)
        return response.content

    def get_job_info(self) -> JobInfo:
        company = self.page.select_one('.topcard__org-name-link').text.strip()
        job_title = self.page.select_one('.topcard__title').text.strip()

        return JobInfo(company=company,
                       job_title=job_title,
                       link=self.url)

