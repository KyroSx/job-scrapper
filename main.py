from env import Env
from job_logger import JobLogger
from linkedin.linkedin_dao import LinkedinDao
from file import FileHandler


class Main:
    def start(self):
        jobs = LinkedinDao().get_jobs_from_links(self._get_links())

        JobLogger().log_jobs(jobs)

    def _get_links(self):
        file_handler = FileHandler(Env.get_links_path())
        return file_handler.read_lines()


if __name__ == '__main__':
    Main().start()
