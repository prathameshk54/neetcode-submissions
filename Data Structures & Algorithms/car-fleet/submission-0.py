class Solution:
    def canMeet(self, c1, c2, target):
        if c1['speed'] <= c2['speed']:
            return False
        time_to_meet = float(c2['pos'] - c1['pos']) / float(c1['speed'] - c2['speed'])
        time_to_end = float(target - c2['pos']) / float(c2['speed'])
        if time_to_meet <= time_to_end:
            return True
        else:
            return False

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [{'pos':position[i], 'speed':speed[i]} for i in range(n)]
        cars = sorted(cars, key = lambda d : d['pos'])

        fleets = []
        for car in cars:
            while len(fleets) and self.canMeet(fleets[-1], car, target):
                fleets.pop()
            fleets.append(car)

        return len(fleets)
        