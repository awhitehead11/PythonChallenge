# Getting started

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Python_Module_Challenge", "Election_results.txt")

total_votes = 0

# Step 1

county_options = []
county_votes = {}

# Step 2

winning_county = ""
winning_county_votes = 0

# Step 3

with open(file_to_load) as election_data:
        reader = csv.reader(election_data)

        header = next(reader)

        for row in reader:
                total_votes = total_votes + 1

                county_name = row[1]
                # Step 4a
                if county_name not in county_options:
                    # Step 4b
                    county_options.append(county_name)
                    # Step 4c
                    county_votes[county_name] = 0
                # Step 5
                county_votes[county_name] += 1

    # Step 6
for county_name in county_votes:
        # Step 6b
    votes = county_votes.get(county_name)
        # Step 6c
    vote_percentage = float(votes) / float(total_votes) * 100

        # Step 6d
    county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")

# Step 6f
    if (votes > winning_county_votes):
        winning_county_votes = votes
        winning_county = county_name

# Step 7
winning_county_summary = (
    f"Election Results\n"
    f"-----------------------\n"
    f"Largest County Turnout: {winning_county}\n"
    f"-----------------------\n"
    f"\nCounty Votes:\n"
    f"{county_results}\n"
    f"\n----------------------\n"
    f"Winning County Votes: {winning_county_votes}")

print(winning_county_summary)

with open(file_to_save, "w") as txt_file:
    txt_file.write(winning_county_summary)
    