# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

#import os
#import csv

# Assign a variable for the file to load and the path.
#election_results = '..\Resources\election_results.csv'

# Open the election results and read the file.
# csvpath = os.path.join('election_results.csv')

# Open the election results and read the file
#file_to_load = ('election_results.csv') 
#with open(file_to_load) as election_data:

# close the file.
       # election_data.close()
        
        # To do: perform analysis.
  #      print("election_data.csv")

###SUCESSFUL
# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
#reader = csv.reader("Resources/election_results.csv")
# header = next(reader)
# for row in reader:
#       print(row)


#NOT successful
# with open(file_to_load) as election_data:
# with open(election_results.csv) as election_data:
#      # To do: perform analysis.
#      print(election_data)


#SUCCESSFUL
# import csv
# import os
# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     # Print the file object.
#      print(election_data)

#SUCCESSFUL (after creating a folder in ElectionAnalysis folder and naming it as analysis.  The text file is created there)
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")
# Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")
# Close the file
#outfile.close()


#SUCCESSFUL
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:
# Write three counties to the file.
    #  txt_file.write("Arapahoe, ")
    #  txt_file.write("Denver, ")
    #  txt_file.write("Jefferson")
# Close the file
#outfile.close()



#SUCCESSFUL
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:
# Write three counties to the file.
#     txt_file.write("Arapahoe, Denver, Jefferson")
# Close the file
#outfile.close()


#SUCCESSFUL
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:
# # Write three counties to the file.
# #write each county on a separate line
#       txt_file.write("Arapahoe\nDenver\nJefferson")
# # Close the file
# outfile.close()



# #SUCCESSFUL
# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     # Read the file object with the reader function.
#     file_reader = csv.reader(election_data)
#     # Print each row in the CSV file.
#     for row in file_reader:
#         print(row)


# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)
#     # Read and print the header row.
#     headers = next(file_reader)
#     print(headers)

# #SUCCESSFUL
# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # 1. Initialize a total vote counter.
# total_votes = 0

# # Open the election results and read the file
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)

#     # Read the header row.
#     headers = next(file_reader)

#     # Print each row in the CSV file.
#     for row in file_reader:
#         # 2. Add to the total vote count.
#         total_votes += 1

# # 3. Print the total votes.
# print(total_votes)



# #SUCCESSFUL
# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Initialize a total vote counter.
# total_votes = 0

# # Candidate Options
# candidate_options = []

# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)

#     # Read the header row.
#     headers = next(file_reader)

#     # Print each row in the CSV file.
#     for row in file_reader:
#         # Add to the total vote count.
#         total_votes += 1

#         # Print the candidate name from each row.
#         candidate_name = row[2]

#         # Add the candidate name to the candidate list.
#         candidate_options.append(candidate_name)

# # Print the candidate list.
# print(candidate_options)




# #SUCCESSFUL
# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Initialize a total vote counter.
# total_votes = 0

# # Candidate Options
# candidate_options = []

# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)

#     # Read the header row.
#     headers = next(file_reader)

# # Print each row in the CSV file.
#     for row in file_reader:
#         # Add to the total vote count.
#         total_votes += 1

#         # Print the candidate name from each row.
#         candidate_name = row[2]

#         # If the candidate does not match any existing candidate...
#         if candidate_name not in candidate_options:
#             # Add it to the list of candidates.
#             candidate_options.append(candidate_name)

# # Print the candidate list.
# print(candidate_options)



# #SUCCESSFUL
# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Initialize a total vote counter.
# total_votes = 0

# # Candidate options and candidate votes
# candidate_options = []
# # 1. Declare the empty dictionary.
# candidate_votes = {}

# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)

#     # Read the header row.
#     headers = next(file_reader)

#     # Print each row in the CSV file.
#     for row in file_reader:
#         # Add to the total vote count.
#         total_votes += 1

#         # Print the candidate name from each row.
#         candidate_name = row[2]

#         if candidate_name not in candidate_options:
#           # Add the candidate name to the candidate list.
#             candidate_options.append(candidate_name)

#            # Begin tracking that candidate's vote count.
#             candidate_votes[candidate_name] = 0

#         # Add a vote to that candidate's count
#         candidate_votes[candidate_name] += 1

# # Print the candidate vote dictionary.
# print(candidate_votes)





# #SUCCESSFUL
# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Initialize a total vote counter.
# total_votes = 0

# # Candidate options and candidate votes
# candidate_options = []
# # 1. Declare the empty dictionary.
# candidate_votes = {}

# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)

#     # Read the header row.
#     headers = next(file_reader)

#     # Print each row in the CSV file.
#     for row in file_reader:
#         # Add to the total vote count.
#         total_votes += 1

#         # Print the candidate name from each row.
#         candidate_name = row[2]

#         if candidate_name not in candidate_options:
#           # Add the candidate name to the candidate list.
#             candidate_options.append(candidate_name)

#            # Begin tracking that candidate's vote count.
#             candidate_votes[candidate_name] = 0

#         # Add a vote to that candidate's count
#         candidate_votes[candidate_name] += 1

# ####if you want to show the number of votes activate this line too)
# # Print the candidate vote dictionary. 
# #print(candidate_votes)

# # Determine the percentage of votes for each candidate by looping through the counts.
# # 1. Iterate through the candidate list.
# for candidate_name in candidate_votes:
#     # 2. Retrieve vote count of a candidate.
#     votes = candidate_votes[candidate_name]
#     # 3. Calculate the percentage of votes.
#     vote_percentage = float(votes) / float(total_votes) * 100
#     # 4. Print the candidate name and percentage of votes.
#     print(f"{candidate_name}: received {vote_percentage}% of the vote.")


# #SUCCESSFUL
# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Initialize a total vote counter.
# total_votes = 0

# # Candidate options and candidate votes
# candidate_options = []
# # 1. Declare the empty dictionary.
# candidate_votes = {}

# # Winning Candidate and Winning Count Tracker
# winning_candidate = ""
# winning_count = 0
# winning_percentage = 0

# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)

#     # Read the header row.
#     headers = next(file_reader)

#     # Print each row in the CSV file.
#     for row in file_reader:
#         # Add to the total vote count.
#         total_votes += 1

#         # Print the candidate name from each row.
#         candidate_name = row[2]

#         if candidate_name not in candidate_options:
#           # Add the candidate name to the candidate list.
#             candidate_options.append(candidate_name)

#            # Begin tracking that candidate's vote count.
#             candidate_votes[candidate_name] = 0

#         # Add a vote to that candidate's count
#         candidate_votes[candidate_name] += 1
        
# ####if you want to show the number of votes activate this line too)
# # Print the candidate vote dictionary. 
# #print(candidate_votes)

# # Determine the percentage of votes for each candidate by looping through the counts.
# # 1. Iterate through the candidate list.
# for candidate_name in candidate_votes:
#     # 2. Retrieve vote count of a candidate.
#     votes = candidate_votes[candidate_name]
#     # 3. Calculate the percentage of votes.
#     vote_percentage = float(votes) / float(total_votes) * 100
#     # 4. Print the candidate name and percentage of votes.
#     print(f"{candidate_name}: received {vote_percentage}% of the vote.")


# #SUCCESSFUL
# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Initialize a total vote counter.
# total_votes = 0

# # Candidate options and candidate votes
# candidate_options = []
# # 1. Declare the empty dictionary.
# candidate_votes = {}

# # Winning Candidate and Winning Count Tracker
# winning_candidate = ""
# winning_count = 0
# winning_percentage = 0

# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)

#     # Read the header row.
#     headers = next(file_reader)

#     # Print each row in the CSV file.
#     for row in file_reader:
#         # Add to the total vote count.
#         total_votes += 1

#         # Print the candidate name from each row.
#         candidate_name = row[2]

#         if candidate_name not in candidate_options:
#           # Add the candidate name to the candidate list.
#             candidate_options.append(candidate_name)

#            # Begin tracking that candidate's vote count.
#             candidate_votes[candidate_name] = 0

#         # Add a vote to that candidate's count
#         candidate_votes[candidate_name] += 1
        
#  ####if you want to show the number of votes activate this line too)
#  #Print the candidate vote dictionary. 
#  #print(candidate_votes)

#  # Determine the percentage of votes for each candidate by looping through the counts.
#  # Iterate through the candidate list.
# for candidate_name in candidate_votes:
#     # Retrieve vote count of a candidate.
#     votes = candidate_votes[candidate_name]
#     # Calculate the percentage of votes.
#     vote_percentage = float(votes) / float(total_votes) * 100

#     #  To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
#     print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

#     # Determine winning vote count and candidate
#     # Determine if the votes is greater than the winning count.
#     if (votes > winning_count) and (vote_percentage > winning_percentage):
#          # If true then set winning_count = votes and winning_percent =
#          # vote_percentage.
#          winning_count = votes
#          winning_percentage = vote_percentage
#          # And, set the winning_candidate equal to the candidate's name.
#          winning_candidate = candidate_name

# #  To do: print out the winning candidate, vote count and percentage to terminal.




# #SUCCESSFUL (Module 3.5.6)
# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Initialize a total vote counter.
# total_votes = 0

# # Candidate options and candidate votes
# candidate_options = []
# # Declare the empty dictionary.
# candidate_votes = {}

# # Winning Candidate and Winning Count Tracker
# winning_candidate = ""
# winning_count = 0
# winning_percentage = 0

# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)

#     # Read the header row.
#     headers = next(file_reader)

#     # Print each row in the CSV file.
#     for row in file_reader:
#         # Add to the total vote count.
#         total_votes += 1

 

#         # Print the candidate name from each row.
#         candidate_name = row[2]

#         if candidate_name not in candidate_options:
#           # Add the candidate name to the candidate list.
#             candidate_options.append(candidate_name)

#            # Begin tracking that candidate's vote count.
#             candidate_votes[candidate_name] = 0

#         # Add a vote to that candidate's count
#         candidate_votes[candidate_name] += 1
        
#  #Print the candidate vote dictionary. 
#  #print(candidate_votes)
# # Print the total votes.
# print(f'The Total number of votes is: {total_votes}.')

#  # Determine the percentage of votes for each candidate by looping through the counts.
#  # Iterate through the candidate list.
# for candidate_name in candidate_votes:
#     # Retrieve vote count of a candidate.
#     votes = candidate_votes[candidate_name]
#     # Calculate the percentage of votes.
#     vote_percentage = float(votes) / float(total_votes) * 100

#     #  To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
#     print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

 
#     # Determine winning vote count and candidate
#     # Determine if the votes is greater than the winning count.
#     if (votes > winning_count) and (vote_percentage > winning_percentage):
#          # If true then set winning_count = votes and winning_percent =
#          # vote_percentage.
#          winning_count = votes
#          winning_percentage = vote_percentage
#          # And, set the winning_candidate equal to the candidate's name.
#          winning_candidate = candidate_name

# #  To do: print out the winning candidate, vote count and percentage to terminal.
# winning_candidate_summary = (
#     f"-------------------------\n"
#     f"Winner: {winning_candidate}\n"
#     f"Winning Vote Count: {winning_count:,}\n"
#     f"Winning Percentage: {winning_percentage:.1f}%\n"
#     f"-------------------------\n")
# print(winning_candidate_summary)





# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)