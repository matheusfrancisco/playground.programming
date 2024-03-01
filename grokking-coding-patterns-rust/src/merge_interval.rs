pub fn merge_overlapping_intervals(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
    let mut out = vec![];
    let mut interval_merged: Vec<i32> = intervals[0].clone();

    for interval in intervals.iter().skip(1) {
        if interval[0] <= interval_merged[1] {
            interval_merged[1] = interval_merged[1].max(interval[1]);
        } else {
            out.push(interval_merged.clone());
            interval_merged = interval.clone();
        }
    }

    out.push(interval_merged.clone());

    out
}

#[cfg(test)]
mod test {
    use super::*;
    #[test]
    fn test_merge_overlapping_intervals() {
        let intervals = vec![vec![1, 4], vec![3, 6], vec![7, 9]];
        let result = merge_overlapping_intervals(intervals);
        assert_eq!(result, vec![vec![1, 6], vec![7, 9]]);
    }
}
