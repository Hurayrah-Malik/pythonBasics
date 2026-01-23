def main() -> None:
    print("main function is running")

    num_students = get_inputs()
    print(num_students)

    scores_list = get_scores()
    print(scores_list)

    print_scores(scores_list)


# ask for number of students
def get_inputs() -> int:
    num_students = int(input("Total number of students:"))
    return num_students


# ask for scores
def get_scores() -> list:
    scores_int = []
    scores_input = input("input all the scores")

    # turn into list of strings
    scores_string = scores_input.split()

    # turn all them into ints
    for score in scores_string:
        scores_int.append(int(score))

    return scores_int


# print the scores one at a time
def print_scores(scores_list: list) -> None:
    counter = 0
    for score in scores_list:
        print("student ", counter, " recieved an ", score)
        counter += 1


if __name__ == "__main__":
    main()
