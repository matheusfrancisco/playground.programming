use std::collections::HashMap;

pub struct Solution {}

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut map: HashMap<[u16; 26], Vec<String>> = HashMap::new();

        for s in &strs {
            let mut count = [0u16; 26];

            for c in s.bytes() {
                count[(c - b'a') as usize] += 1;
            }

            map.entry(count).or_default().push(s.clone());
        }

        map.into_values().collect()
    }
}

fn normalize(mut groups: Vec<Vec<String>>) -> Vec<Vec<String>> {
    for group in &mut groups {
        group.sort();
    }
    groups.sort();
    groups
}

fn find_anagram(s: String, p: String) -> Vec<i32> {
    if p.len() > s.len() {
        return vec![];
    }
    let k = p.len();
    let mut p_count = 0;
    for c in p.chars() {
        p_count += 1 << (c as u8 - b'a');
    }
    let mut s_count = 0;
    let mut indexes = vec![];

    for i in 0..s.len() {
        s_count += 1 << (s.as_bytes()[i] - b'a');
        if i >= k {
            s_count -= 1 << (s.as_bytes()[i - k] - b'a');
        }
        if s_count == p_count {
            indexes.push((i + 1 - k) as i32);
        }
    }
    indexes
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_group_anagrams() {
        let strs = vec![
            "eat".to_string(),
            "tea".to_string(),
            "tan".to_string(),
            "ate".to_string(),
            "nat".to_string(),
            "bat".to_string(),
        ];

        let result = Solution::group_anagrams(strs);
        assert_eq!(
            normalize(result),
            normalize(vec![
                vec!["bat".to_string()],
                vec!["tan".to_string(), "nat".to_string()],
                vec!["eat".to_string(), "tea".to_string(), "ate".to_string()],
            ])
        );
    }

    #[test]
    fn test_find_anagram() {
        let s = "cbaebabacd".to_string();
        let p = "abc".to_string();

        assert_eq!(find_anagram(s, p), vec![0, 6]);
    }
}
