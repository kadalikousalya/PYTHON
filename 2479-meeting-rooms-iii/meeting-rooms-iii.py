class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        #time -mlogm+mlogN
        #O(n)
        meetings.sort()

        available=[i for i in range(n)] # 0 1 2 3 4
        
        used=[] #(end_time,room_number)
        count=[0]*n #count[n]=meetings schedule

        for start,end in meetings:
            #finish meetings
            while used and start>=used[0][0]:
                _,room=heapq.heappop(used)
                heapq.heappush(available,room)


            # no room is availbe
            if not available:
                end_time,room=heapq.heappop(used)
                end=end_time+(end-start)
                heapq.heappush(available,room)



            #room is availbe 
            room=heapq.heappop(available)
            heapq.heappush(used,(end,room))
            count[room]+=1


        return count.index(max(count))


        