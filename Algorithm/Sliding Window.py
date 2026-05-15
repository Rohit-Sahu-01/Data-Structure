#  Sliding Window Algorithm
#  Time Complexity: O(n)

# Logic: We will maintain a window of size k and keep track of the sum of the elements in the current window. As we slide the window from left to right, we will update the sum by adding the new element and removing the old element that is sliding out of the window. We will keep track of the maximum sum encountered during this process.    
def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return -1

    max_sum = 0
    window_sum = sum(arr[:k])

    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
result = max_sum_subarray(arr, k)
print("Maximum sum of a subarray of size", k, "is:", result)
