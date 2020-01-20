import csv 
import os

print("Election Results")
print("-------------------------")

totalVotes = 0
# Create a list to store the word 'Khan' 
Khan = []
# Create a list to store the word 'Correy' 
Correy = []
# Create a list to store the word 'Li' 
Li = []
# Create a list to store the word 'O'Tooley' 
OTooley = []


csvpath = os.path.join("Resources","election_data.csv")
with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
    #loop through each row of data after the header
    for row in csv_reader:
        #the number of row looped equals to the number of total vote
        totalVotes = totalVotes + 1
        #if we come across the word 'Khan', add it to the list; length of string euqals to the number of times 'Khan' appears
        if row[2] == "Khan":
            Khan.append(row[2])
            KhanVote = len(Khan)
        #if we come across the word 'Correy', add it to the list; length of string euqals to the number of times 'Correy' appears
        if row[2] == "Correy":
            Correy.append(row[2])
            CorreyVote = len(Correy)
        #if we come across the word 'Li', add it to the list; length of string euqals to the number of times 'Li' appears
        if row[2] == "Li":
            Li.append(row[2])
            LiVote = len(Li)
        #if we come across the word 'O'Tooley', add it to the list; length of string euqals to the number of times 'O'Tooley' appears
        if row[2] == "O'Tooley":
            OTooley.append(row[2])
            OTooleyVote = len(OTooley)
#create a dictionary that store the name of the candidates as key, the number of votes they get as value
votes = {'Khan': KhanVote, 'Correy': CorreyVote, 'Li': LiVote, "O'Tooley": OTooleyVote}


print(f'Total Votes: {totalVotes}')
print("-------------------------")
print(f'Khan: {(KhanVote/totalVotes * 100):.3f}% ({KhanVote})')
print(f'Correy: {(CorreyVote/totalVotes * 100):.3f}% ({CorreyVote})')
print(f'Li: {(LiVote/totalVotes * 100):.3f}% ({LiVote})')
print("O'Tooley: " + f'{(OTooleyVote/totalVotes * 100):.3f}% ({OTooleyVote})')
print('-------------------------')
print(f'Winner: {max(votes, key=votes.get)}')
print('-------------------------')

#set variable for output file
output_file = os.path.join("election_data.txt")
#open the output file
with open(output_file, 'w') as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f'Total Votes: {totalVotes}\n')
    text_file.write("-------------------------\n")
    text_file.write(f'Khan: {(KhanVote/totalVotes * 100):.3f}% ({KhanVote})\n')
    text_file.write(f'Correy: {(CorreyVote/totalVotes * 100):.3f}% ({CorreyVote})\n')
    text_file.write(f'Li: {(LiVote/totalVotes * 100):.3f}% ({LiVote})\n')
    text_file.write("O'Tooley: " + f'{(OTooleyVote/totalVotes * 100):.3f}% ({OTooleyVote})\n')
    text_file.write('-------------------------\n')
    text_file.write(f'Winner: {max(votes, key=votes.get)}\n')
    text_file.write('-------------------------\n')
text_file.close
    