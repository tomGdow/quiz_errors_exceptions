import random

import problems_quiz_errors as p
import functions_quiz_errors as f
# import data_quiz_errors as d

if __name__ == '__main__':
    problem_list = [
            p.problem_one,
            p.problem_two,
            p.problem_three,
            p.problem_four,
            p.problem_five, 
            p.problem_six, 
            p.problem_seven,
            p.problem_eight, 
            p.problem_nine,
            p.problem_ten,
            p.problem_eleven,
            p.problem_twelve, 
            p.problem_thirteen, 
            p.problem_fourteen,
            p.problem_fifteen, 
            p.problem_sixteen,
            p.problem_seventeen
            ]
    random_problem_list = random.sample(problem_list, k=16)
    f.display_problem(random_problem_list[0])
    i = 1
    quit = False
    while not quit and i < 16:
        choice =f.next_question(random_problem_list[i], f.continue_choice)
        i += 1
        # f.next_question(random_problem_list[i], f.continue_choice)

