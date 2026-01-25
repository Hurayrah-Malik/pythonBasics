def main() -> None:
    # get number of students
    num_students = get_inputs()

    # get a list of scores
    scores_list = get_scores(num_students)

    # clean up list of scores
    scores_list = verify_scores(scores_list, num_students)

    print_scores(scores_list)


# ask for number of students
def get_inputs() -> int:
    num_students = int(input("Total number of students: "))
    return num_students


# ask for scores
def get_scores(num_students: int) -> list[int]:
    scores_int = []
    scores_input = input("Enter " + str(num_students) + " score(s): ")

    # turn into list of strings
    scores_string = scores_input.split()

    # turn all them into ints
    for score in scores_string:
        scores_int.append(int(score))

    return scores_int


# if scores is less than students, ask for more. if its more, then shorten it
def verify_scores(scores_list: list, num_students: int) -> list[int]:
    # if items in list is less than num_students, then ask again
    while len(scores_list) < num_students:
        scores_list = get_scores(num_students)
    # in case more scores than students, slice the list
    scores_list = scores_list[0:num_students]

    return scores_list


# print the scores one at a time
def print_scores(scores_list: list) -> None:
    counter = 1
    best_score = max(scores_list)
    for score in scores_list:
        grade = calculate_grade(best_score, score)
        print(f"Student {counter} score is {score} and grade is {grade}")

        counter += 1


# given the highest grade in class, calculate score
def calculate_grade(best: int, score: int) -> str:
    if score >= best - 10:
        return "A"
    elif score >= best - 20:
        return "B"
    elif score >= best - 30:
        return "C"
    elif score >= best - 40:
        return "D"
    else:
        return "F"


# get best score from list
# def best_score(scores: list) -> int:


if __name__ == "__main__":
    main()
