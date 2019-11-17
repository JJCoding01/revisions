import unittest
from revisions import revisions, MaximumRevisionError


class TestRevisionErrors(unittest.TestCase):
    def test_sequence_errors(self):
        msg = "invalid sequence did not raise a ValueError"
        with self.assertRaises(ValueError, msg=msg):
            next(revisions("not full or partial"))

    def test_maximum_revision_error(self):

        limits = [(26 + 26 ** 2, "full"), (23 + 23 ** 2, "partial")]
        for limit, sequence in limits:
            msg = f"revisions went past limit for {sequence} sequence"
            with self.assertRaises(MaximumRevisionError, msg=msg):
                for k, _ in enumerate(revisions(sequence)):
                    if k > limit + 1:
                        # break after the limit of the generator should have
                        # reached its limit and raised an error. This ensures
                        # that this test will exit, even if generator is
                        # infinite
                        break


class TestRevisionSequences(unittest.TestCase):
    def test_full_sequence(self):
        expected_revs = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for expected_rev, actual_rev in zip(expected_revs, revisions()):
            self.assertEqual(
                expected_rev,
                actual_rev,
                msg="starting full sequence does not match expected",
            )

    def test_partial_sequence(self):
        expected_revs = "0ABCDEFGHJKLMNPQRTUVWXYZ"
        for expected_rev, actual_rev in zip(
            expected_revs, revisions("partial")
        ):
            self.assertEqual(
                expected_rev,
                actual_rev,
                msg="starting partial sequence does not match expected",
            )


if __name__ == "__main__":
    unittest.main()
