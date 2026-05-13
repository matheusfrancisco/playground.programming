use std::collections::VecDeque;

fn main() {
    println!("Hello, world!");
}

struct Interpreter<'a> {
    stack: VecDeque<i32>,
    index: usize,
    ops: &'a [&'a str],
}

impl<'a> Interpreter<'a> {
    fn next_op(&mut self) -> Option<String> {
        if self.index < self.ops.len() {
            let op = self.ops[self.index];
            self.index += 1;
            return Some(op.to_owned());
        }
        None
    }

    fn execute_op(&mut self, op: &str) -> Option<bool> {
        match op {
            "OP_ADD" => {
                let Some(b) = self.stack.pop_back() else {
                    return Some(false);
                };
                let Some(a) = self.stack.pop_back() else {
                    return Some(false);
                };
                self.stack.push_back(a + b);
            }
            "OP_EQUAL" => {
                let Some(b) = self.stack.pop_back() else {
                    return Some(false);
                };
                let Some(a) = self.stack.pop_back() else {
                    return Some(false);
                };
                self.stack.push_back(if a == b { 1 } else { 0 });
            }
            "OP_SUB" => {
                let Some(b) = self.stack.pop_back() else {
                    return Some(false);
                };
                let Some(a) = self.stack.pop_back() else {
                    return Some(false);
                };
                self.stack.push_back(a - b);
            }
            "OP_VERIFY" => {
                if let Some(element) = self.stack.pop_back() {
                    if element == 0 {
                        return Some(false);
                    }
                }
            }
            "OP_IF" => {
                if self
                    .stack
                    .pop_back()
                    .map(|element| element > 0)
                    .unwrap_or(false)
                {
                    while let Some(op) = self.next_op() {
                        if op == "OP_ELSE" {
                            break;
                        }
                        if let Some(result) = self.execute_op(&op) {
                            return Some(result);
                        }
                    }

                    while let Some(op) = self.next_op() {
                        if op == "OP_ENDIF" {
                            break;
                        }
                    }
                } else {
                    while let Some(op) = self.next_op() {
                        if op == "OP_ELSE" {
                            break;
                        }
                    }

                    while let Some(op) = self.next_op() {
                        if op == "OP_ENDIF" {
                            break;
                        }
                        if let Some(result) = self.execute_op(&op) {
                            return Some(result);
                        }
                    }
                }
            }
            n => {
                let part = &n[3..];
                self.stack.push_back(part.parse::<i32>().unwrap());
            }
        }

        None
    }
}

fn execute(ops: &[&str]) -> bool {
    let mut interpreter = Interpreter {
        stack: VecDeque::new(),
        index: 0,
        ops,
    };
    while let Some(op) = interpreter.next_op() {
        if let Some(result) = interpreter.execute_op(&op) {
            return result;
        }
    }
    interpreter
        .stack
        .pop_back()
        .map(|entry| entry > 0)
        .unwrap_or(false)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn examples() {
        let cases = [
            (vec!["OP_1", "OP_2", "OP_ADD"], true),
            (vec!["OP_1", "OP_1", "OP_ADD", "OP_3", "OP_EQUAL"], false),
            (vec!["OP_3", "OP_2", "OP_SUB", "OP_1", "OP_EQUAL"], true),
            (
                vec![
                    "OP_3", "OP_2", "OP_SUB", "OP_5", "OP_ADD", "OP_5", "OP_EQUAL",
                ],
                false,
            ),
            (vec!["OP_ADD"], false),
            (vec!["OP_1", "OP_2"], true),
            (vec!["OP_0", "OP_VERIFY", "OP_1"], false),
            (vec!["OP_1", "OP_VERIFY", "OP_2"], true),
            (
                vec![
                    "OP_1", "OP_2", "OP_EQUAL", "OP_IF", "OP_0", "OP_ELSE", "OP_1", "OP_ENDIF",
                ],
                true,
            ),
            (
                vec![
                    "OP_1", "OP_1", "OP_EQUAL", "OP_IF", "OP_0", "OP_ELSE", "OP_1", "OP_ENDIF",
                ],
                false,
            ),
        ];
        for (program, expected) in cases {
            let actual = execute(&program);
            dbg!(&actual);
            assert_eq!(expected, actual);
        }
    }
}
