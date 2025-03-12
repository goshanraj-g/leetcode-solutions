class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        merged_intervals = [intervals[0]]
        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            last_merged_end = merged_intervals[-1][1]
            if current_start <= last_merged_end:
                merged_intervals[-1][1] = max(last_merged_end, current_end)
            else:
                merged_intervals.append([current_start, current_end])
        return merged_intervals
