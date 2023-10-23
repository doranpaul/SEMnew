# Define the threshold values as global constants
LECTURE_THRESHOLD = 16 
LAB_THRESHOLD = 11
SUPPORT_THRESHOLD = 22
CANVAS_THRESHOLD = 27

def suggest_improvement_plan(lecture, lab, support, canvas):
    suggestions = []

    if lecture <= LECTURE_THRESHOLD:
        suggestions.append("Attend more lecture sessions to improve your overall attendance. You don't want to risk failing!")
    if lecture > LECTURE_THRESHOLD:
        suggestions.append("Great job, keep up the good work in your lectures!")

    if lab <= LAB_THRESHOLD:
        suggestions.append("Increase your participation in lab sessions to boost your attendance. You don't want to risk failing!")
    if lab > LAB_THRESHOLD:
        suggestions.append("Great job, keep up the good work in your lab work!")

    if support <= SUPPORT_THRESHOLD:
        suggestions.append("Make sure to attend more support sessions for better engagement. You don't want to risk failing!")
    if support > SUPPORT_THRESHOLD:
        suggestions.append("Great job, keep attending your support sessions!")

    if canvas <= CANVAS_THRESHOLD:
        suggestions.append("Spend more time on Canvas activities to meet the required attendance. You don't want to risk failing!")
    if canvas > CANVAS_THRESHOLD:
        suggestions.append("Great job, keep up to date with your canvas engagement!")
        
    return suggestions
