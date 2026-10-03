class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Stack holds fleets
        # Bottom of stack = fleets that arrived at the target first
        carstack = []

        # Car starting distance + speed tuples sorted in descending order 
        # (closest cars to target to furthest)
        cars = list(zip(position, speed))
        cars.sort(key = lambda tup: tup[0], reverse=True)

        # Calculate the fastest a car could make it to the target
        # Then check the stack if the fleet in front of it (if it exists)
        # arrives at the target slower or at the same time. If not, it is a
        # new fleet and should be added to the stack of fleets
        for pos,spd in cars:
            timeToTarget = (target-pos) / spd
            # if not carstack:
            #     carstack.append(timeToTarget)
            # elif carstack[-1] < timeToTarget:
            #     carstack.append(timeToTarget)
            if carstack and carstack[-1] >= timeToTarget:
                # do nothing?
                continue
            else:
                # add to stack as a fleet
                carstack.append(timeToTarget)

        return len(carstack)