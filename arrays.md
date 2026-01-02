# Array-Based Data Structures and Algorithms Interview Problems

A curated list of frequently asked array problems for technical interview preparation, organized by difficulty and problem-solving patterns.

---

## 📊 Table of Contents

- [Easy Problems](#easy-problems)
- [Medium Problems](#medium-problems)
- [Hard Problems](#hard-problems)
- [Pattern Index](#pattern-index)

---

## Easy Problems

### Sorting & Searching
1. **Two Sum** (LeetCode 1)
   - Pattern: Hashing with arrays
   - Time: O(n), Space: O(n)
   - Edge cases: No solution, duplicate elements

2. **Best Time to Buy and Sell Stock** (LeetCode 121)
   - Pattern: Greedy, single pass
   - Time: O(n), Space: O(1)
   - Edge cases: Empty array, descending prices

3. **Contains Duplicate** (LeetCode 217)
   - Pattern: Hashing
   - Time: O(n), Space: O(n)
   - Variants: Sort and compare (O(n log n), O(1) space)

4. **Missing Number** (LeetCode 268)
   - Pattern: Math, XOR, or sum formula
   - Time: O(n), Space: O(1)
   - Tricks: XOR properties, arithmetic sum

5. **Remove Duplicates from Sorted Array** (LeetCode 26)
   - Pattern: Two pointers (in-place)
   - Time: O(n), Space: O(1)
   - Edge cases: Empty array, single element

6. **Plus One** (LeetCode 66)
   - Pattern: Array manipulation, carry
   - Time: O(n), Space: O(1)
   - Edge cases: All 9s, leading zeros

7. **Move Zeroes** (LeetCode 283)
   - Pattern: Two pointers (in-place)
   - Time: O(n), Space: O(1)
   - Variants: Move to end vs. beginning

8. **Intersection of Two Arrays** (LeetCode 349)
   - Pattern: Set/Hashing
   - Time: O(n + m), Space: O(min(n, m))
   - Variants: Intersection with duplicates

9. **Single Number** (LeetCode 136)
   - Pattern: XOR operation
   - Time: O(n), Space: O(1)
   - Trick: XOR properties (a ^ a = 0, a ^ 0 = a)

10. **Majority Element** (LeetCode 169)
    - Pattern: Boyer-Moore Voting Algorithm
    - Time: O(n), Space: O(1)
    - Tricks: Voting algorithm, hashmap alternative

### Two Pointers
11. **Valid Palindrome** (LeetCode 125)
    - Pattern: Two pointers
    - Time: O(n), Space: O(1)
    - Edge cases: Empty string, case sensitivity

12. **Squares of a Sorted Array** (LeetCode 977)
    - Pattern: Two pointers (merge two sorted arrays)
    - Time: O(n), Space: O(n)
    - Trick: Merge from both ends

13. **Merge Sorted Array** (LeetCode 88)
    - Pattern: Two pointers (backwards)
    - Time: O(n + m), Space: O(1)
    - Trick: Fill from the end to avoid overwriting

---

## Medium Problems

### Two Pointers & Sliding Window
14. **3Sum** (LeetCode 15)
    - Pattern: Two pointers (sorted array)
    - Time: O(n²), Space: O(1) excluding output
    - Edge cases: Duplicates, negative numbers
    - Variants: 3Sum Closest, 4Sum

15. **Container With Most Water** (LeetCode 11)
    - Pattern: Two pointers (greedy)
    - Time: O(n), Space: O(1)
    - Trick: Move pointer with smaller height

16. **Trapping Rain Water** (LeetCode 42)
    - Pattern: Two pointers, prefix/suffix arrays
    - Time: O(n), Space: O(1) with two pointers
    - Alternative: Stack approach
    - Edge cases: No trapped water, all zeros

17. **Longest Substring Without Repeating Characters** (LeetCode 3)
    - Pattern: Sliding window, hashmap
    - Time: O(n), Space: O(min(n, m)) where m is charset size
    - Edge cases: Empty string, all same characters

18. **Minimum Window Substring** (LeetCode 76)
    - Pattern: Sliding window (variable)
    - Time: O(n + m), Space: O(n + m)
    - Edge cases: No valid window, multiple solutions

19. **Longest Repeating Character Replacement** (LeetCode 424)
    - Pattern: Sliding window (variable)
    - Time: O(n), Space: O(1)
    - Trick: Track max frequency in window

20. **Maximum Sum Subarray** (LeetCode 53) - Kadane's Algorithm
    - Pattern: Dynamic programming, greedy
    - Time: O(n), Space: O(1)
    - Variants: Circular subarray, print subarray
    - Edge cases: All negative numbers

21. **Subarray Sum Equals K** (LeetCode 560)
    - Pattern: Prefix sum + hashing
    - Time: O(n), Space: O(n)
    - Trick: count[prefixSum - k] technique
    - Edge cases: Negative numbers, zeros

22. **Maximum Size Subarray Sum Equals k** (LeetCode 325)
    - Pattern: Prefix sum + hashing
    - Time: O(n), Space: O(n)
    - Variant: Find longest subarray

### Binary Search
23. **Search in Rotated Sorted Array** (LeetCode 33)
    - Pattern: Binary search (modified)
    - Time: O(log n), Space: O(1)
    - Edge cases: Not rotated, duplicates
    - Variants: Find minimum in rotated array

24. **Find First and Last Position of Element** (LeetCode 34)
    - Pattern: Binary search (bounds)
    - Time: O(log n), Space: O(1)
    - Trick: Two binary searches for left/right bounds

25. **Search a 2D Matrix** (LeetCode 74)
    - Pattern: Binary search (2D)
    - Time: O(log(m*n)), Space: O(1)
    - Tricks: Flatten 2D to 1D, matrix indexing

26. **Find Peak Element** (LeetCode 162)
    - Pattern: Binary search (on answer)
    - Time: O(log n), Space: O(1)
    - Edge cases: Single element, edges are peaks

27. **Koko Eating Bananas** (LeetCode 875)
    - Pattern: Binary search on answer
    - Time: O(n * log(max(piles))), Space: O(1)
    - Trick: Binary search on the answer space

28. **Capacity To Ship Packages Within D Days** (LeetCode 1011)
    - Pattern: Binary search on answer
    - Time: O(n * log(sum(weights))), Space: O(1)
    - Similar: Split Array Largest Sum

### Prefix Sums & Difference Arrays
29. **Range Sum Query - Immutable** (LeetCode 303)
    - Pattern: Prefix sum
    - Time: O(1) query, O(n) preprocess, Space: O(n)
    - Variants: 2D prefix sums, mutable arrays

30. **Product of Array Except Self** (LeetCode 238)
    - Pattern: Prefix/suffix product
    - Time: O(n), Space: O(1) excluding output
    - Edge cases: Zero values, single zero
    - Trick: Two passes (forward and backward)

31. **Car Pooling** (LeetCode 1094)
    - Pattern: Difference array (sweep line)
    - Time: O(n), Space: O(max_location)
    - Alternative: Sorting + priority queue

32. **Corporate Flight Bookings** (LeetCode 1109)
    - Pattern: Difference array
    - Time: O(n), Space: O(n)
    - Trick: Range updates in O(1)

### Greedy & Optimization
33. **Jump Game** (LeetCode 55)
    - Pattern: Greedy
    - Time: O(n), Space: O(1)
    - Variants: Jump Game II (minimum jumps)
    - Edge cases: Start at 0, can't reach end

34. **Jump Game II** (LeetCode 45)
    - Pattern: Greedy (BFS-like)
    - Time: O(n), Space: O(1)
    - Trick: Track current and farthest reach

35. **Gas Station** (LeetCode 134)
    - Pattern: Greedy
    - Time: O(n), Space: O(1)
    - Trick: If total gas >= total cost, solution exists

36. **Non-overlapping Intervals** (LeetCode 435)
    - Pattern: Greedy (interval scheduling)
    - Time: O(n log n), Space: O(1)
    - Variants: Merge intervals, insert interval

37. **Partition Labels** (LeetCode 763)
    - Pattern: Greedy, hashmap
    - Time: O(n), Space: O(1) charset size
    - Trick: Track last occurrence of each character

38. **Boats to Save People** (LeetCode 881)
    - Pattern: Greedy, two pointers
    - Time: O(n log n), Space: O(1)
    - Trick: Sort and pair heaviest with lightest

### Subarray & Subsequence Techniques
39. **Maximum Product Subarray** (LeetCode 152)
    - Pattern: Dynamic programming
    - Time: O(n), Space: O(1)
    - Trick: Track both max and min product
    - Edge cases: Single element, zeros

40. **Longest Increasing Subsequence** (LeetCode 300)
    - Pattern: DP, binary search optimization
    - Time: O(n log n), Space: O(n)
    - Trick: Patience sorting with binary search

41. **Continuous Subarray Sum** (LeetCode 523)
    - Pattern: Prefix sum + modulo hashing
    - Time: O(n), Space: O(n)
    - Trick: If (prefixSum[j] - prefixSum[i]) % k == 0, then prefixSum[j] % k == prefixSum[i] % k

42. **Subarray Sum Divisible by K** (LeetCode 974)
    - Pattern: Prefix sum + modulo hashing
    - Time: O(n), Space: O(k)
    - Similar to problem 523

43. **Number of Subarrays with Bounded Maximum** (LeetCode 795)
    - Pattern: Counting technique
    - Time: O(n), Space: O(1)
    - Trick: Count = count(≤right) - count(≤left-1)

### Hashing & Frequency Counting
44. **Group Anagrams** (LeetCode 49)
    - Pattern: Hashing (character counting)
    - Time: O(n * k), Space: O(n * k)
    - Tricks: Character frequency array as key

45. **Longest Consecutive Sequence** (LeetCode 128)
    - Pattern: Hashset, union-find
    - Time: O(n), Space: O(n)
    - Trick: Only start counting from sequence start
    - Edge cases: Empty array, duplicates

46. **Top K Frequent Elements** (LeetCode 347)
    - Pattern: Hashing + heap/sorting
    - Time: O(n log k), Space: O(n)
    - Alternatives: Quickselect, bucket sort

47. **4Sum II** (LeetCode 454)
    - Pattern: Hashing (reduce from 4 arrays)
    - Time: O(n²), Space: O(n²)
    - Trick: Group into two pairs

### Sorting & Arrangement
48. **Sort Colors** (LeetCode 75) - Dutch National Flag
    - Pattern: Three-way partitioning
    - Time: O(n), Space: O(1)
    - Trick: Three pointers (left, current, right)

49. **Kth Largest Element in Array** (LeetCode 215)
    - Pattern: Quickselect, heap
    - Time: O(n) average, O(n²) worst, Space: O(1)
    - Alternative: Min heap of size k

50. **Merge Intervals** (LeetCode 56)
    - Pattern: Sorting, merging
    - Time: O(n log n), Space: O(n)
    - Edge cases: No overlaps, all overlaps

51. **Insert Interval** (LeetCode 57)
    - Pattern: Linear scan (sorted intervals)
    - Time: O(n), Space: O(n)
    - Edge cases: Insert at start/end/middle

52. **Largest Number** (LeetCode 179)
    - Pattern: Custom sorting
    - Time: O(n log n), Space: O(n)
    - Trick: Compare a+b vs b+a as strings

---

## Hard Problems

### Advanced Two Pointers & Sliding Window
53. **Median of Two Sorted Arrays** (LeetCode 4)
    - Pattern: Binary search (partition)
    - Time: O(log(min(m, n))), Space: O(1)
    - Trick: Binary search on partition point
    - Edge cases: Empty arrays, all elements on one side

54. **Sliding Window Maximum** (LeetCode 239)
    - Pattern: Deque (monotonic)
    - Time: O(n), Space: O(k)
    - Alternative: Segment tree, multiset
    - Trick: Maintain decreasing deque

55. **Minimum Window Subsequence** (LeetCode 727)
    - Pattern: Dynamic programming, two pointers
    - Time: O(m * n), Space: O(m * n)
    - Variant: More complex than minimum window substring

### Binary Search on Answer
56. **Split Array Largest Sum** (LeetCode 410)
    - Pattern: Binary search on answer
    - Time: O(n * log(sum)), Space: O(1)
    - Similar to: Capacity to Ship Packages

57. **Find Minimum in Rotated Sorted Array II** (LeetCode 154)
    - Pattern: Binary search with duplicates
    - Time: O(log n) average, O(n) worst, Space: O(1)
    - Edge cases: Many duplicates

58. **Kth Smallest Element in Sorted Matrix** (LeetCode 378)
    - Pattern: Binary search on answer
    - Time: O(k * log(max - min)), Space: O(1)
    - Alternative: Heap approach

59. **Minimum Size Subarray Sum** (LeetCode 209)
    - Pattern: Sliding window, binary search on answer
    - Time: O(n), Space: O(1)
    - Variant: Can use binary search with prefix sums

### Advanced Subarray Problems
60. **Maximum Sum Circular Subarray** (LeetCode 918)
    - Pattern: Kadane's + circular handling
    - Time: O(n), Space: O(1)
    - Trick: Max circular = Total - Min subarray (or max non-circular)

61. **Count of Smaller Numbers After Self** (LeetCode 315)
    - Pattern: Merge sort, Fenwick tree, segment tree
    - Time: O(n log n), Space: O(n)
    - Trick: Count inversions during merge sort

62. **Reverse Pairs** (LeetCode 493)
    - Pattern: Merge sort (counting)
    - Time: O(n log n), Space: O(n)
    - Trick: Count during merge phase

63. **Subarray Sums Divisible by K** (LeetCode 974)
    - Pattern: Prefix sum + modulo
    - Time: O(n), Space: O(k)
    - Already listed in Medium, but can be tricky

64. **Shortest Subarray with Sum at Least K** (LeetCode 862)
    - Pattern: Monotonic deque + prefix sums
    - Time: O(n), Space: O(n)
    - Edge cases: Negative numbers (makes it hard)
    - Trick: Maintain increasing deque of prefix sums

### Advanced DP & Optimization
65. **Best Time to Buy and Sell Stock IV** (LeetCode 188)
    - Pattern: Dynamic programming (state machine)
    - Time: O(n * k), Space: O(k)
    - Variants: Unlimited transactions, with cooldown, with fee

66. **Maximum Subarray Sum After One Operation** (LeetCode 1746)
    - Pattern: Dynamic programming (state tracking)
    - Time: O(n), Space: O(1)
    - Trick: Track states (not used, using, used)

67. **Cherry Pickup** (LeetCode 741)
    - Pattern: Dynamic programming (3D)
    - Time: O(n³), Space: O(n²) optimized
    - Trick: Two paths simultaneously

### Advanced Techniques
68. **First Missing Positive** (LeetCode 41)
    - Pattern: Array as hashmap (index manipulation)
    - Time: O(n), Space: O(1)
    - Trick: Use array indices as hash keys
    - Edge cases: Duplicates, large numbers

69. **Trapping Rain Water II** (LeetCode 407)
    - Pattern: Priority queue (3D version)
    - Time: O(m * n * log(m * n)), Space: O(m * n)
    - Extension: 2D version of trapping rain water

70. **Meeting Rooms III** (LeetCode 2402)
    - Pattern: Sorting + priority queues
    - Time: O(n log n), Space: O(n)
    - Trick: Track available rooms and ongoing meetings

71. **Maximum Points You Can Obtain from Cards** (LeetCode 1423)
    - Pattern: Sliding window (reverse thinking)
    - Time: O(n), Space: O(1)
    - Trick: Find minimum subarray of length (n - k)

72. **Constrained Subsequence Sum** (LeetCode 1425)
    - Pattern: Deque + dynamic programming
    - Time: O(n), Space: O(n)
    - Trick: Monotonic deque for range maximum query

73. **Maximum Number of Non-overlapping Subarrays With Sum Equals Target** (LeetCode 1546)
    - Pattern: Greedy + prefix sum + hashing
    - Time: O(n), Space: O(n)
    - Trick: Track last position, greedy selection

74. **Number of Submatrices That Sum to Target** (LeetCode 1074)
    - Pattern: 2D prefix sum + hashing
    - Time: O(m * n²), Space: O(m * n)
    - Trick: Reduce 2D to 1D subarray sum problem

75. **Minimum Operations to Reduce X to Zero** (LeetCode 1658)
    - Pattern: Sliding window (reverse)
    - Time: O(n), Space: O(1)
    - Trick: Find longest subarray with sum (total - x)

---

## Pattern Index

### Two Pointers
- Valid Palindrome (Easy)
- Squares of Sorted Array (Easy)
- Merge Sorted Array (Easy)
- 3Sum (Medium)
- Container With Most Water (Medium)
- Trapping Rain Water (Medium)
- Boats to Save People (Medium)
- Median of Two Sorted Arrays (Hard)

### Sliding Window
- Longest Substring Without Repeating Characters (Medium)
- Minimum Window Substring (Medium)
- Longest Repeating Character Replacement (Medium)
- Sliding Window Maximum (Hard)
- Minimum Size Subarray Sum (Hard)
- Maximum Points You Can Obtain from Cards (Hard)
- Minimum Operations to Reduce X to Zero (Hard)

### Binary Search
- Search in Rotated Sorted Array (Medium)
- Find First and Last Position (Medium)
- Search a 2D Matrix (Medium)
- Find Peak Element (Medium)
- Koko Eating Bananas (Medium)
- Capacity To Ship Packages (Medium)
- Split Array Largest Sum (Hard)
- Find Minimum in Rotated Sorted Array II (Hard)
- Kth Smallest Element in Sorted Matrix (Hard)

### Prefix Sums & Difference Arrays
- Range Sum Query (Medium)
- Product of Array Except Self (Medium)
- Car Pooling (Medium)
- Corporate Flight Bookings (Medium)
- Subarray Sum Equals K (Medium)
- Subarray Sum Divisible by K (Medium)
- Continuous Subarray Sum (Medium)
- Number of Submatrices That Sum to Target (Hard)

### Greedy
- Best Time to Buy and Sell Stock (Easy)
- Jump Game (Medium)
- Jump Game II (Medium)
- Gas Station (Medium)
- Non-overlapping Intervals (Medium)
- Partition Labels (Medium)
- Boats to Save People (Medium)

### Hashing
- Two Sum (Easy)
- Contains Duplicate (Easy)
- Intersection of Two Arrays (Easy)
- Group Anagrams (Medium)
- Longest Consecutive Sequence (Medium)
- Top K Frequent Elements (Medium)
- 4Sum II (Medium)
- First Missing Positive (Hard)

### Dynamic Programming (Arrays)
- Maximum Sum Subarray (Kadane's) (Medium)
- Maximum Product Subarray (Medium)
- Longest Increasing Subsequence (Medium)
- Best Time to Buy and Sell Stock IV (Hard)
- Cherry Pickup (Hard)
- Constrained Subsequence Sum (Hard)

### Sorting
- Sort Colors (Dutch Flag) (Medium)
- Kth Largest Element (Medium)
- Merge Intervals (Medium)
- Insert Interval (Medium)
- Largest Number (Medium)
- Count of Smaller Numbers After Self (Hard)
- Reverse Pairs (Hard)

### Subarray Techniques
- Maximum Sum Subarray (Medium)
- Subarray Sum Equals K (Medium)
- Maximum Product Subarray (Medium)
- Maximum Sum Circular Subarray (Hard)
- Shortest Subarray with Sum at Least K (Hard)

### Advanced Techniques
- First Missing Positive (Array as Hashmap) (Hard)
- Trapping Rain Water II (Priority Queue) (Hard)
- Meeting Rooms III (Priority Queue) (Hard)

---

## 🎯 Preparation Tips

1. **Master the Patterns**: Focus on understanding each pattern deeply rather than memorizing solutions.
2. **Time-Space Trade-offs**: Practice optimizing from O(n²) to O(n log n) to O(n).
3. **Edge Cases**: Always consider empty arrays, single elements, duplicates, negative numbers, zeros.
4. **In-place Operations**: Many problems require O(1) space - master two-pointer and array manipulation tricks.
5. **Modulo Tricks**: Important for subarray problems (prefix sums, divisibility).
6. **Binary Search on Answer**: Recognize when the answer space is searchable.
7. **Monotonic Structures**: Deque and stack for range queries in sliding windows.
8. **State Tracking**: DP problems often track multiple states (used/not used, current position).

---

## 📚 Additional Resources

- **LeetCode**: Primary platform for these problems
- **Pattern Practice**: Group problems by pattern for focused practice
- **Time Complexity**: Aim for optimal solutions, understand alternatives
- **Space Optimization**: Practice reducing space complexity where possible

---

*Last Updated: 2024*

