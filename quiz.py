import random

import problems_quiz_errors as p
import functions_quiz_errors as f
# import data_quiz_errors as d

if __name__ == '__main__':
    problem_list = [
            p.problem_one,
            # p.problem_two,
            # p.problem_three,
            # p.problem_four,
            # p.problem_five, 
            # p.problem_six, 
            # p.problem_seven,
            # p.problem_eight, 
            # p.problem_nine,
            # p.problem_ten,
            # p.problem_eleven,
            # p.problem_twelve, 
            # p.problem_thirteen, 
            # p.problem_fourteen,
            # p.problem_fifteen, 
            # p.problem_sixteen,
            # p.problem_seventeen,
            # p.problem_eighteen,
            # p.problem_nineteen,
            # p.problem_twenty,
            # p.problem_twenty_one,
            # p.problem_twenty_two,
            # p.problem_twenty_three,
            # p.problem_twenty_four,
            # p.problem_twenty_five,
            # p.problem_twenty_six,
            # p.problem_twenty_seven,
            # p.problem_twenty_eight,
            # p.problem_twenty_nine,
            # p.problem_thirty,        
            # p.problem_thirty_one,        
            # p.problem_thirty_two,        
            # p.problem_thirty_three,        
            # p.problem_thirty_four,        
            # p.problem_thirty_five,        
            # p.problem_thirty_six,        
            # p.problem_thirty_seven,        
            # p.problem_thirty_eight,        
            # p.problem_thirty_nine,        
            # p.problem_forty,        
            # p.problem_forty_one,        
            # p.problem_forty_two,        
            # p.problem_forty_three,        
            # p.problem_forty_four,        
            # p.problem_forty_five,        
            # p.problem_forty_six,        
            # p.problem_forty_seven,        
            # p.problem_forty_eight,        
            # p.problem_forty_nine,        
            # p.problem_fifty,        
            # p.problem_fifty_one,        
            # p.problem_fifty_two,        
            # p.problem_fifty_three,        
            # p.problem_fifty_four,        
            # p.problem_fifty_five,        
            p.problem_fifty_six,        
            p.problem_fifty_seven,        
            ]
    random_problem_list = random.sample(problem_list, k=len(problem_list)) # k = probem_number
    question_counter = f.counter(len(problem_list))
    f.display_problem(random_problem_list[0],question_counter, len(problem_list))
    i = 1
    quit = False
    while not quit and i < len(problem_list):  # i < problem_number
        choice =f.next_question(random_problem_list[i], f.continue_choice, question_counter, len(problem_list))
        i += 1
        quit = not choice

