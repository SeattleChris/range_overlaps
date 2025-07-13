# range_overlaps

In a sports ball game, one team has `N` number of shots with given ranges (inclusive) while the opposing team has `M` number of players who each have a given response range (inclusive). If there is *any* overlap, including at the inclusive ends, of a player's response range and a shot's range than that is considered covered for that player. A player's strength is how many different shots they can cover. The team strength is the sum of all of the player's strengths.

## Function

*Inputs*: Given `N` number of shot ranges and `M` number of player response ranges, with all ranges given as two `int` inclusive end points.

*Returns*: An `int` for team strength as described.

*Constraints*:
1 <= `N`, `M` <= 10^5
1 <= all range endpoints (start or end) <= 10^8
