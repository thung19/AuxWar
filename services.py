from state import users
from state import songs, bids, parties, rounds
from models import Bid, Party


def create_bid(user_id, song_id, bid_amount):
    user = users.get(user_id)

    if user is None:
        raise ValueError("User not found")

    song = songs.get(song_id)
    if song is None:
        raise ValueError("Song not found")

    if user.party_id != song.party_id:
        raise ValueError("User and song are not in the same party")

    if bid_amount <= 0:
        raise ValueError("Bid must be positive")

    if bid_amount > user.tokens:
        raise ValueError("Insufficient funds")
    
    bid_id = len(bids) + 1

    party = parties.get(song.party_id)

    bids[bid_id] = Bid(
        id=bid_id,
        party_id=song.party_id,
        user_id=user_id,
        song_id=song_id,
        amount=bid_amount,
        round_id=party.current_round_id
    )
    return bids[bid_id]

def determine_winner(bids):
    if not bids:
        return None
    return max(bids, key=lambda bid: bid.amount)

def end_round(party_id):
    party = parties.get(party_id)
    if party is None:
        raise ValueError("Party not found")
    
    round_bids = [bid for bid in bids.values() if bid.round_id == party.current_round_id]

    winning_bid = determine_winner(round_bids)

    if winning_bid is not None:
        winner = users[winning_bid.user_id]
        winner.tokens -= winning_bid.amount

    party.current_round_id += 1

    return winning_bid

def create_party(name, join_code, host_user_id):
    party_id = len(parties) + 1
    parties[party_id] = Party(
        id=party_id,
        name=name,
        join_code=join_code,
        host_user_id=host_user_id,
        current_round_id=1
    )
    return parties[party_id]

def join_party(user_id, party_id):
    user = users.get(user_id)
    if user is None:
        raise ValueError("User not found")

    party = parties.get(party_id)
    if party is None:
        raise ValueError("Party not found")

    user.party_id = party_id
    return user

def leave_party(user_id):
    user = users.get(user_id)
    if user is None:
        raise ValueError("User not found")

    user.party_id = None
    return user