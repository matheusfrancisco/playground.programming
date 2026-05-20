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
            indexes.push((i - k + 1) as i32);
        }
    }
    indexes
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_find_anagram() {
        let s = "cbaebabacd".to_string();
        let p = "abc".to_string();

        assert_eq!(find_anagram(s, p), vec![0, 6]);
    }
}
