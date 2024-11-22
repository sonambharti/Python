'''
# 2456. Most Popular Video Creator

You are given two string arrays creators and ids, and an integer array views, all of length n. 
The ith video on a platform was created by creators[i], has an id of ids[i], and has views[i] views.

The popularity of a creator is the sum of the number of views on all of the creator's videos. 
Find the creator with the highest popularity and the id of their most viewed video.

If multiple creators have the highest popularity, find all of them.
If multiple videos have the highest view count for a creator, find the lexicographically smallest id.
Note: It is possible for different videos to have the same id, meaning that ids do not uniquely 
identify a video. For example, two videos with the same ID are considered as distinct videos with 
their own viewcount.

Return a 2D array of strings answer where answer[i] = [creatorsi, idi] means that creatorsi has the 
highest popularity and idi is the id of their most popular video. The answer can be returned in any order.

 

Example 1:

Input: creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4]

Output: [["alice","one"],["bob","two"]]

Explanation:

The popularity of alice is 5 + 5 = 10.
The popularity of bob is 10.
The popularity of chris is 4.
alice and bob are the most popular creators.
For bob, the video with the highest view count is "two".
For alice, the videos with the highest view count are "one" and "three". Since "one"
is lexicographically smaller than "three", it is included in the answer.

Example 2:

Input: creators = ["alice","alice","alice"], ids = ["a","b","c"], views = [1,2,2]

Output: [["alice","b"]]

Explanation:

The videos with id "b" and "c" have the highest view count.
Since "b" is lexicographically smaller than "c", it is included in the answer.


'''


import heapq
import math

def mostPopularCreator(creators, ids, views):
    d = {}
    n = len(creators)
    max_v = 0
    for i in range(n):
        if creators[i] not in d:
            d[creators[i]] = [views[i], ids[i], views[i]]
        else:
            d[creators[i]][0] += views[i]
            if views[i] > d[creators[i]][2]:
                d[creators[i]][2] = views[i]
                d[creators[i]][1] = ids[i]
            elif views[i] == d[creators[i]][2]:
                d[creators[i]][1] = min(d[creators[i]][1], ids[i])

        if d[creators[i]][0] > max_v:
            max_v = d[creators[i]][0]
    
    ans = []
    for c in d:
        if d[c][0] == max_v:
            ans.append([c, d[c][1]])
    return ans
            
            
            

def mostPopularCreator_heap(creators, ids, views):
    mapped_data = {}
    highest_popularity = 0
    for creator, id, view in zip(creators, ids, views):
        if not creator in mapped_data:
            mapped_data[creator] = [view, id, view]
        else:
            prev = mapped_data[creator]
            prev[0] += view
            if (prev[2] == view and prev[1] > id) or (prev[2] < view):
                prev[1] = id
            if prev[2] < view:
                prev[2] = view
        highest_popularity = max(highest_popularity, mapped_data[creator][0])
    
    result = []
    for creator, [view, id, id_value] in mapped_data.items():
        if view == highest_popularity:
            result.append([creator, id])
    return result
    
    
    
if __name__ == "__main__":
    creators = ["alice","alice","alice"]
    ids = ["a","b","c"]
    views = [1,2,2]
    # res = mostPopularCreator(creators, ids, views)
    # print("The highest popularity and idi is the id of their most popular video is: ", res)
    
    res = mostPopularCreator_heap(creators, ids, views)
    print("The highest popularity and idi is the id of their most popular video is: ", res)
    
    
