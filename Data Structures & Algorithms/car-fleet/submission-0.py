class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        carstack = []

        # Car starting distance + speed tuples sorted in descending order 
        # (closest cars to target to furthest)
        cars.sort(key = lambda tup: tup[0], reverse=True)

        for pos,spd in cars:
            timeToTarget = (target-pos) / spd
            if not carstack:
                carstack.append(timeToTarget)
            elif carstack[-1] < timeToTarget:
                carstack.append(timeToTarget)
            # if carstack and carstack[-1] >= timeToTarget:
            #     # do nothing?
            # else:
            #     # add to stack as a fleet
            #     carstack.append(timeToTarget)

        return len(carstack)