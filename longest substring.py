#!/usr/bin/env python
# coding: utf-8

# In[6]:


"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given a string, find the length of the longest substring without repeating characters.

Can you find a solution in linear time?
"""

class Solution:
  def lengthOfLongestSubstring(self, s):
    if len(s) == 0:
        return 0
    sub = ""
    max_ = 0
    temp = 0
    for a in s:
        if sub.find(a) == -1:
            sub += a
            temp += 1
        else:
            if temp > max_:
                max_ = temp
            temp = 1
            sub = "" + a
    return max_
            
            
        

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
print(Solution().lengthOfLongestSubstring('szymonmrozowski'))
print(Solution().lengthOfLongestSubstring('kkkalbinosmrukvyqp'))
# 10


# In[ ]:




