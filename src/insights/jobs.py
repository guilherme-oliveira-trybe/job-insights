from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:

    with open(path, encoding="utf-8") as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        return list(jobs_reader)


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    return set([job["job_type"] for job in data])


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job['job_type'] == job_type]
