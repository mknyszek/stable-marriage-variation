stable-marriage-variation
=========================

This project was an idea I got when doing a problem for CS 70: Discrete Math &amp; Probability at UC Berkeley. 

The Problem 
-----------
Like in the stable marriage problem, Joe Greedy wants to ﬁnd a stable pairing between n men m1;:::;mn and
n women w1;:::;wn with some given lists of preferences. Despite the simplicity of the Propose & Reject
procedure, Joe feels like it does not appeal to his innate sense of aesthetics. Instead, he decides he will use
the following procedure:

(a) Start by assigning man mi with women wi for all i = 1:::n.
In other words, let S = {(m1;w1);:::;(mn;wn)}.

(b) Repeat everyday the following unless there is no rogue pair in S:
    
  (a’) Pick a rogue pair (m∗;w∗).
    
  (b’) Swap partners so that m∗ and w∗ are together in the new pairing. That is, if we previously had S = {:::;(m∗;w′);:::;(m′;w∗);:::}, we now have S = {:...,(m∗;,w∗);:::;(m′;w′);:::} while the other couples remain the same.

Does this procedure work no matter how Joe picks the rogue pair in step (a)? Prove or give counter example.

The Code
--------
Part of the solution involves finding a loop to know whether a pairing can be ever be recreated.

This program creates a "poor man's directed graph" (i.e. a bunch of Python dictionaries) out of the possible pairings that occur when one tries to eliminate one of the rogue couples by swapping partners. Then, it runs a depth-first search to find cycles in the graph.

This isn't the world's most robust piece of code, but it was enjoyable to write and think about. It also helped me out with the problem by helping me prove the solution to myself.

And yes I know the solution to the problem, and no I will not say what it is. :P
