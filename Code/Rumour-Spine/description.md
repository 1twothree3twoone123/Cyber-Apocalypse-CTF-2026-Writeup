# Rumour Spine
Difficulty: **hard**

## Challenge Requirements

### Rumour Spine
Suncourt doesn't march first — it primes first. Miren Vale has traced the
Quiet March's invitation chain: a coordinator who never touches ash, only
schedules, feeding a priming signal through a network of quiet hands —
candle-buyers, shrine-attendants, penitent-scribes — until a target
district falls still the night before the March arrives. Every hand who
passes the signal on is a link Miren can expose.

Miren means to break the chain before the district goes quiet. She can
expose any quiet hand along the way — one flagged, one route burned, at
the cost of one favour she can never call in again. The coordinator and
the target district can't be touched directly: too visible, too soon.
What is the minimum number of quiet hands that must be exposed to sever
every path the priming signal could still travel?

The first line contains four space-separated integers: N E S T.
N is the number of quiet hands (nodes, labelled 0 to N-1).
E is the number of directed links (edges) the priming signal can travel.
S is the coordinator node.
T is the target district node.

Each of the next E lines contains two space-separated integers u and v,
representing a directed link along which the signal can pass from hand u
to hand v.

Print a single integer: the minimum number of hands (nodes other than S
and T) that must be exposed to disconnect all paths from S to T.


6 <= N <= 120  
1 <= E <= 360  
S = 0, T = N-1  
The graph may contain cycles  
It is guaranteed that at least one path from S to T exists  
It is guaranteed that there is no direct edge from S to T  

```
Example:

Input:
7 8 0 6
0 1
0 2
1 3
2 4
3 6
4 6
2 3
1 4

Expected output:
2

The paths the priming signal can take from node 0 to node 6 are:
  0 -> 1 -> 3 -> 6
  0 -> 1 -> 4 -> 6
  0 -> 2 -> 3 -> 6
  0 -> 2 -> 4 -> 6

No single hand lies on all four paths, so exposing one alone can't cut the
coordinator off from the target district. Exposing both hands 1 and 2
leaves no surviving path from 0 to 6, so the answer is 2.
```