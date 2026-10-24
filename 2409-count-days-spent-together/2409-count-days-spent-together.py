class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        from datetime import datetime

        def day(s):
            return datetime.strptime(s, "%m-%d").timetuple().tm_yday

        return max(0, min(day(leaveAlice), day(leaveBob)) -
                   max(day(arriveAlice), day(arriveBob)) + 1)
