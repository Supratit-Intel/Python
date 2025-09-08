def activity_selection(intervals):
    intervals = sorted(intervals, key=lambda x: x[1])
    res = [intervals[0]]
    last_end = intervals[0][1]
    for s,e in intervals[1:]:
        if s >= last_end:
            res.append((s,e))
            last_end = e
    return res

if __name__ == '__main__':
    intervals = [(1,2),(3,4),(0,6),(5,7),(8,9)]
    print(activity_selection(intervals))