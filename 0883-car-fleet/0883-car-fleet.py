class Solution(object):
    def carFleet(self, target, position, speed):
        if not position or len(position) == 1:
            return len(position)

        cars = sorted(zip(position, speed), reverse=True)  # Sort by position descending
        stack = []
        
        for pos, spd in cars:
            time = float(target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
                # Forms a new fleet → push time to stack
            # else → the car catches up → do nothing (merges into fleet)
                
        return len(stack)
