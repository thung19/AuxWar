from models import Party, User, Song
from state import parties, users, songs

def seed_data():
    users[1] = User(
        id=1,
        username="Thomas",
        party_id=1,
        tokens=100
    )

    users[2] = User(
        id=2,
        username="David",
        party_id=1,
        tokens=100
    )

    users[3] = User(
        id=3,
        username="Sam",
        party_id=1,
        tokens=100
    )

    # Party
    parties[1] = Party(
        id=1,
        name="Thomas's Party",
        join_code="AUX123",
        host_user_id=1
    )

    # Songs
    songs[1] = Song(
        id=1,
        party_id=1,
        title="Nights",
        artist="Frank Ocean",
        submitted_by=1
    )

    songs[2] = Song(
        id=2,
        party_id=1,
        title="Mr. Brightside",
        artist="The Killers",
        submitted_by=2
    )

    songs[3] = Song(
        id=3,
        party_id=1,
        title="Runaway",
        artist="Kanye West",
        submitted_by=3
    )