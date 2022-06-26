# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote




# Import the datetime class from the datetime module.
# #####import datetime
# Use the now() attribute on the datetime class to get the present time.
# #####now = datetime.datetime.now()
# Print the present time.
# #####print("The time right now is ", now)

# You can alias a module like below
# import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# Print the present time.
# print("The time right now is ", now)

# import csv
# print(dir(csv))

# The general format for opening a file is, file_variable = open(filename, mode).

# declare file path
# file_to_load_up = 'election_results.csv'

# open file with declared variable
# election_data = open(file_to_load_up, 'r')

# Closing a file disconnects the program from the file. 
# It's important that you close the file after you read a file and write data to a file.

# When you read data from a file and it is not closed at the end of the operation, you can lose some of the data. 
# When you write data to a file, the data is not stored in the file at first. 
# It is written to a "buffer" in the computer memory and may be overwritten later if the file is not closed. 
# Once you close the file, the data is stored in the file.

# Close the file.
# election_data.close()


# Open the election results and read the file
# with open(file_to_load_up) as election_data:

#      To do: perform analysis.
#      print(election_data)

# Close the file. Again
# election_data.close()

# import os.path

# print(dir(os.path))

# import modules
# import csv
# import os
# Assign a variable for the file to load and the path.
# file_to_load = os.path.join("election_results.csv")
# Open the election results and read the file.
# with open(file_to_load) as election_data:

#     Print the file object.
#     print(election_data)

# election_data.close()

# Create a filename variable to a direct or indirect path to the file.

# file_to_save = os.path.join("election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.

# print(open(file_to_save, "w"))


# ## one way to open and write to a file.  notice variable to grab, variable to open in w formate and then a function to write with string filled out)

# Create a filename variable to a direct or indirect path to the file.

#         file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.

#         outfile = open(file_to_save, "w")

# Write some data to the file.

#         outfile.write("Hello World")

# Close the file
#       outfile.close()

# simpler "cleaner way to do the same thing"

# Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     Write some data to the file.
#     txt_file.write("Counties in the Election\n------------------\nArapahoe\nDenver\nJefferson")

# Add our dependencies.
# Add our dependencies.

import csv
import os


# Assign a variable to load a file from a path.

file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.

file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

#Declare Candidate Options
candidate_options = []

#declare dictionary for Printing
candidate_votes = {}

# Winning Candidate and Winning Count Tracker

winning_candidate = ""

winning_count = 0

winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

        file_reader = csv.reader(election_data)

# Read and print the header row.
        headers = next(file_reader)


        for row in file_reader:

                total_votes += 1

        # Print the candidate name from each row

                candidate_name = row[2]

# If the candidate does not match any existing candidate...

                if candidate_name not in candidate_options:
        
        #append candidate name
                        # Add the candidate name to the candidate list.
                        candidate_options.append(candidate_name)
                        # Begin tracking that candidate's vote count.
                        candidate_votes[candidate_name] = 0
                # Add a vote to that candidate's count
                candidate_votes[candidate_name] += 1
        
        with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
                election_results = (
                        f"\nElection Results\n"
                        f"-------------------------\n"
                        f"Total Votes: {total_votes:,}\n"
                        f"-------------------------\n")
                print(election_results, end="")
                # Save the final vote count to the text file.
                txt_file.write(election_results)

                # 1. Iterate through the candidate list.
                for candidate_name in candidate_votes:

                        # 2. Retrieve vote count of a candidate.

                        votes = candidate_votes[candidate_name]

                        # 3. Calculate the percentage of votes.

                        vote_percentage = round(float(votes) / float(total_votes) * 100,1)
                        
                        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

                        print(candidate_results)

                        txt_file.write(candidate_results)

                        if (votes > winning_count) and (vote_percentage > winning_percentage):
                        # If true then set winning_count = votes and winning_percent =
                        # vote_percentage.
                                winning_count = votes
                                winning_percentage = vote_percentage
                        # And, set the winning_candidate equal to the candidate's name.
                                winning_candidate = candidate_name

                        # Print the winning candidate's results to the terminal.
                winning_candidate_summary = (
                        f"-------------------------\n"
                        f"Winner: {winning_candidate}\n"
                        f"Winning Vote Count: {winning_count:,}\n"
                        f"Winning Percentage: {winning_percentage:.1f}%\n"
                        f"-------------------------\n")

                print(winning_candidate_summary)
                
                txt_file.write(winning_candidate_summary)