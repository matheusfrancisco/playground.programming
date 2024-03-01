use std::collections::{HashMap, HashSet};

pub fn repeated_dnd_sequence(s: &str, k: i32) -> HashSet<String> {
    if s.len() <= k as usize {
        return HashSet::new();
    }
    let base = 4;
    let hi_place_value = i32::pow(base, (k - 1) as u32);
    let mapping = HashMap::<String, i32>::from([
        ("A".to_string(), 0),
        ("C".to_string(), 1),
        ("G".to_string(), 2),
        ("T".to_string(), 3),
    ]);

    let numbers: Vec<i32> = s.chars().map(|c| mapping[&c.to_string()]).collect();

    let mut hash = 0;
    let mut substring_hashes = HashSet::<i32>::new();
    let mut output = HashSet::<String>::new();

    for start in 0..=(s.len() - k as usize) {
        if start != 0 {
            hash = (hash - numbers[start - 1] * hi_place_value) * base
                + numbers[start + k as usize - 1];
        } else {
            for end in 0..k {
                hash = hash * base + numbers[end as usize];
            }
        }
        if substring_hashes.contains(&hash) {
            let subsequence = s[start..start + k as usize].to_string();
            output.insert(subsequence);
        }
        substring_hashes.insert(hash);
    }

    output
    //
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_repeated_dnd_sequence() {
        let s = "AGACCTAGAC";
        let result = repeated_dnd_sequence(s, 2);
        assert_eq!(
            result,
            HashSet::from(["AG".to_string(), "GA".to_string(), "AC".to_string()])
        );
    }
    #[test]
    fn test_empty_string() {
        let result = repeated_dnd_sequence("", 3);
        assert!(result.is_empty()); // Assert an empty set for an empty input
    }

    #[test]
    fn test_no_repeats() {
        let result = repeated_dnd_sequence("ACGT", 2);
        assert!(result.is_empty());
    }

    #[test]
    fn test_single_repeat() {
        let result = repeated_dnd_sequence("ACGTACGT", 3);
        let mut expected = HashSet::new();
        expected.insert("CGT".to_string());
        expected.insert("ACG".to_string());
        assert_eq!(result, expected);
    }

    #[test]
    fn test_multiple_repeats() {
        let result = repeated_dnd_sequence("ACGTACGTTAACGG", 3);
        let mut expected = HashSet::new();
        expected.insert("ACG".to_string());
        expected.insert("CGT".to_string());
        assert_eq!(result, expected);
    }

    #[test]
    fn test_overlapping_repeats() {
        let result = repeated_dnd_sequence("AAAA", 2);
        let mut expected = HashSet::new();
        expected.insert("AA".to_string());
        assert_eq!(result, expected);
    }
}
