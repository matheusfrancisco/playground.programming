fn my_sqrt(n: i32) -> i32 {
    if n < 2 {
        return n;
    }

    let mut left = 1;
    let mut right = n / 2;

    while left <= right {
        let mid = left + (right - left) / 2;
        let mid_squared = mid * mid;

        if mid_squared == n {
            return mid;
        } else if mid_squared < n {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    right
}

#[cfg(test)]
mod tests {

    #[test]
    fn test_sqrt() {
        assert_eq!(super::my_sqrt(9), 3);
        assert_eq!(super::my_sqrt(4), 2);
        assert_eq!(super::my_sqrt(16), 4);
        assert_eq!(super::my_sqrt(8), 2);
    }
}
