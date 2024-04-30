
# The following code is trying to use a dictionary to map score ranges to grades. 
# Get the grades for the corresponding scores.
# If the score is not in the dictionary, the function should return 'F'.

# markwy, 2024.4.22
# if elif else, match case and dictionary mapping to get grades from scores
# A better approach would be to use if-elif-else statements, like this:
def check_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# This code is trying to use a dictionary to map score ranges to grades, and then immediately access the value associated with the key True. However, this approach is not recommended for a couple of reasons:
# Readability: This code is not very intuitive. Someone reading this code might not immediately understand what it's doing, which makes it harder to maintain.
# Efficiency: This code evaluates all the conditions and creates a new dictionary every time the function is called, which is not very efficient.
# Error-prone: If none of the conditions are True, trying to access the key True will raise a KeyError.
# 不够直观，不够高效，需要算出所有的条件
def match_grade(score):
    return {
        90 <= score <= 100: 'A',
        80 <= score < 90: 'B',
        70 <= score < 80: 'C',
        60 <= score < 70: 'D',
        0 <= score < 60: 'F'
    }[True]

# .get(score // 10 * 10, 'F'): This uses the get() method of the dictionary 
# to look up the grade for the rounded-down score. 
# If the score is not in the dictionary (i.e., it's less than 60), it returns 'F' as a default value.
def match_case_grade(score):
    if score < 0 or score > 100:
        return 'Invalid score'
    return {
        100: 'A+',
        90: 'A',
        80: 'B',
        70: 'C',
        60: 'D'
     }.get(score // 10 * 10, 'F')

    # match 只能匹配特定值，不能匹配范围
    # match score:
    #     case 90 : return 'A'
    #     case 80: return 'B'
    #     case 70: return 'C'
    #     case 60: return 'D'
    #     case _: return 'F'

def giveScore():
    score = int(input('Enter your score: '))
    # print(f'Your grade is {match_case_grade(score)}')
    print(f'Your grade is {check_grade(score)}')

def main():
    while True:
        try:
            giveScore()
            if input('input exit, quit, or no to quit, or press enter to continue: ') in ['exit', 'quit', 'no']:
                print('Program exit normally.')
                break
        except ValueError:
            print('Please enter a valid score.')
            continue
        else:
            # print('in else clause...')
            continue


#
# what means if __name__ == '__main__':?
# When the Python interpreter reads a source file, it executes all of the code found in it.
# Before executing the code, it will define a few special variables. For example, if the Python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__". If this file is being imported from another module, __name__ will be set to the module's name.
# In the case of your script, let's assume that it's saved as script.py. When you run your script as python script.py, the __name__ variable will be __main__, so the block that checks if __name__ == '__main__': will be executed. If you import your script from another module, the block will not be executed.
# This allows you to have a way to execute code in your script when you want to run it as a program and not have that code execute when you just want to import your script as a module in another program.
#
# 当程序独立运行时，__name__的值为'__main__'，当程序被导入时，__name__的值为模块名。
if __name__ == '__main__':
    # print(__name__)
    main()
