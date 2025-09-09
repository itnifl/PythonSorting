# coding: utf-8

def insertion_sort(A, n):
    """
    Insertion Sort:
    We loop through the array starting from the second element.
    For each element (the 'key'), we compare it with the elements to the left.
    We shift all larger elements one position to the right until we find
    the correct position for the key.
    The key is then placed so that everything on the left is <= key
    and everything on the right is >= key.
    We continue with the next key until the whole array is sorted.
    """

    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A