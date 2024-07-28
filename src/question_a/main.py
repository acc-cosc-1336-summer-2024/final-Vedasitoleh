#add import

import question_a

user_input = 'Y'

while user_input != 'quit':
    user_input = input("Enter 'quit' to exit program: \n")
    question_a.display_multiplication_table(question_a.create_multiplication_table(1))
    
    

