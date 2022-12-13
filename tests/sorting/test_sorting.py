from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "title": "Front-End",
            "min_salary": "1000",
            "max_salary": "4000",
            "date_posted": "20-08-11",
        },
        {
            "title": "Back-End",
            "min_salary": "1500",
            "max_salary": "4700",
            "date_posted": "20-09-11",
        },
        {
            "title": "Full-Stack",
            "min_salary": "1800",
            "max_salary": "4800",
            "date_posted": "20-10-11",
        },
        {
            "title": "Quality-Assurance",
            "min_salary": "1900",
            "max_salary": "5000",
            "date_posted": "20-11-11",
        },
    ]

    sort_by(jobs, "min_salary")
    assert jobs == [
        {
            "title": "Front-End",
            "min_salary": "1000",
            "max_salary": "4000",
            "date_posted": "20-08-11",
        },
        {
            "title": "Back-End",
            "min_salary": "1500",
            "max_salary": "4700",
            "date_posted": "20-09-11",
        },
        {
            "title": "Full-Stack",
            "min_salary": "1800",
            "max_salary": "4800",
            "date_posted": "20-10-11",
        },
        {
            "title": "Quality-Assurance",
            "min_salary": "1900",
            "max_salary": "5000",
            "date_posted": "20-11-11",
        },
    ]

    sort_by(jobs, "max_salary")
    assert jobs == [
        {
            "title": "Quality-Assurance",
            "min_salary": "1900",
            "max_salary": "5000",
            "date_posted": "20-11-11",
        },
        {
            "title": "Full-Stack",
            "min_salary": "1800",
            "max_salary": "4800",
            "date_posted": "20-10-11",
        },
        {
            "title": "Back-End",
            "min_salary": "1500",
            "max_salary": "4700",
            "date_posted": "20-09-11",
        },
        {
            "title": "Front-End",
            "min_salary": "1000",
            "max_salary": "4000",
            "date_posted": "20-08-11",
        },
    ]

    sort_by(jobs, "date_posted")
    assert jobs == [
        {
            "title": "Quality-Assurance",
            "min_salary": "1900",
            "max_salary": "5000",
            "date_posted": "20-11-11",
        },
        {
            "title": "Full-Stack",
            "min_salary": "1800",
            "max_salary": "4800",
            "date_posted": "20-10-11",
        },
        {
            "title": "Back-End",
            "min_salary": "1500",
            "max_salary": "4700",
            "date_posted": "20-09-11",
        },
        {
            "title": "Front-End",
            "min_salary": "1000",
            "max_salary": "4000",
            "date_posted": "20-08-11",
        },
    ]
