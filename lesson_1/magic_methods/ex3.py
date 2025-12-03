# Exercise 3

"""
Challenge: Create the classes needed to make the following code work as shown:
"""

class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0
    
    def __iadd__(self, other):
        self.votes += other
        return self.votes
    
    def __str__(self):
        return f'{self.name}: {self.votes}'
    
class Election:
    def __init__(self, candidates):
        self.candidates = candidates
    
    def results(self):
        total = 0
        most_votes = 0
        most_voted = None
        for candidate in self.candidates:
            total += candidate.votes
            if candidate.votes > most_votes:
                most_votes = candidate.votes
                most_voted = candidate.name
            print(candidate)
        print()
        print(f'{most_voted} won: {(most_votes/total)*100:.2f}% of votes')


mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()

# Mike Jones: 3 votes
# Susan Dore: 4 votes
# Kim Waters: 1 votes

# Susan Dore won: 50.0% of votes