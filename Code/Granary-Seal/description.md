# Granary Seal
Difficulty: **very easy**

## Challenge Requirements

### Granary Seal
The palace granaries are the last thing standing between Crownspire and open
starvation. Every ration order that reaches the gatehouse passes through
three hands: the clerk who raises it, the countersigner who clears it, and
the courier who carries it. Lysa Harrowmere keeps a custody roll for each of
the three roles — the hands the gatehouse has actually watched work, entry
by entry, over seasons of ordinary orders.

Since the Signet shattered, forged orders have been slipping through on
habit alone: clean wax, an eager countersign, a courier too calm for a
crisis. The fakes are good, but never perfect — a hand that has never
touched the roll, a clerk standing where a countersigner belongs, a courier
no custody entry has ever named. Lysa needs a count of how many orders in
the current batch survive the old sequence: every hand present, every hand
where it belongs.

The first line contains an integer C — the number of clerks on the custody roll.
The next C lines each contain one clerk's name.

The following line contains an integer CS — the number of countersigners on the custody roll.
The next CS lines each contain one countersigner's name.

The following line contains an integer R — the number of couriers on the custody roll.
The next R lines each contain one courier's name.

The following line contains an integer N — the number of orders in the batch.
Each of the next N lines describes one order as three space-separated names:
  clerk countersigner courier

Print a single integer: the number of orders in which every hand appears on
its role's custody roll.


1 <= C, CS, R <= 20  
1 <= N <= 5000  
Names consist of lowercase letters and dots, length <= 30
An order survives only if all three hands are on their role's custody roll

```
Example:

Input:
3
aldric.vowmark
bren.irongate
seyna.saltholm
3
voss.ashglass
tal.greywater
mira.crownwall
3
garren.cinders
lysa.stonepass
elric.brinemark
7
aldric.vowmark voss.ashglass garren.cinders
bren.irongate tal.greywater lysa.stonepass
cassian.embervane voss.ashglass garren.cinders
aldric.vowmark forger.oathstone garren.cinders
seyna.saltholm mira.crownwall ghost.saltwind
bren.irongate voss.ashglass elric.brinemark
seyna.saltholm tal.greywater garren.cinders

Expected output:
4

Orders 1, 2, 6, and 7 have all three hands present on their respective
custody rolls — they survive the old sequence.

Order 3 fails because cassian.embervane does not appear on the clerk roll.
Order 4 fails because forger.oathstone does not appear on the countersigner roll.
Order 5 fails because ghost.saltwind does not appear on the courier roll.
```