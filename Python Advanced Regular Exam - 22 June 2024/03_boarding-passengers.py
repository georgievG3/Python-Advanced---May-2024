def boarding_passengers(capacity, *args):
    groups_count = len(args)
    groups_boarded = 0
    boarding_details = {}

    for group in args:
        number_of_passengers = int(group[0])
        benefit_program = group[1]

        if number_of_passengers <= capacity:
            if benefit_program not in boarding_details:
                boarding_details[benefit_program] = 0
            boarding_details[benefit_program] += number_of_passengers
            capacity -= number_of_passengers
            groups_boarded += 1
        elif number_of_passengers > capacity:
            continue

        if capacity == 0:
            break

    result = ''
    sorted_boarding_details = sorted(boarding_details.items(), key=lambda x: (-x[1], x[0]))

    result += "Boarding details by benefit plan:\n"

    for k, v in sorted_boarding_details:
        result += f"## {k}: {v} guests\n"

    if groups_count == groups_boarded:
        result += "All passengers are successfully boarded!"

    elif capacity <= 0 and groups_count > groups_boarded:
        result += "Boarding unsuccessful. Cruise ship at full capacity."

    elif capacity > 0 and groups_count > groups_boarded:
        result += f"Partial boarding completed. Available capacity: {capacity}."

    return result

