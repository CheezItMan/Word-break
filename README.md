# Word Break

Given a string `s` and a dictionary of strings `word_dict`, return `True` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

## Example 1:

**Input:** `s = "leetcode"`, `word_dict = ["leet", "code"]`

**Output:** `True`

**Explanation:**

We return `True` because "leetcode" can be segmented as "leet code".



## Example 2:

**Input:** `s = "applepenapple"`, `word_dict = ["apple", "pen"]`

**Output:** `True`

**Explanation:**

We return `True` because "applepenapple" can be segmented as "apple pen apple".  Note that "apple" can be used twice.

## Example 3:

**Input:** `s = "catsandog"`, `word_dict = ["cats", "dog", "sand", "and", "cat"]``

**Output:** `False`

**Explanation:**

We return `False` because "catsandog" _cannot_ be segmented with the words provided in the dictionary without overlap.


## Why Use A Priority Queue?

**Question:** Why does your team thing a priority queue is appropriate here?

*This exercise was taken from: [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)*
