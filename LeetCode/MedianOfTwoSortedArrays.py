

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        total_elements = len(nums1)+ len(nums2)
        midpoint = 0
        last_element=0
        element=0
        m1=0;m2=0
        while midpoint<=total_elements//2:
            midpoint+=1
            last_element = element

            if (m1==len(nums1)):
                element = nums2[m2]
                m2+=1
                continue
            if (m2==len(nums2)):
                element = nums1[m1]
                m1 += 1
                continue

            if nums1[m1]<nums2[m2]:
                element=nums1[m1]
                m1+=1
            else:
                element = nums2[m2]
                m2+=1

        if (total_elements%2==1):
            return (element)
        else:
            return (element+last_element)/2


s = Solution()
nums1 = [1,2]
nums2 = [3,4]
print(s.findMedianSortedArrays(nums1,nums2))