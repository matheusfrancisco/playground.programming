fn max_subarray_sum_fixed(arr: &[i32], k: i32) -> i32 {

    let mut sum = 0;
    let mut max_sum = 0;
    for r in 0..arr.len() {
        sum += arr[r];
        if r >= k as usize - 1 {
            max_sum = max_sum.max(sum);
            sum -= arr[r - (k as usize - 1)];
        }
    }
    max_sum
    
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_max_subarray_fixed_sum() {
        let arr = [2, 1, 5, 1, 3, 2];
        let k = 3;
        assert_eq!(max_subarray_sum_fixed(&arr, k), 9);
    }
}
