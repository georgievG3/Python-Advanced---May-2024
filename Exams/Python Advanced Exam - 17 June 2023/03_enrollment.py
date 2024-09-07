def gather_credits(needed_credits, *args):
    total_credits = 0
    enrolled_courses = []

    for course_name, course_credits in args:
        if total_credits >= needed_credits:
            break

        if course_name in enrolled_courses:
            continue

        enrolled_courses.append(course_name)
        total_credits += int(course_credits)

    sorted_courses = sorted(enrolled_courses)
    result = []

    if total_credits >= needed_credits:
        result.append(f"Enrollment finished! Maximum credits: {total_credits}.\n")
        result.append(f"Courses: {', '.join(c for c in sorted_courses)}")

    else:
        result.append(f"You need to enroll in more courses! You have to gather {needed_credits - total_credits} credits more.")

    return ''.join(result)

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))