from state import users
from state import songs, bids
from models import Bid


def create_bid(user_id, song_id, bid_amount):
    user = users.get(user_id)

    if user is None:
        raise ValueError("User not found")

    song = songs.get(song_id)
    if song is None:
        raise ValueError("Song not found")

    if bid_amount <= 0:
        raise ValueError("Bid must be positive")
    
    bids[len(bids) + 1] = Bid(
        id=len(bids) + 1,
        party_id=song.party_id,
        user_id=user_id,
        song_id=song_id,
        amount=bid_amount
    )
    return bids[len(bids)]

def determine_winner(bids):
    if not bids:
        return None
    sorted_bids = sorted(bids, key=lambda bid: bid.amount, reverse=True)

    bid = sorted_bids[0]
    user_id = bid.user_id
    user = users[user_id]
    user.tokens -= bid.amount

    return bid
   