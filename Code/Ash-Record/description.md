# Ash Record
Difficulty: **medium**

## Challenge Requirements

### Ash Record
Aeron's scouts found a riverside hamlet that should have been starving. The
ovens were still warm. The stew pot was fresh. The chairs were set, then
abandoned mid-meal. Elowen Ashglass reads the scene like a staged
confession: soot where it shouldn't cling, drag-marks that don't match
panic, footprints that kept their spacing instead of scattering. This
wasn't a raid — it was a procession, and someone wanted the hamlet
preserved, not burned.

Elowen has recovered residues across the site, each carrying a timestamp
and a material type. She also holds the extraction sequence she suspects
was followed — the order materials would appear in if hands moved people
out calmly, stage by stage, from entry to compliance to departure. She
needs the longest prefix of that sequence she can actually confirm: a
subsequence of residues matching it in order, where no two consecutively
matched residues are closer together than a minimum gap, because no stage
of an orderly extraction happens faster than that.

The first line contains three space-separated integers: N P min_gap.
N is the number of recovered residues.
P is the length of the suspected extraction sequence.
min_gap is the minimum time difference required between any two consecutively
matched residues.

The second line contains P space-separated strings: the material types in the
extraction sequence, in order.

Each of the next N lines describes one recovered residue as two space-separated
values: an integer timestamp and a material type string.

Residues are not necessarily given in timestamp order.

Print a single integer: the maximum number of consecutive steps from the
beginning of the extraction sequence that can be confirmed by a subsequence
of residues satisfying the time gap constraint.


1 <= N <= 5000  
1 <= P <= 12  
1 <= min_gap <= 10  
1 <= timestamp <= 10000  
Material type strings consist of lowercase letters, length <= 10  

```
Example:

Input:
5 4 3
ash rope oil ash
1 ash
4 rope
7 oil
10 ash
11 rope

Expected output:
4

The suspected extraction sequence is: ash, rope, oil, ash.
The minimum time gap between consecutively matched residues is 3.

Confirming the full sequence of 4 steps:
  Step 1: residue at timestamp 1, type ash.
  Step 2: residue at timestamp 4, type rope.  Gap from step 1: 3 >= 3.
  Step 3: residue at timestamp 7, type oil.   Gap from step 2: 3 >= 3.
  Step 4: residue at timestamp 10, type ash.  Gap from step 3: 3 >= 3.

All four steps are confirmed with valid gaps, so the answer is 4.
The residue at timestamp 11 (rope) is not needed for this match.
```