# z3PE68

Basically a magic tile problem, I thought, why not try this in z3?
Here I am.

## How it works
- Create Ints for all places on the 5-gon
- Constraint them 1-10 (20 constraints)
- Create an extra Int 's'
- Enforce equality of group sums against 's' (5 constraints)
- Constraint 's' from 6-27 or known value (2 or 1 constraints)
- Maximize the objective function which returns the minimum string

## The objective function

The objective function simply computes all digit strings possible
and selects the minimum out of them.

## Inference

Evaluate the objective function over the model and add 1 to all of digits
ensuring that 9 gets replaced with "10" instead of a carryover happening

<hr />

If this solution helped you with your z3 formulation then a star would be appreciated
(It's 6 am rn)
