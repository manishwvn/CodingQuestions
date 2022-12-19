class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(nums, low, high):
            pivot = nums[high]
            i = low-1
            for j in range(low, high):
                if nums[j] > pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i+1], nums[high] = nums[high], nums[i+1]
            return i+1
    
        def quickSelect(nums, low, high, k):
            if low <= high:
                p = partition(nums, low, high)
                if p == k:
                    return nums[p]
                elif p < k:
                    return quickSelect(nums, p+1, high, k)
                else:
                    return quickSelect(nums, low, p-1, k)

        return quickSelect(nums, 0, len(nums)-1, k-1)
        