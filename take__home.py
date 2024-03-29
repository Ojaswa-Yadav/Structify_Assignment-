
from collections import defaultdict
from itertools import combinations
import numpy as np

def count_chord_int(rad, id):
    chords = defaultdict(list)
    for rad, I in zip(rad, id):
        c_id = I[1:]
        if I.startswith('s'):
            chords[c_id].append(rad % (2 * np.pi))
        else:
            chords[c_id].append(rad % (2 * np.pi))
            chords[c_id].sort()
    intersections = 0
    for chord1, chord2 in combinations(chords.values(), 2):
        start1, end1 = chord1
        start2, end2 = chord2
        if (start1 < start2 < end1 < end2) or (start2 < start1 < end2 < end1):
            intersections += 1

    return intersections

#Example Input 1
radians1 = [0.78, 1.47, 1.77, 3.92]
identifiers1 = ['s_1', 's_2', 'e_1', 'e_2']
print(count_chord_int(radians1, identifiers1))

# Example Input 2
radians2 = [0.9, 1.3, 1.70, 2.92]
identifiers2 = ['s1', 'e1', 's2', 'e2']
print(count_chord_int(radians2, identifiers2))

#Example Input 3
radians3 = [0.5, 1.5, 2.5, 3.5]
identifiers3 = ['s1', 'e1', 's2', 'e2']
print(count_chord_int(radians3, identifiers3))

