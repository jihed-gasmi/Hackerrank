if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    lst=student_marks[query_name]
    marks="{:.2f}".format(sum(lst)/len(lst))
    print(marks)
