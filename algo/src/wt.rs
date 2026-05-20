fn container_with_most_water(height: Vec<i32>) -> i32 {
    let mut l = 0;
    let mut r = height.len() - 1;
    let mut max_area = 0;

    while l < r {
        let width = (r - l) as i32;
        let area = width * height[l].min(height[r]);
        max_area = max_area.max(area);

        if height[l] < height[r] {
            l += 1;
        } else {
            r -= 1;
        }
    }

    max_area
}

#[cfg(test)]
mod tests {

    #[test]
    fn test_container_with_most_water() {
        use super::*;

        assert_eq!(
            container_with_most_water(vec![1, 8, 6, 2, 5, 4, 8, 3, 7]),
            49
        );
        assert_eq!(container_with_most_water(vec![1, 1]), 1);
    }
}
