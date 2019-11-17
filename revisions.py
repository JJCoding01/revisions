"""
Simple script to generate revision letters using the an alpha revision scheme
with an initial release of 0.
"""

from itertools import cycle


class MaximumRevisionError(Exception):
    """
    Exception for when the sequence runs out and revisions start repeating
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)


def revisions(sequence="full"):
    """
    Generates infinite series of revisions

    Creates a generator that will iterate over an infinite sequence of
    revisions in the form
    0, A, B, C, ..., X, Y, Z, AA, AB, AC, ..., AX, AY, AZ, BA, BB, BC, ...

    yield: revision
    yield type: str
    """
    if sequence == "full":
        sequence = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif sequence == "partial":
        # missing i, o, and s
        sequence = "ABCDEFGHJKLMNPQRTUVWXYZ"
    else:
        # for simplicity here, do not allow custom sequences
        raise ValueError(
            f"sequence parameter must be either "
            f"'full', or 'partial', not {sequence}"
        )

    # yield the initial release as revision 0
    yield "0"

    # create a revision cycle, and a suffix cycle. The suffix cycle is the same
    # as the revision cycle, but will be incremented at a different rate. The
    # suffix will be used when the revision cycles through and starts repeating
    rev_cycle = cycle(sequence)
    suffix_cycle = cycle(sequence)

    # length of revision cycle. This will be used to determine when a suffix
    # is required.
    rev_length = len(sequence)
    rev_limit = rev_length + rev_length ** 2

    suffix = ""  # initially, no suffix (A, B, C, ...)
    for k, rev in enumerate(rev_cycle):
        if rev_limit < k:
            # limit of sequence with a single suffix have been reached
            # break
            msg = f"maximum revision level ({rev_limit}) has been reached!"
            raise MaximumRevisionError(msg)

        if k % rev_length == 0 and k > 0:
            # increment the suffix every time the revision list rolls over
            suffix = next(suffix_cycle)
        yield suffix + rev
