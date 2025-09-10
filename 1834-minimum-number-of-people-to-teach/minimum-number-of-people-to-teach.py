class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        problemtic=set()
        for u,v in friendships:
            if not (set(languages[u-1]) & set(languages[v-1])):
                problemtic.add(u)
                problemtic.add(v)
        if not problemtic:
            return 0
        min_teach = float('inf')
        for l in range(1,n+1):
            teach_count=0
            for user in problemtic:
                if l not in languages[user-1]:
                    teach_count+=1
            min_teach=min(min_teach,teach_count)
        return min_teach
            

