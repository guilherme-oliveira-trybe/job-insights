from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    return max(
        [int(job["max_salary"]) for job in data if job["max_salary"].isdigit()]
    )


def get_min_salary(path: str) -> int:
    data = read(path)
    return min(
        [int(job["min_salary"]) for job in data if job["min_salary"].isdigit()]
    )


def check_params(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError

    min_salary = str(job["min_salary"])
    max_salary = str(job["max_salary"])

    if not max_salary.isnumeric() or not min_salary.isnumeric():
        raise ValueError

    if int(min_salary) > int(max_salary):
        raise ValueError

    if not str(salary).lstrip("-").isnumeric():
        raise ValueError


# ajuda na monitoria para solução do requisito
def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        check_params(job, salary)
        return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])
    except ValueError:
        raise


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    jobs_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_list.append(job)
        except ValueError as error:
            print(error)
    return jobs_list
