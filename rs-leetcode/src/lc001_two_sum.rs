pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut map = std::collections::HashMap::<i32, i32>::new();

    for (i, v) in nums.iter().enumerate() {
        let r = target - v;
        match map.get(&r) {
            Some(&j) => return vec![j, i as i32],
            _ => map.insert(*v, i as i32),
        };
    }
    vec![]
}

#[cfg(test)]
mod test {
    use super::*;
    #[test]
    fn test_two_sum() {
        let nums = vec![2, 11, 15, 7];
        let target = 9;
        let result = two_sum(nums, target);
        assert_eq!(result, vec![0, 3]);
    }
}
