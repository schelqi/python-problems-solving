# Challenge from Hackerrank
# https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=false

#Read from input
line1 = input().split()
number_of_students = int(line1[0])
number_of_subjects = int(line1[1])
all_scores = list()
for i in range(number_of_subjects):
    line = input().split()
    scores = list(map(float, line ))
    all_scores.append(scores)

scores_per_student = zip(*all_scores)
out_format = '{avg:.1f}'

for scores in scores_per_student:
    avg_score  = sum(scores)/ number_of_subjects
    print(out_format.format(avg = avg_score))

