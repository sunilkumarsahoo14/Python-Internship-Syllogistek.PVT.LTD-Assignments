#Q3.find the winner
def find_winner(votes):
    # initialize an empty dictionary
    vote_count = {}
    
    # count the votes for each candidate
    for candidate in votes:
        if candidate in vote_count:
            vote_count[candidate] += 1
        else:
            vote_count[candidate] = 1
    
    # find the candidate with the maximum votes
    max_votes = 0
    winner = None

    for candidate, count in vote_count.items():
        if count > max_votes:
            max_votes = count
            winner = candidate
    
    return winner

votes = ['a', 'b', 'a', 'c', 'a']
winner = find_winner(votes)
#print the result
print("The winner is:", winner)
