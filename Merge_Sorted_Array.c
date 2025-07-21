void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int i = m - 1;         // Last index of elements in nums1
    int j = n - 1;         // Last index of elements in nums2
    int k = m + n - 1;     // Last index of merged array in nums1

    // Merge in reverse order
    while (i >= 0 && j >= 0) {
        if (nums1[i] > nums2[j]) {
            nums1[k--] = nums1[i--];
        } else {
            nums1[k--] = nums2[j--];
        }
    }

    // Copy any remaining elements of nums2 (if any)
    while (j >= 0) {
        nums1[k--] = nums2[j--];
    }

    // No need to copy remaining nums1 elements; they are already in place
}
