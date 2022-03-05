# class Solution:
#     def restoreString(self, s: str, indices: List[int]) -> str:
#         dic={}
#         for i in range(len(indices)):
#             dic[str(indices[i])]=s[i]
        
#         indices.sort()
#         ans=""
#         for i in range(len(indices)):
#             ans+=dic[str(i)]
#         return ans
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = [""]*len(s)
        s = list(s)
        
        for i in range(len(indices)):
            arr[indices[i]] = s[i]
            
        return "".join(arr)
