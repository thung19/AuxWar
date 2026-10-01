from dataclasses import dataclass

@dataclass
class User:
    id: int
    username: str
    tokens: int
    party_id: int

@dataclass
class Party:
    id: int
    name: str
    join_code: str
    host_user_id: int

@dataclass
class Song:
    id: int
    title: str
    artist: str
    party_id: str
    submitted_by: int

@dataclass
class Bid:
    id: int
    party_id: int
    user_id: int
    song_id: int
    amount: int

