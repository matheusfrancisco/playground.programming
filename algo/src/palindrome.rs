fn is_palindrome(s: String) -> bool {
    let mut l = 0;
    let mut r = s.len() - 1;
    let b = s.as_bytes();

    while l < r {
        let left_char = b[l];
        let right_char = b[r];

        if !left_char.is_ascii_alphanumeric() {
            l += 1;
            continue;
        }

        if !right_char.is_ascii_alphanumeric() {
            r -= 1;
            continue;
        }

        if left_char.to_ascii_lowercase() != right_char.to_ascii_lowercase() {
            return false;
        }

        l += 1;
        r -= 1;
    }

    true
}

fn is_palindrome2(s: String) -> bool {
    let filtered: String = s
        .chars()
        .filter(|c| c.is_ascii_alphanumeric())
        .map(|c| c.to_ascii_lowercase())
        .collect();

    filtered == filtered.chars().rev().collect::<String>()
}

fn is_palindrome3(s: String) -> bool {
    let filtered: Vec<char> = s
        .chars()
        .filter(|c| c.is_ascii_alphanumeric())
        .map(|c| c.to_ascii_lowercase())
        .collect();

    let mut l = 0;
    let mut r = filtered.len() - 1;

    while l < r {
        if filtered[l] != filtered[r] {
            return false;
        }
        l += 1;
        r -= 1;
    }

    true
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_palindrome() {
        assert_eq!(is_palindrome("do geese see god".to_string()), true);
        assert_eq!(
            is_palindrome("was it a car or a cat I saw".to_string()),
            true
        );
        assert_eq!(is_palindrome("not a palindrome".to_string()), false);
    }
}
