[![Build Status](https://travis-ci.com/josephjcontreras/revisions.svg?branch=master)](https://travis-ci.com/josephjcontreras/revisions)

# Introduction

This is a simple script used to generate alpha revision sequences.

The initial release is specified as the number `0`, with subsequent revisions 
specified by upper case letters.

When revising revision `Z`, the next revision is `AA`. This will create the
following sequence.

```
0, A, B, C, ..., X, Y, Z, AA, AB, AC, ..., AX, AY, AZ, BA, BB, BC, ...
```

The default sequence is the whole alphabet
This can be modified by passing `"partial"` to remove letters `I`, `O`,
and `S` to avoid confusing them with numbers `1`, `0`, and `5`.

The disadvantage of using `"partial"`, is that there are fewer revisions that 
can be made compared to `"full"`.
 
```
# "full"
# length: 26
# number of revisions: 26 + 26**2 = 702 + initial release
sequence = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# "partial":
# length: 23 (alphabet without i, o, and s)
# number of revision: 23 + 23**2 = 552 + initial release
sequence = "ABCDEFGHJKLMNPQRTUVWXYZ"
```

# Errors Raised

If the parameter passed to `revision` is not either `"full"` or `"partial"`,
 a `ValueError` is raised.

When the number of revisions runs out, a `MaximumRevisionError` is raised, 
signaling the end of the revision sequence.
