# Status Report

# Input for date
dates = input("Please enter date range: ")

# Input for tickets created
valid_input = False
while not valid_input:
    tickets_created = input("Number of tickets created: ")
    try:
        tickets_created = int(tickets_created)
        valid_input = True
    except:
        print("Invalid input. Please enter a number.")

# Input for tickets solved
valid_input = False
while not valid_input:
    tickets_solved = input("Number of tickets solved: ")
    try:
        tickets_solved = int(tickets_solved)
        valid_input = True
    except:
        print("Invalid input. Please enter a number.")

# Input for CSAT
valid_input = False
while not valid_input:
    csat_score = input("CSAT Score (enter N/A for no survey responses): ")
    if csat_score == "N/A" or csat_score == "n/a":
        print("N/A (no survey responses)")
        valid_input = True
    else:
        try:
            csat_score = float(csat_score)
            valid_input = True
        except:
            print("Invalid input. Please enter a number.")

# Capsule Review
# Input for submissions
valid_input = False
while not valid_input:
    capsule_submissions = input("Number of capsules submitted: ")
    try:
        capsule_submissions = int(capsule_submissions)
        valid_input = True
    except:
        print("Invalid input. Please enter a number.")

# Input for in review
valid_input = False
while not valid_input:
    capsules_in_review = input("Number of capsules in review: ")
    try:
        capsules_in_review = int(capsules_in_review)
        valid_input = True
    except:
        print("Invalid input. Please enter a number.")

# Input for approved
valid_input = False
while not valid_input:
    capsules_approved = input("Number of capsules approved: ")
    try:
        capsules_approved = int(capsules_approved)
        valid_input = True
    except:
        print("Invalid input. Please enter a number.")

# Input for rejected
valid_input = False
while not valid_input:
    capsules_rejected = input("Number of capsules rejected: ")
    try:
        capsules_rejected = int(capsules_rejected)
        valid_input = True
    except:
        print("Invalid input. Please enter a number.")

# Highlights
# Input for list
highlights = input("Please enter highlights for this week separated by a semicolon: ")
highlights_to_list = highlights.split("; ")
highlights_to_list.append("Provided Auth0 access to various internal devs")

# Generate all output at once
print("\nStatus Report for", dates, "\n")
print("Tickets Created:", tickets_created)
print("Tickets Solved:", tickets_solved)
print("CSAT Score:", csat_score, "%\n")
print("Capsule Review Summary")
print("Capsule Submissions:", capsule_submissions)
print("Capsules in Review:", capsules_in_review)
print("Capsules Approved:", capsules_approved)
print("Capsules Rejected:", capsules_rejected, "\n")
print('Highlights', *highlights_to_list, sep='\n')