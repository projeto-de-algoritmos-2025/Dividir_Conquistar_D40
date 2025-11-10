class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        #garantir que nums1 seja menor
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
            
        total_length = m + n

        half_len = (total_length + 1) // 2 #dividir em duas metadades iguais
      
        low = 0
        high = m
        
        while low <= high:
            i = (low + high) // 2
            j = half_len - i
            
            max_left_1 = nums1[i - 1] if i > 0 else float('-inf')
            min_right_1 = nums1[i] if i < m else float('inf')
            
            max_left_2 = nums2[j - 1] if j > 0 else float('-inf')
            min_right_2 = nums2[j] if j < n else float('inf')

            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:

                max_of_left = max(max_left_1, max_left_2)
                
                if total_length % 2 == 1:

                    return max_of_left
                else:
                    min_of_right = min(min_right_1, min_right_2)
                    return (max_of_left + min_of_right) / 2.0
            
            elif max_left_1 > min_right_2:
                high = i - 1
            else: 
                low = i + 1
