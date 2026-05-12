"""
SLIDING WINDOW ALGORITHM EXPLANATION
=====================================

The Sliding Window technique is used to solve problems involving:
- Arrays/Strings with contiguous subsequences
- Finding optimal subarrays (max/min sum, longest substring, etc.)
- Problems that can be optimized from O(n²) to O(n)

Core Concept:
- Use two pointers (left and right) to create a "window"
- Expand the window by moving right pointer
- Shrink the window by moving left pointer
- Track results as the window slides across the data
"""

# EXAMPLE 1: Maximum Sum of Subarray of Size K
def max_sum_subarray(arr, k):
    """
    Find the maximum sum of a contiguous subarray of size k
    
    Step-by-step process:
    1. Calculate sum of first window (first k elements)
    2. Slide the window: remove left element, add right element
    3. Track the maximum sum encountered
    
    Time Complexity: O(n) instead of O(n*k) with brute force
    Space Complexity: O(1)
    """
    if len(arr) < k or k <= 0:
        return 0
    
    # Step 1: Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Step 2 & 3: Slide the window
    for i in range(k, len(arr)):
        # Remove leftmost element of previous window
        window_sum -= arr[i - k]
        # Add rightmost new element
        window_sum += arr[i]
        # Update maximum
        max_sum = max(max_sum, window_sum)
    
    return max_sum


# EXAMPLE 2: Longest Substring Without Repeating Characters
def longest_substring_without_repeating(s):
    """
    Find the length of longest substring without repeating characters
    
    Step-by-step process:
    1. Use left pointer at start, right pointer for expansion
    2. Use a dictionary to track character positions
    3. When duplicate found, move left pointer past the previous occurrence
    4. Update max length as window expands
    
    Time Complexity: O(n)
    Space Complexity: O(min(n, m)) where m is character set size
    """
    char_index = {}  # Store last seen index of each character
    max_length = 0
    left = 0  # Left boundary of window
    
    # Expand window with right pointer
    for right in range(len(s)):
        # If character already in current window
        if s[right] in char_index and char_index[s[right]] >= left:
            # Move left pointer past the previous occurrence
            left = char_index[s[right]] + 1
        
        # Update character's latest position
        char_index[s[right]] = right
        
        # Update max length (current window size)
        max_length = max(max_length, right - left + 1)
    
    return max_length


# EXAMPLE 3: Minimum Window Substring
def min_window_substring(s, t):
    """
    Find the minimum window substring in s that contains all characters in t
    
    Step-by-step process:
    1. Create frequency map of target characters
    2. Use two pointers: left and right to expand/contract window
    3. Expand window by moving right until all characters are included
    4. Contract window by moving left to find minimum length
    5. Track the minimum window found
    
    Time Complexity: O(|s| + |t|)
    Space Complexity: O(|t|) for character frequency
    """
    if not s or not t:
        return ""
    
    # Step 1: Create frequency map of target
    target_freq = {}
    for char in t:
        target_freq[char] = target_freq.get(char, 0) + 1
    
    required = len(target_freq)  # Number of unique characters to match
    formed = 0  # Number of unique characters in current window with desired frequency
    
    window_counts = {}  # Frequency map for current window
    left = 0  # Left boundary of window
    min_length = float('inf')
    min_left = 0  # Track start of minimum window
    
    # Step 2 & 3: Expand window with right pointer
    for right in range(len(s)):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        # If frequency matches target, increment formed
        if char in target_freq and window_counts[char] == target_freq[char]:
            formed += 1
        
        # Step 4: Contract window when all characters are found
        while left <= right and formed == required:
            char = s[left]
            
            # Update result if current window is smaller
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_left = left
            
            # Remove character from left
            window_counts[char] -= 1
            if char in target_freq and window_counts[char] < target_freq[char]:
                formed -= 1
            
            # Move left pointer to contract window
            left += 1
    
    return s[min_left:min_left + min_length] if min_length != float('inf') else ""


# Test cases
if __name__ == "__main__":
    # Test Example 1
    print("Example 1: Maximum Sum of Subarray")
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4
    print(f"Array: {arr}, k: {k}")
    print(f"Maximum sum: {max_sum_subarray(arr, k)}")  # Output: 24
    print()
    
    # Test Example 2
    print("Example 2: Longest Substring Without Repeating")
    s = "abcabcbb"
    print(f"String: {s}")
    print(f"Longest substring length: {longest_substring_without_repeating(s)}")  # Output: 3
    print()
    
    # Test Example 3
    print("Example 3: Minimum Window Substring")
    s = "ADOBECODEBANC"
    t = "ABC"
    print(f"String: {s}, Target: {t}")
    print(f"Minimum window: {min_window_substring(s, t)}")  # Output: "BANC"
