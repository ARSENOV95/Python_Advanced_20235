def gather_credits(needed_credits :int,*args):
    enrollment_pts = 0
    enrolled = []

    result = ''

    for course,credits in args:
        if needed_credits <= 0:
            break

        if course not in enrolled:
            enrolled.append(course)
            needed_credits -= credits
            enrollment_pts += credits

        if needed_credits <= 0:
            break

    if needed_credits > 0:
        result += f"You need to enroll in more courses! You have to gather {needed_credits} credits more."

    else:
        result += f"Enrollment finished! Maximum credits: {enrollment_pts}.\n"
        enrolled = sorted(enrolled)
        result += f"Courses: {', '.join(enrolled)}"

    return result

#print(gather_credits(80,("Basics", 27),))

#print(gather_credits(80, ("Advanced", 30), ("Basics", 27), ("Fundamentals", 27),)) 

#print(gather_credits(60, ("Basics", 27), ("Fundamentals", 27), ("Advanced", 30), ("Web", 30))) 