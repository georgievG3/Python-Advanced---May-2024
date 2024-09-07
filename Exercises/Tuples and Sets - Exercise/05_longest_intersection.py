number = int(input())

longest_intersection = []

for _ in range(number):
    first_range, second_range = input().split("-")

    start1, end1 = map(int, first_range.split(","))
    start2, end2 = map(int, second_range.split(","))

    first_set = set(range(start1, end1 + 1))
    second_set = set(range(start2, end2 + 1))

    sets_intersection = first_set.intersection(second_set)

    if len(sets_intersection) > len(longest_intersection):
        longest_intersection = sets_intersection

print(f"Longest intersection is [{', '.join(str(el) for el in longest_intersection)}] with length {len(longest_intersection)}")

# number = int(input())
#
# longest_intersection = set()
# for _ in range(number):
#     first_range, second_range = input().split("-")
#
#     # Parse the first range
#     start1, end1 = map(int, first_range.split(","))
#     # Parse the second range
#     start2, end2 = map(int, second_range.split(","))
#
#     # Create sets for both ranges
#     first_set = set(range(start1, end1 + 1))
#     second_set = set(range(start2, end2 + 1))
#
#     # Calculate the intersection of both sets
#     sets_intersection = first_set.intersection(second_set)
#
#     # Update the longest intersection if necessary
#     if len(sets_intersection) > len(longest_intersection):
#         longest_intersection = sets_intersection
#
# # Print the longest intersection
# print(f"Longest intersection is [{', '.join(map(str, sorted(longest_intersection)))}] with length {len(longest_intersection)}")

