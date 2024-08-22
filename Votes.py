class VotingSystem:
    def __init__(self):
        self.registered_voters = {}
        self.votes = {}
        self.voted_voters = set()

    def register_voter(self, voter_id, name):
        if voter_id in self.registered_voters:
            print(f"Voter with ID {voter_id} is already registered.")
        else:
            self.registered_voters[voter_id] = name
            print(f"Voter {name} registered successfully with ID {voter_id}.")

    def cast_vote(self, voter_id, candidate):
        if voter_id not in self.registered_voters:
            print("Voter not registered.")
            return
        
        if voter_id in self.voted_voters:
            print(f"Voter with ID {voter_id} has already voted.")
            return

        if candidate not in self.votes:
            self.votes[candidate] = 0
        
        self.votes[candidate] += 1
        self.voted_voters.add(voter_id)
        print(f"Vote cast successfully by {self.registered_voters[voter_id]} for {candidate}.")

    def get_results(self):
        if not self.votes:
            print("No votes have been cast yet.")
            return
        
        print("Voting results:")
        for candidate, vote_count in self.votes.items():
            print(f"{candidate}: {vote_count} votes")

    def check_voter(self, voter_id):
        if voter_id in self.registered_voters:
            print(f"Voter ID {voter_id} belongs to {self.registered_voters[voter_id]}.")
        else:
            print(f"Voter ID {voter_id} is not registered.")

# Example usage
voting_system = VotingSystem()

# Register voters
voting_system.register_voter("V001", "Alice")
voting_system.register_voter("V002", "Bob")

# Attempt to register the same voter again
voting_system.register_voter("V001", "Alice")

# Cast votes
voting_system.cast_vote("V001", "Candidate_A")
voting_system.cast_vote("V002", "Candidate_B")

# Attempt to vote again with the same voter ID
voting_system.cast_vote("V001", "Candidate_A")

# Check voter information
voting_system.check_voter("V001")
voting_system.check_voter("V003")

# Get voting results
voting_system.get_results()
