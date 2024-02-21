pub fn repeated_dnd_sequence(s: &str, k: i32) -> Vec<String> {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_repeated_dnd_sequence() {
        let s = "AGACCTAGAC";
        let result = repeated_dnd_sequence(s, 2);
        assert_eq!(result, vec!["AG", "AC"]);
    }
}
