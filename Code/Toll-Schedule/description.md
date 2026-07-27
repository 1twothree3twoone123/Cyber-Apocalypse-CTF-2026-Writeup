# Toll Schedule
Difficulty: **easy**

## Challenge Requirements

### Toll Schedule

Stonepass doesn't close for weather anymore. It closes on words borrowed
from weather — "raiders," "avalanches," "public order" — while the schedule
underneath keeps quietly playing favourites: one banner's convoys glide
through, another's stack up in the snow until daylight dies. Elric Ashspar
has spent weeks sketching the checkpoint's hardware and is certain of one
thing — the mechanism isn't broken. It's tuned.

To prove it, Elric first needs the number nobody at the gate wants
published: the least total time this exact column of convoys could
possibly spend waiting, under any legal assignment of clearances to
convoys. Each convoy reaches the pass at a known time; each clearance
opens at a known time and can seat exactly one convoy, no earlier than its
arrival. Elric must find the assignment that minimises the column's total
wait — the clean baseline the real schedule will be measured against.

The first line contains two space-separated integers: N and G.
N is the number of convoys.
G is the number of available checkpoint clearances (G >= N).

The second line contains N space-separated integers: the arrival time of each
convoy (in any order).

The third line contains G space-separated integers: the opening time of each
checkpoint clearance (in any order).

A convoy may only be assigned to a clearance that opens at or after the
convoy's arrival time. Each convoy must be assigned to exactly one clearance.
Each clearance can handle at most one convoy. It is guaranteed that a valid
assignment exists.

Print a single integer: the minimum total waiting time across all convoys,
where the waiting time for a convoy is its clearance's opening time minus
the convoy's arrival time.


1 <= N <= 1200  
N <= G <= 1500  
1 <= arrival time <= 200  
1 <= clearance opening time <= 220  
It is guaranteed that every convoy can be assigned to a distinct clearance

```
Example:

Input:
4 4
2 4 6 9
3 5 8 11

Expected output:
6

The four convoys arrive at times 2, 4, 6, and 9.
The four checkpoint clearances open at times 3, 5, 8, and 11.

One valid assignment that achieves the minimum total wait:
  Convoy arriving at 2 -> clearance opening at 3.  Wait: 1.
  Convoy arriving at 4 -> clearance opening at 5.  Wait: 1.
  Convoy arriving at 6 -> clearance opening at 8.  Wait: 2.
  Convoy arriving at 9 -> clearance opening at 11. Wait: 2.

Total waiting time: 1 + 1 + 2 + 2 = 6.
```