
//! Given a binary tree, return its level order traversal: a list of lists of
//! integers, where the i-th list contains the values of the nodes on level i,
//! from left to right.
//!
//! Example (study page tree):
//!         1
//!        / \
//!       2   3
//!      / \
//!     4   5
//! Output: [[1], [2, 3], [4, 5]].
//!
//! API: returns a `Vec<Vec<i32>>` — one inner Vec per level, owned by the
//! outer Vec.
//!

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Box<TreeNode>>,
    pub right: Option<Box<TreeNode>>,
}

impl TreeNode {
    pub fn leaf(val: i32) -> Box<TreeNode> {
        Box::new(TreeNode {
            val,
            left: None,
            right: None,
        })
    }
}

/// Return one `Vec<i32>` per level, top to bottom, left to right.
/// Empty tree → empty outer Vec.
pub fn level_order(root: Option<&TreeNode>) -> Vec<Vec<i32>> {
    let mut levels: Vec<Vec<i32>> = vec![];
    let mut queue: Vec<Option<&TreeNode>> = vec![root];

    while !queue.is_empty() {
        let mut next_queue: Vec<Option<&TreeNode>> = vec![];
        let mut current_level: Vec<i32> = vec![];

        for node in queue {
            if let Some(n) = node {
                current_level.push(n.val);
                next_queue.push(n.left.as_deref());
                next_queue.push(n.right.as_deref());
            }
        }

        if !current_level.is_empty() {
            levels.push(current_level);
        }

        queue = next_queue;
    }
    levels
}


#[cfg(test)]
mod tests {
    use super::*;
    use crate::prng::Rng;


    fn build_tree(level: &[Option<i32>]) -> Option<Box<TreeNode>> {
        let root_val = match level.first() {
            Some(Some(v)) => *v,
            _ => return None,
        };
        // Flat arena: (val, left index, right index), filled level by level.
        let mut nodes: Vec<(i32, Option<usize>, Option<usize>)> = vec![(root_val, None, None)];
        let mut head = 0;
        let mut i = 1;
        while i < level.len() && head < nodes.len() {
            if let Some(v) = level[i] {
                nodes.push((v, None, None));
                nodes[head].1 = Some(nodes.len() - 1);
            }
            i += 1;
            if i >= level.len() {
                break;
            }
            if let Some(v) = level[i] {
                nodes.push((v, None, None));
                nodes[head].2 = Some(nodes.len() - 1);
            }
            i += 1;
            head += 1;
        }
        fn to_boxed(nodes: &[(i32, Option<usize>, Option<usize>)], idx: usize) -> Box<TreeNode> {
            let (val, l, r) = nodes[idx];
            Box::new(TreeNode {
                val,
                left: l.map(|i| to_boxed(nodes, i)),
                right: r.map(|i| to_boxed(nodes, i)),
            })
        }
        Some(to_boxed(&nodes, 0))
    }

    fn build_random_tree(r: &mut Rng, n: usize) -> Option<Box<TreeNode>> {
        let mut root: Option<Box<TreeNode>> = None;
        for count in 0..n {
            let node = TreeNode::leaf(count as i32); // distinct values
            let mut slot = &mut root;
            while let Some(cur) = slot {
                slot = if r.bool() { &mut cur.left } else { &mut cur.right };
            }
            *slot = Some(node);
        }
        root
    }

    // Test-only helpers: count nodes / collect depth of each value 
    fn count_nodes(node: Option<&TreeNode>) -> usize {
        let Some(n) = node else { return 0 };
        1 + count_nodes(n.left.as_deref()) + count_nodes(n.right.as_deref())
    }

    fn depth_of_value(node: Option<&TreeNode>, val: i32, depth: usize) -> Option<usize> {
        let n = node?;
        if n.val == val {
            return Some(depth);
        }
        if let Some(d) = depth_of_value(n.left.as_deref(), val, depth + 1) {
            return Some(d);
        }
        depth_of_value(n.right.as_deref(), val, depth + 1)
    }

    #[test]
    fn example_from_the_study_page_1_2_3_4_5() {
        let root = build_tree(&[Some(1), Some(2), Some(3), Some(4), Some(5)]);

        let levels = level_order(root.as_deref());

        assert_eq!(levels.len(), 3);
        assert_eq!(&levels[0][..], &[1]);
        assert_eq!(&levels[1][..], &[2, 3]);
        assert_eq!(&levels[2][..], &[4, 5]);
    }

    #[test]
    fn empty_tree_empty_outer_vec() {
        let levels = level_order(None);
        assert_eq!(levels.len(), 0);
    }

    #[test]
    fn single_node_and_missing_children_keep_left_to_right_order() {
        // 1 has only a right child 3, which has only a left child 4.
        let root = build_tree(&[Some(1), None, Some(3), Some(4), None]);

        let levels = level_order(root.as_deref());

        assert_eq!(levels.len(), 3);
        assert_eq!(&levels[0][..], &[1]);
        assert_eq!(&levels[1][..], &[3]);
        assert_eq!(&levels[2][..], &[4]);
    }

    #[test]
    fn stress_every_value_lands_on_the_level_equal_to_its_depth() {
        let mut r = Rng::new(0xD00D18);
        for _ in 0..25 {
            let n = r.range_usize(1, 50);
            let root = build_random_tree(&mut r, n);

            let levels = level_order(root.as_deref());

            // Total emitted values equals node count.
            let mut total = 0;
            for level in &levels {
                assert!(!level.is_empty()); // no empty levels
                total += level.len();
            }
            assert_eq!(total, count_nodes(root.as_deref()));

            // Each value appears on the level matching its true depth.
            for (li, level) in levels.iter().enumerate() {
                for &v in level {
                    assert_eq!(depth_of_value(root.as_deref(), v, 0), Some(li));
                }
            }
        }
    }
}
