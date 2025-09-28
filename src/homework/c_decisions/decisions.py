def get_letter_grade(score):
    """
    Returns the letter grade for a given numeric score.
    90-100: A
    80-89:  B
    70-79:  C
    60-69:  D
    0-59:   F
    """
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return 'Invalid score'

def get_letter_grade_switch(score):
    """
    Returns the letter grade for a given numeric score using match-case.
    90-100: A
    80-89:  B
    70-79:  C
    60-69:  D
    0-59:   F
    """
    match score:
        case s if 90 <= s <= 100:
            return 'A'
        case s if 80 <= s < 90:
            return 'B'
        case s if 70 <= s < 80:
            return 'C'
        case s if 60 <= s < 70:
            return 'D'
        case s if 0 <= s < 60:
            return 'F'
        case _:
            return 'Invalid score'
   