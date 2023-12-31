# -*- coding: utf-8 -*-
"""Longest_Subsequence_Common.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a6NxIWKDa_dhI3ZbMRHR0DX5lh8WpwWF
"""

"""
A subsequence is a sequence that can be derived from another
sequence by deleting some or no elements without changing the
order of the remaining elements.

For example, 'abd' is a subsequence of 'abcd' whereas 'adc' is not

Given 2 strings containing lowercase english alphabets, find the length
of the Longest Common Subsequence (L.C.S.).

Example:
    Input:  'abcdgh'
            'aedfhr'
    Output: 3

    Explanation: The longest subsequence common to both the string is "adh"

Time Complexity : O(M*N)
Space Complexity : O(M*N), where M and N are the lengths of the 1st and 2nd string
respectively.

"""


def longest_common_subsequence(s1, s2):
    """
    :param s1: string
    :param s2: string
    :return: int
    """
    m, n = len(s1), len(s2)

    dp = [[0] * (n + 1)] * (m + 1)
    """
    dp[i][j] : contains length of LCS of s1[0..i-1] and s2[0..j-1]
    """

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]