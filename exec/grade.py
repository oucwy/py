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
    # match score:
    #     case 90 : return 'A'
    #     case 80: return 'B'
    #     case 70: return 'C'
    #     case 60: return 'D'
    #     case _: return 'F'

def giveScore():
    score = int(input('Enter your score: '))
    print(f'Your grade is {match_case_grade(score)}')
    print(f'Your grade is {check_grade(score)}')

def main():
    # score = int(input('Enter your score: '))
    # r = {
    #     90 <= score <= 100: 'A',
    #     80 <= score < 90: 'B',
    #     70 <= score < 80: 'C',
    #     60 <= score < 70: 'D',
    #     0 <= score < 60: 'F'
    # }[True]

    # print(f'Your grade is {r}')
    # loop to get scores
    while True:
        try:
            giveScore()
        except ValueError:
            print('Please enter a valid score.')
            continue
        else:
            break

if __name__ == '__main__':
    main()
