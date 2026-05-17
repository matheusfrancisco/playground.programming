// two pointers invariants
// invariants must stay true as the loop runs

//The algorithm is allowed to change values, move pointers, and update state,
//but this statement must be true again when the loop is ready for the next iteration.
// If you cannot state the invariant, there is a good chance you are following a pattern mechanically
// rather than understanding why it works.
//
//type of problems
//same direction pointers
// one pointers reads the next value from the original input
// one pointer marks where the next kept valur should go
// sometimes both move together
//Reach for same-direction pointers when the problem asks you to:
//rewrite an array in-place
//remove or compress elements without extra memory
//keep only the values that satisfy some condition
//maintain a fixed gap between two forward-moving pointers
//

use std::{error, str::FromStr};

type List<T> = Option<Box<Node<T>>>;

#[derive(Clone)]
pub struct Node<T> {
    pub val: T,
    pub next: List<T>,
}

fn middle_of_linked_list(head: List<i32>) -> i32 {
    let mut slow = head.as_deref(); // &head
    let mut fast = head.as_deref(); // &head

    while let Some(next_fast) = fast.and_then(|n| n.next.as_deref()) {
        slow = slow.and_then(|n| n.next.as_deref());
        fast = next_fast.next.as_deref();
    }
    slow.map_or(0, |n| n.val)
}

fn build_list<'a, T, I>(iter: &mut I) -> Result<List<T>, Box<dyn error::Error>>
where
    T: FromStr,
    I: Iterator<Item = &'a str>,
    <T as FromStr>::Err: 'static + error::Error,
{
    let val = match iter.next() {
        Some(val) => val.parse()?,
        None => return Ok(None),
    };
    let next = build_list(iter)?;
    Ok(Some(Box::new(Node { val, next })))
}

// new lenght
fn remove_duplicate(arr: &mut Vec<i32>) -> usize {
    if arr.is_empty() {
        return 0 as usize;
    }
    let mut slow = 0;
    for fast in 1..arr.len() {
        if arr[slow] != arr[fast] {
            arr[slow + 1] = arr[fast];
            slow += 1;
        }
    }
    slow + 1
}

#[cfg(test)]
mod tests {
    #[test]
    fn test_middle_of_linked_list() {
        let input = "1 2 3 4 5";
        let list = super::build_list(&mut input.split_whitespace()).unwrap();
        assert_eq!(super::middle_of_linked_list(list), 3);

        let input = "1 2 3 4 5 6";
        let list = super::build_list(&mut input.split_whitespace()).unwrap();
        assert_eq!(super::middle_of_linked_list(list), 4);

        let input = "1 2 3 4 5 6 7 8";
        let list = super::build_list(&mut input.split_whitespace()).unwrap();
        assert_eq!(super::middle_of_linked_list(list), 5);

        //edge case
        let input = "1";
        let list = super::build_list(&mut input.split_whitespace()).unwrap();
        assert_eq!(super::middle_of_linked_list(list), 1);

        let input = "";
        let list = super::build_list(&mut input.split_whitespace()).unwrap();
        assert_eq!(super::middle_of_linked_list(list), 0);
    }

    #[test]
    fn test_remove_duplicate() {
        let mut arr = vec![0, 0, 1, 1, 1, 2, 2, 3, 3, 4];
        let expected = vec![0, 1, 2, 3, 4];
        let new_length = super::remove_duplicate(&mut arr);
        assert_eq!(new_length, expected.len());

        let mut arr = vec![1, 1, 2];
        let expected = vec![1, 2];
        let new_length = super::remove_duplicate(&mut arr);
        assert_eq!(new_length, expected.len());

        //edge case
        let mut arr = vec![1];
        let expected = vec![1];
        let new_length = super::remove_duplicate(&mut arr);
        assert_eq!(new_length, expected.len());

        let mut arr = vec![];
        let expected: Vec<i32> = vec![];
        let new_length = super::remove_duplicate(&mut arr);
        assert_eq!(new_length, expected.len());
    }
}
