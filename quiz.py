# import os
# import random

import problems_quiz_errors as p
import functions_quiz_errors as f

# choice = ''
if __name__ == '__main__':
    f.display_problem(p.problem_one)
    user_continue_choice= f.continue_choice()
    if user_continue_choice:
        f.display_problem(p.problem_two)
        user_continue_choice=f.continue_choice()
    if user_continue_choice:
        f.display_problem(p.problem_three)
        user_continue_choice=f.continue_choice()
    if user_continue_choice:
        f.display_problem(p.problem_four)
        user_continue_choice=f.continue_choice()
    if user_continue_choice:
        f.display_problem(p.problem_five)
