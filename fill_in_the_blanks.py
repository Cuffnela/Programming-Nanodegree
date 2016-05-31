# fill in the blanks quiz
difficulty = ['easy', 'medium', 'hard']
levels = [('A parabola is the graph of a _____1_____ equation, meaning an '
            'equation of degree 2. A parabola has a _____2_____ if the '
            'leading coeffiecient is positive and a _____3_____ if the '
            'leading coefficient is negative. This point is called the '
            '_____4_____ of the parabola.'),
            ('Exponential and logarithmic functions are _____1_____ functions. '
            'On a graph the inverse is a _____2_____ across the line y=x. '
            'The domain of an exponetial function is the _____3_____ of the '
            'relative logarithmic function. Exponetial functions and logarithmic'
            ' functions both have a _____4_____. '),
            ('The three most common trigonometric functions are sine, cosine and '
            '_____1_____. Each trig function also has a corresponding reciprocal'
            ' trig function. The reciprocal of sine is _____2_____. The reciprocal'
            ' of cosine is _____3_____. And the reciprocal of tangent is _____4_____.'
            ' Each can be represented by a _____5_____ of the lengths of the '
            'sides of a right triangle.')]
levels_ans = [['quadratic','minimum','maximum','vertex'],
            ['inverse','reflection', 'range', 'base'],
            ['tangent', 'cosecant','secant','cotangent','ratio']]

# Determines if the current word is a blank to be filled. Returns true is word
# is blank. Returns False is word is not a blank.
def is_blank(word):
    if word.find('_____') != -1:
        return True
    return False

# Sets the level based on user_input. If user_input invalid prompts user to
# enter difficulty again. Runs until correct input is given. Returns number of
# choosen level. Easy =0, Medium=1, Hard =2.
def choose_level(user_input):
    while user_input not in difficulty:
        user_input = raw_input('Your input was invalid. Check your spelling and'
                               'select either easy, medium or hard. \n')
    current_level = difficulty.index(user_input)
    print '\n Welcome to '+ user_input +' mode.'
    return current_level

# Prints out the question for the level
def print_question(level):
    print '\n'+' '.join(level)

# Determines if the user's answer was correct for the given blank.
# If incorrect prompts user to try again. Runs until the correct answer is entered.
# Returns True if user is correct.
def is_correct(user_input, blank_num, answer):
    while user_input != answer[blank_num-1]:
        print "Incorrect. Try again!\n"
        user_input = raw_input('What should go in blank '+str(blank_num)+'?\n')
    if user_input == answer[blank_num-1]:
        print 'Correct!\n'
    return True

# Moves user through the test as blanks are answered correctly. Fill blanks when
# user is correct.
def test(level, answer):
    index = 0
    blank_num = 1
    for word in level:
        if is_blank(word):
            print_question(level)
            user_input = raw_input('\nWhat should go in blank '+str(blank_num)+'?\n')
            if is_correct(user_input, blank_num, answer):
                level[index] = answer[blank_num-1]
                blank_num += 1
        index += 1

# Runs the whole fill in the balk game.
def play_game():
    user_input = raw_input('Select a difficulty by typing easy, medium or hard and pressing enter.\n')
    current_level = choose_level(user_input)
    level = levels[current_level].split()
    answer = levels_ans[current_level]
    test(level,answer)

# Allows user to play again as many times as they like before exiting.
play_count = 0
if play_count ==0:
    play_game()
    play_count += 1
# If already played asks if you would like to play again.
while play_count >0:
    user_input = raw_input('Would you like to try another level? (Yes or No)')
    if user_input == 'Yes' or user_input =='yes':
        play_game()
    elif user_input == 'No' or user_input == 'no':
        print 'Thanks for participating.'
        break
    else:
        print "Invalid input. Check your spelling and try again."
