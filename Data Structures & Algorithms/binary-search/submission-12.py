class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)-1
        bounds = [0,l]
        for n in range((l//2)+2):
            mid = (bounds[0] + bounds[1]) // 2
            if nums[mid] <= target:
                bounds[0] = mid +1
                if nums[mid] == target:
                    return mid
                mid -=1
            else:
                bounds[1] = mid
                
        return -1
            
            
                
