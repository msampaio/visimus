from django.test import TestCase
import music

class MusicTest(TestCase):
    def test_transposition(self):
        self.assertEqual(music.transposition([1,2,3], 2), [3,4,5])
        self.assertEqual(music.transposition([10,11,0], 3), [1,2,3])

    def test_inversion(self):
        self.assertEqual(music.inversion([0, 4, 7], 0), [0, 8, 5])

    def test_inversion_first_note(self):
        self.assertEqual(music.inversion_first_note([3, 7, 9]), [3, 11, 9])

    def test_transposition_startswith(self):
        self.assertEqual(music.transposition_startswith([3, 5, 6], 7), [7, 9, 10])

    def test_rotate(self):
        self.assertEqual(music.rotate([1,2,3]), [2,3,1])

    def test_intervals(self):
        self.assertEqual(music.intervals([1, 2, 3]), [1, 1])
        self.assertEqual(music.intervals([0, 4, 7]), [4, 3])
        self.assertEqual(music.intervals([0, 11, 3]), [11, 4])

    def test_matrix(self):
        row = [4, 5, 7, 1, 6, 3, 8, 2, 11, 0, 9, 10]
        matrix = [[4, 5, 7, 1, 6, 3, 8, 2, 11, 0, 9, 10],
            [3, 4, 6, 0, 5, 2, 7, 1, 10, 11, 8, 9],
            [1, 2, 4, 10, 3, 0, 5, 11, 8, 9, 6, 7],
            [7, 8, 10, 4, 9, 6, 11, 5, 2, 3, 0, 1],
            [2, 3, 5, 11, 4, 1, 6, 0, 9, 10, 7, 8],
            [5, 6, 8, 2, 7, 4, 9, 3, 0, 1, 10, 11],
            [0, 1, 3, 9, 2, 11, 4, 10, 7, 8, 5, 6],
            [6, 7, 9, 3, 8, 5, 10, 4, 1, 2, 11, 0],
            [9, 10, 0, 6, 11, 8, 1, 7, 4, 5, 2, 3],
            [8, 9, 11, 5, 10, 7, 0, 6, 3, 4, 1, 2],
            [11, 0, 2, 8, 1, 10, 3, 9, 6, 7, 4, 5],
            [10, 11, 1, 7, 0, 9, 2, 8, 5, 6, 3, 4]]

        self.assertEqual(music.row_matrix(row), matrix)
