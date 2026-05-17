use std::error;
use std::fmt::Display;
use std::io;
use std::str::FromStr;

type List<T> = Option<Box<Node<T>>>;

#[derive(Clone)]
pub struct Node<T> {
    pub val: T,
    pub next: List<T>,
}

fn remove_nth_from_end_2(head: Option<Box<Node<i32>>>, n: i32) -> Option<Box<Node<i32>>> {
    fn helper(node: List<i32>, n: i32) -> (List<i32>, i32) {
        match node {
            None => (None, 0),
            Some(mut boxed) => {
                let (rest, count_from_end) = helper(boxed.next.take(), n);
                let this_index = count_from_end + 1;
                if this_index == n {
                    (rest, this_index)
                } else {
                    boxed.next = rest;
                    (Some(boxed), this_index)
                }
            }
        }
    }

    helper(head, n).0
}

pub fn remove_nth_from_end(head: Option<Box<Node<i32>>>, n: i32) -> Option<Box<Node<i32>>> {
    let mut len = 0;

    {
        let mut current = &head;
        while let Some(node) = current {
            len += 1;
            current = &node.next;
        }
    }

    let mut dummy = Box::new(Node { val: 0, next: head });
    let target = len - n;

    let mut curr = &mut dummy;
    for _ in 0..target {
        curr = curr.next.as_mut().unwrap();
    }

    let next = curr.next.take();
    if let Some(mut node) = next {
        curr.next = node.next.take();
    }

    dummy.next
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

fn format_list<T: Display>(node: &List<T>, out: &mut Vec<String>) {
    if let Some(node) = node {
        out.push(format!("{}", node.val));
        format_list(&node.next, out);
    }
}

fn print_words<T: Display>(v: &Vec<T>) {
    let mut iter = v.iter();
    if let Some(val) = iter.next() {
        print!("{}", val);
        for val in iter {
            print!(" {}", val);
        }
    }
    println!();
}

#[cfg(test)]
mod tests {

    #[test]
    fn test_remove_nth_from_end() {
        let input = "1 2 3 4 5";
        let list = super::build_list(&mut input.split_whitespace()).unwrap();
        let result = super::remove_nth_from_end(list, 2);
        let mut out = Vec::new();
        super::format_list(&result, &mut out);
        super::print_words(&out);
    }
}
