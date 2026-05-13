// sorted array of unique integers was rotated at an unknown pivot index,
// [10, 20, 30, 40, 50] was rotated [30, 40, 50, 10, 20]
// find the index of the minimum element in this array
//
//
// if I can look in the middle to understand which half to throw away, I can use
// the binary search.
//
//
// [30, 40, 50, 10, 20]
//  l               r
// which side should I go
// mid =  l + (r - l) / 2 = 0 + (4 - 0) / 2 = 2
// mid = 2 , mid_value = 50
// 50 > 20, so the minimum is in the right half, I can throw away the left half
// [10, 20]
// l   r
// mid = 0 + (1 - 0) / 2 = 0
// mid_value = 10
// 10 < 20, so the minimum is in the left half, I can throw
// away the right half
// [10]
// l r
// l = r, so the minimum is at index 0, which is 10
//
//[3, 5, 7, 11, 13, 17, 19, 2]
//l         m                r
//mid = 0 + (7 - 0) / 2 = 3
//
// 11> 2, so the minimum is in the right half, I can throw away the left half
// [13, 17, 19, 2]
// l            r
// mid = 0 + (3 - 0) / 2 = 1
// mid_value = 17
// 17 > 2, so the minimum is in the right half, I can throw
// away the left half
// [19, 2]
// l   r
// mid = 0 + (1 - 0) / 2 = 0
// mid_value = 19
// 19 > 2, so the minimum is in the right half, I can throw
// away the left half
// [2]
// l r
//
//When a sorted structure has one break point, you can often binary-search for the break itself.
//This shows up in "find peak element," "search in rotated array," "find rotation count," and more.
//

fn find_min(mut nums: Vec<i32>) -> i32 {
    if nums.is_empty() {
        return -1; // or handle as needed
    }
    let mut r = nums.len() - 1;
    let mut l = 0;

    while l < r {
        let mid = l + (r - l) / 2;
        if nums[mid] > nums[r] {
            l = mid + 1;
        } else {
            r = mid;
        }
    }

    nums[l]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_find_min() {
        assert_eq!(find_min(vec![10, 20, 30]), 10);
        assert_eq!(find_min(vec![30, 40, 50, 10, 20]), 10);
        assert_eq!(find_min(vec![3, 5, 7, 11, 13, 17, 19, 2]), 2);
    }
}


// Where these patterns show up next
//Search in rotated sorted array same setup, but you're finding a target value, with the rotation complicating things
//find peak element broken monotonicity again "peak" is a position defined by a condition
//first bad version first true a bolean 
// Median of two sorted arrays Flavor B with a more involved decision rule

