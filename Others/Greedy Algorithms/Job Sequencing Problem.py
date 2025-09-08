def job_sequencing(jobs):
    # jobs: list of (id, deadline, profit)
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    max_deadline = max(j[1] for j in jobs)
    res = [None] * (max_deadline+1)
    total_profit = 0
    for jid, d, p in jobs:
        for slot in range(d, 0, -1):
            if res[slot] is None:
                res[slot] = jid
                total_profit += p
                break
    return res, total_profit

if __name__ == '__main__':
    jobs = [('a',2,100),('b',1,19),('c',2,27)]
    print(job_sequencing(jobs))