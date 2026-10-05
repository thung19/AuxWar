# AuxWar

## Project Premise

AuxWar is a live party music app that turns control of the aux into a game.

At the start of a party, each guest receives a limited number of virtual tokens. Guests use those tokens to bid on songs they want to hear. When it is time to choose the next song, the song with the highest winning bid gets played.

The goal is to replace the usual fight over the aux with a competitive, social system where everyone has some influence over the music.

## Core Experience

A typical party should work like this:

1. A host creates an AuxWar party.
2. Guests join the party, ideally through a QR code or join code.
3. Each guest receives a starting token balance.
4. Guests can submit songs and bid tokens on the songs they want to hear next.
5. Bids update live so everyone can see the competition.
6. When the current song ends, the winning song is selected and played.
7. Tokens spent on winning bids are deducted from the appropriate users.
8. The bidding process continues throughout the party.

Potential extensions include bidding to skip the current song, party statistics, leaderboards, spending summaries, and recaps showing moments like "Thomas spent 80 tokens on Mr. Brightside."

## Product Principles

AuxWar should feel:

- Fast and real-time
- Competitive but simple
- Easy to join without setup
- Fun to watch even when you are not currently bidding
- Designed around parties and groups rather than individual music listening

Avoid adding complexity unless it improves the live party experience.

## Development Philosophy

This project is also intended to be a fundamentals-focused software engineering build.

When helping with implementation:

- Prefer clear, understandable code over unnecessary abstraction.
- Explain why architectural or implementation decisions are being made.
- Build features incrementally rather than jumping immediately to a production-scale system.
- Keep the initial version small enough to simulate and test locally.
- Do not introduce infrastructure such as Redis, Kafka, microservices, or complex distributed systems until the project actually needs them.
- Favor learning core backend, database, API, state-management, concurrency, and real-time system concepts through the project.

## Current Goal

The initial goal is a functional prototype where multiple users can join a party, receive tokens, submit songs, place bids, determine a winning song, and progress through multiple bidding rounds.