# Three Tankards and a Lie
Difficulty: **very easy**

## Challenge Requirements

### Three Tankards and a Lie

The Drowned Bell doesn't ask questions — which is exactly why Ferro
Quicktongue runs his nightly game there. Three dented tankards, one bent
copper chit, and a room full of off-duty gate clerks who really ought to
know better than to bet against a man whose hands move faster than his
mouth. Half the tavern is three mugs deep and hollering wagers by the
time Rin Kagetsura wanders in, off duty and not remotely interested in
Ferro's game.

What catches Rin's eye is the table by the door, where a courier is
running the exact same swap-and-shuffle — except the thing sliding under
those tankards isn't a copper chit, it's a folded scrap bound for
someone at Suncourt, and the courier is betting that nobody in a room
this drunk is actually watching the cups. Rin is watching. Every swap
happens in plain sight, same as Ferro's — the only question left is
which tankard the message is sitting under once the shuffling finally
stops.

A handful of patrons had already marked which tankard they were
following before the swapping started, chasing their own side bets on
where their cup would land. Rin doesn't care about their coin — but
working out where every marked tankard actually ends up, theirs
included, is the only way to know which one held the real message.

The first line contains three space-separated integers: N M Q.
N is the number of tankards on the bar, numbered 1 to N. Tankard i starts
by holding item i.
M is the number of swaps performed, in order.
Q is the number of starting positions to track.

Each of the next M lines contains two space-separated integers a b — the
two positions whose contents are exchanged.

Each of the next Q lines contains a single integer p — a starting
position whose final resting place must be reported.

Print Q lines. For each queried starting position p, print the position
of the item that started at p, after all M swaps have been applied in
order.

1 <= N <= 2000  
0 <= M <= 5000  
1 <= Q <= 2000  
1 <= a, b <= N  
1 <= p <= N

```
Example:

Input:
5 4 2
1 3
2 4
3 5
4 1
3
5

Expected output:
4
3

The item that started at position 3: the swap (1,3) moves it to position
1. Neither (2,4) nor (3,5) touches position 1, so it stays there until
the swap (4,1) moves it to position 4.

The item that started at position 5: neither (1,3) nor (2,4) touches
position 5. The swap (3,5) moves it to position 3, and the final swap
(4,1) doesn't touch position 3, so it stays there.

Final positions: the item that started at 3 ends at 4; the item that
started at 5 ends at 3.
```