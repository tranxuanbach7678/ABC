def assign_ranks(n, stu_name, stu_score):
    # Create a list of tuples (name, score)
    students = []
    for i in range(n):
        students.append((stu_name[i], stu_score[i]))

    # Manual ranking logic
    ranks = [0] * n  # Initialize ranks list

    for i in range(n):
        rank = 1  # Start with rank 1 for the current student
        for j in range(n):
            # Compare scores to determine rank
            if students[i][1] < students[j][1]:
                rank += 1
        ranks[stu_name.index(students[i][0])] = rank  # Assign rank to the correct position

    return ranks

if __name__ == '__main__':
    n = int(input().strip())
    stu_name = input().rstrip().split()
    stu_score = list(map(int, input().rstrip().split()))

    ranks = assign_ranks(n, stu_name, stu_score)
    print(" ".join(map(str, ranks)))