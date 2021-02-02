def selection_sort(coll):
    """
    Selection Sort Implementation.
    Time O(n^2) run.
    O(1) space complexity.
    """
    for i in range(len(coll)):
        min_index = i
        for j in range(i + 1, len(coll)):
            if coll[j] < coll[min_index]:
                min_index = j

        coll[i], coll[min_index] = coll[min_index], coll[i]


l1 = [99, 44, 3, 0]
l = [99, 44, 600, 2, 1, 5, 63, -100, 87, 283, 4, 0, -1, 0]
selection_sort(l)
print(l)
