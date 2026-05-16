// Find Peak Element
// https://leetcode.com/problems/find-peak-element/description/
// A peak element is an element that is strictly greater than its neighbors.
// Given an integer array nums, find a peak element, and return its index. If
// the array contains multiple peaks, return the index to any of the peaks.
// You may imagine that nums[-1] = nums[n] = -∞.
//
//Setup: lo = 0, hi = 4 (len - 1)
//
//Iter 1:
//  lo=0, hi=4, mid = 0 + (4-0)/2 = 2
//  arr[mid]=3, arr[mid+1]=2
//  3 < 2? No → hi = mid = 2
//  Window now [0, 2]
//
//Iter 2:
//  lo=0, hi=2, mid = 0 + (2-0)/2 = 1
//  arr[mid]=9, arr[mid+1]=3
//  9 < 3? No → hi = mid = 1
//  Window now [0, 1]
//
//Iter 3:
//  lo=0, hi=1, mid = 0 + (1-0)/2 = 0
//  arr[mid]=5, arr[mid+1]=9
//  5 < 9? Yes → lo = mid + 1 = 1
//  Window now [1, 1]
//
//Loop exits (lo == hi). Return 1. 
//

fn find_peak_element(nums: Vec<i32>) -> i32 {
    let mut lo = 0;
    let mut hi = nums.len() - 1;

    while lo < hi {
        let mid = lo + (hi - lo) / 2;
        if nums[mid] < nums[mid + 1] {
            lo = mid + 1; // Move right
        } else {
            hi = mid; // Move left
        }
    }

    lo as i32 // Return the index of the peak element
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_find_peak_element() {
        let nums = vec![1, 2, 3, 1];
        assert_eq!(find_peak_element(nums), 2);

        let nums = vec![1, 2, 1, 3, 5, 6, 4];
        let result = find_peak_element(nums);
        assert!(result == 1 || result == 5); // Both indices are valid peaks
    }

}
