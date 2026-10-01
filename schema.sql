CREATE TABLE party (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    join_code TEXT NOT NULL UNIQUE,
    host_user_id BIGINT NOT NULL REFERENCES user(id)
    created_at TIMESTAMPZ NOT NULL DEFAULT NOW()

);

CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    party_id BIGINT REFERENCES party(id)
    created_at TIMESTAMPZ NOT NULL DEFAULT NOW()
);