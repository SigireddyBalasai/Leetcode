from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result = [0] * n  # Initialize result list with zeros for n flights
        
        for first, last, seats in bookings:
            result[first - 1] += seats  # Adjust for 0-based index in Python
            if last < n:  # Avoid index out of range error
                result[last] -= seats
        
        # Calculate cumulative sum to get the final counts
        for i in range(1, n):
            result[i] += result[i - 1]
        
        return result
