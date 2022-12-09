from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs_list = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for job in jobs_list:
        assert 'title' in job
        assert 'salary' in job
        assert 'type' in job
