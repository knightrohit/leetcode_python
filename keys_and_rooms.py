"""
Input: [[1],[2],[3],[]]
Output: true

Input: [[1,3],[3,0,1],[2],[0]]
Output: false

Time complexity = O(K), here K is the total number of keys
Space complexity = O(N)
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        if not rooms:
            return False
        
        if len(rooms) == 1:
            return True
        
        visited = [False]*len(rooms)
        visited[0] = True
        x = len(rooms)
        indx = 0
        
        def visit(indx):
            if visited[indx]:
                for key in rooms[indx]:
                    if not visited[key]: 
                        visited[key] = True
                        visit(key)                    
        visit(indx)
        return all(visited)