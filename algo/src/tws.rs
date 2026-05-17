// the solution should have O(1) space complexity and O(n) time complexity
fn two_sum_sorted(arr: Vec<i32>, target: i32) -> Vec<i32> {
    if arr.len() < 2 {
        return vec![];
    }

    let mut left = 0;
    let mut right = arr.len() - 1;

    while left < right {
        let s = arr[left] + arr[right];
        if s == target {
            return vec![left as i32, right as i32];
        } else if s < target {
            left += 1;
        } else {
            right -= 1;
        }
    }
    vec![]
}

#[cfg(test)]
mod tests {

    #[test]
    fn test_two_sum_sorted() {
        let arr = vec![1, 2, 3, 4, 6];
        let target = 6;
        let expected = vec![1, 3];
        assert_eq!(super::two_sum_sorted(arr, target), expected);

        let arr = vec![2, 5, 9, 11];
        let target = 11;
        let expected = vec![0, 2];
        assert_eq!(super::two_sum_sorted(arr, target), expected);

        //edge case
        let arr = vec![1];
        let target = 1;
        let expected: Vec<i32> = vec![];
        assert_eq!(super::two_sum_sorted(arr, target), expected);

        let arr = vec![];
        let target = 0;
        let expected: Vec<i32> = vec![];
        assert_eq!(super::two_sum_sorted(arr, target), expected);
    }
}
