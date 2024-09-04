from collections import defaultdict


class Solution(object):

    def turnRight(self, direction):
        if direction =='N':
           direction= 'E'
        elif direction =='S':
            direction = 'W'
        elif direction =='E':
            direction = 'S'
        elif direction =='W':
            direction = 'N'
        return direction
    def turnLeft(self, direction):
        if direction =='N':
           direction= 'W'
        elif direction =='S':
            direction = 'E'
        elif direction =='E':
            direction = 'N'
        elif direction =='W':
            direction = 'S'
        return direction
    def checkObstacle(self, init ,target, cords, positive):
        # print(f'Init: {init}, target: {target}, positive: {positive}')
        for i in cords:
            if positive and  init<i<=target:
                return i-1
            elif not positive and target<=i<init:
                return i+1
        return target

    def move(self,position, command, row_map, col_map, direction):
        # print(f'Before command {command} position is {position} direction is {direction}')
        if direction =='E':
            if position[1] in col_map:
                position[0] = self.checkObstacle(position[0], position[0]+command, col_map[position[1]], True)
            else:
                position[0]+=command
        elif direction =='W':
            if position[1] in col_map:
                position[0] = self.checkObstacle(position[0], position[0]-command, col_map[position[1]], False)
            else:
                position[0]-=command
        elif direction =='N':
            if position[0] in row_map:
                position[1] = self.checkObstacle(position[1], position[1]+command, row_map[position[0]], True)
            else:
                position[1]+=command
        else:
            if position[0] in row_map:
                position[1] = self.checkObstacle(position[1], position[1]-command, row_map[position[0]], False)
            else:
                position[1]-=command
        # print(f'After command {command} position is {position}')
        
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        direction = 'N'
        position = [0,0]
        obstacle_map_row=defaultdict(set)
        obatacle_map_col =defaultdict(set)
        max_dist = 0
        for row,col in obstacles:
            obstacle_map_row[row].add(col)
            obatacle_map_col[col].add(row)
        for command in commands:
            if command<0:
                if command==-1:
                    direction = self.turnRight(direction)
                else:
                    direction = self.turnLeft(direction)
                # print(f'After turn {command} direction is {direction}')
            else:
                self.move(position,command,obstacle_map_row,obatacle_map_col, direction)
                max_dist = max(max_dist,(position[0]**2)+(position[1]**2) )
        return max_dist
    
print(Solution().robotSim([4,-1,4,-2,4], [[2,4]]))