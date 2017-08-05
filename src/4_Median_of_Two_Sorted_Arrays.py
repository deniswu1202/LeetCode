class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):  
        total_length= len(nums1)+len(nums2) 
        k = (total_length+1)/2

        if total_length%2 == 0:
            return (self.findK(nums1, nums2, k) + self.findK(nums1, nums2, k+1))/2.0
        else :
            return self.findK(nums1, nums2, k) 
            
    def findK(self, nums1, nums2, k):
        m, n = len(nums1), len(nums2)
        if m==0 or n==0:
            return nums2[k-1] if m==0 else nums1[k-1]
        if k == 1:
            return min(nums1[0],nums2[0])
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        pm = min(k/2, m)
        pn = k - pm

        if nums1[pm-1] == nums2[pn-1]:
            return nums1[pm-1]
        elif nums1[pm-1] < nums2[pn-1]:
            return self.findK(nums1[pm:], nums2, k-pm)
        else:
            return self.findK(nums1, nums2[pn:], k-pn)


a = Solution()   
print a.findMedianSortedArrays([1,2,3,4,5,6],[5,6,])
