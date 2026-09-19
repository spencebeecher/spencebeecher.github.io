---
title: Living Legends: an RPG where the rules are code and the AI only narrates
date: 2026-09-19
summary: What I'm building: a tabletop role-playing game with a generated, hand-inked world, built day to day by two AI agents that play it and fix it.
---

Living Legends is a tabletop role-playing game I've been building since March. It runs on the D&D 5e rules (the open SRD), and it has one firm rule of its own: **the rules engine decides everything, and the language model only narrates.** Every roll, every shift in how far a character trusts you, every secret they give up is computed and replayable from a seed. The model turns those outcomes into prose inside a contract listing what it may and may not say, so it can't invent a fact or hand over a secret you didn't earn.

Characters aren't scripted. Each is built from tags like `STUBBORN`, `INNKEEPER` and `PROTECT_LOVED_ONES` that carry behaviour and move the difficulty of your checks, and each keeps secrets behind escalating checks that trust makes easier. Push too hard on the same angle and they get annoyed, mechanically. The scope is deliberately small for now: one town of about a thousand people and the land around it.

![A generated world map: continents, rivers, mountains, forests and towns](../assets/living-legends/map.jpg)

*Thunderdale, one generated world: 26 places (2 cities, 11 towns and 13 market towns) holding 53,170 people across roughly 150 km.*

## The map

The world is generated, then drawn in a hand-inked style. A heightmap becomes continents; rivers start in the snowfields and join on their way to the sea; the number of towns comes from the land area at about the population density of England around 1300, and each is sized by rank. Roads are routed to avoid climbing, merge when they head for the same town, and get a town of their own where three of them cross.

![A close-up of hatched mountains, a coastal city and towns](../assets/living-legends/detail.jpg)

*Up close: hatched mountains with snow caps, forests coloured by kind, a ringed dot for a city and plain dots for towns.*

![A small town at a road junction](../assets/living-legends/crossroads.jpg)

*Salt Gate, a town that grew where three roads meet.*

![The same map before and after sizing towns by land area](../assets/living-legends/before-after.jpg)

*The same world before and after sizing towns by land area: ten places became twenty-five, with roads out to the ones beside them.*

You can [explore the map](../assets/living-legends/thunderdale-atlas.html): hover a town for its name, click it for its population and the roads that reach it.

## Who builds it

Most of the day-to-day work is done by two AI agents with separate jobs. A **playtester**, running on a local language model, plays the game unattended, talking, rolling checks and fighting, and writes down where it got stuck or confused. A **fixer**, an AI coding agent (Claude Code), reads those findings one at a time and turns each into a tested change on its own branch. Merging into the main line stays my job, and neither agent grades its own work. Since March that has come to about 1,700 commits and over 700 test files.

Next is the milestone the small scope was chosen for: one town, its 41 trades and 60 named people, playable end to end.
