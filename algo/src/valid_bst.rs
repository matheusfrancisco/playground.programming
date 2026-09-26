//! A binary search tree (BST) requires that for EVERY node, all values in its
//! left subtree are strictly smaller and all values in its right subtree are
//! strictly greater than the node's value. Equivalently (study page): an
//! in-order traversal of a BST yields a strictly increasing sequence.
//! Given a binary tree, decide whether it is a valid BST.
//!
//! This escalates P17 (visible tree nodes): there you carried ONE bound down
//! the recursion (the max seen so far); here every node lives inside an open
//! interval, so you carry TWO bounds down (min, max) and tighten one of them
//! at each step.
//!
//! The classic wrong answer checks only parent vs. child locally. It accepts
//! this tree, where a GRANDCHILD violates the GRANDPARENT's bound:
//!         5
//!        / \
//!       4   6
//!          / \
//!         3   7
//! Locally 3 < 6 looks fine, but 3 sits in the RIGHT subtree of 5, so every
//! value there must exceed 5. Not a BST.

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

pub fn is_valid_bst(root: Option<&TreeNode>) -> bool {
    // Every node must satisfy lo < val < hi, where `None` means unbounded.
    // Descending left tightens the upper bound; descending right tightens the lower.
    fn helper(node: Option<&TreeNode>, lo: Option<i32>, hi: Option<i32>) -> bool {
        let Some(n) = node else { return true };
        println!("node {} lo {:?} hi {:?}", n.val, lo, hi);
        if lo.is_some_and(|lo| n.val <= lo) || hi.is_some_and(|hi| n.val >= hi) {
            return false;
        }
        helper(n.left.as_deref(), lo, Some(n.val)) && helper(n.right.as_deref(), Some(n.val), hi)
    }
    helper(root, None, None)
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::prng::Rng;

    /// Build a tree from a level-order array where `None` marks a missing child.
    /// Children slots are only consumed for nodes that exist (LeetCode-style).
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

    /// Insert a node using the BST rule (assumes distinct values) — used by the
    /// stress test to build trees that are valid BSTs by construction.
    fn bst_insert(root: &mut Option<Box<TreeNode>>, node: Box<TreeNode>) {
        let mut slot = root;
        while let Some(cur) = slot {
            slot = if node.val < cur.val {
                &mut cur.left
            } else {
                &mut cur.right
            };
        }
        *slot = Some(node);
    }

    /// Build a random valid BST by inserting a shuffled set of DISTINCT values.
    fn build_random_valid_bst(r: &mut Rng, n: usize) -> Option<Box<TreeNode>> {
        let mut vals: Vec<i32> = (0..n).map(|i| i as i32 * 3 - 90).collect(); // distinct
        r.shuffle(&mut vals);
        let mut root: Option<Box<TreeNode>> = None;
        for v in vals {
            bst_insert(&mut root, TreeNode::leaf(v));
        }
        root
    }

    /// Insert n nodes at random positions (duplicates allowed) — almost always
    /// NOT a BST; the stress test checks agreement with the oracle either way.
    fn build_random_tree(r: &mut Rng, n: usize) -> Option<Box<TreeNode>> {
        let mut root: Option<Box<TreeNode>> = None;
        for _ in 0..n {
            let node = TreeNode::leaf(r.range_i32(-50, 50));
            let mut slot = &mut root;
            while let Some(cur) = slot {
                slot = if r.bool() {
                    &mut cur.left
                } else {
                    &mut cur.right
                };
            }
            *slot = Some(node);
        }
        root
    }

    fn inorder_collect(node: Option<&TreeNode>, out: &mut Vec<i32>) {
        let Some(n) = node else { return };
        inorder_collect(n.left.as_deref(), out);
        out.push(n.val);
        inorder_collect(n.right.as_deref(), out);
    }

    fn oracle_is_bst(root: Option<&TreeNode>) -> bool {
        let mut vals = Vec::new();
        inorder_collect(root, &mut vals);
        vals.windows(2).all(|w| w[0] < w[1])
    }

    #[test]
    fn example_from_the_study_page_bst_accepted_grandchild_violation_rejected() {
        // A proper BST: in-order 3,4,5,6,7,8,9.
        let good = build_tree(&[
            Some(6),
            Some(4),
            Some(8),
            Some(3),
            Some(5),
            Some(7),
            Some(9),
        ]);
        assert!(is_valid_bst(good.as_deref()));
        // The header's counterexample: 3 < 6 locally, but 3 is in the right
        // subtree of 5  a local parent/child check wrongly accepts this.
        let bad = build_tree(&[Some(5), Some(4), Some(6), None, None, Some(3), Some(7)]);
        assert!(!is_valid_bst(bad.as_deref()));
    }

    #[test]
    fn empty_tree_and_single_node_are_valid_extreme_i32_values_need_open_bounds() {
        assert!(is_valid_bst(None));
        let one = build_tree(&[Some(42)]);
        assert!(is_valid_bst(one.as_deref()));
        // i32::MIN/i32::MAX as NODE VALUES: valid tree — i32 sentinels would
        // wrongly reject the children here (design question 4).
        let wide = build_tree(&[Some(0), Some(i32::MIN), Some(i32::MAX)]);
        assert!(is_valid_bst(wide.as_deref()));
        // Duplicate of i32::MAX in the right subtree: strictness must reject it.
        let dup = build_tree(&[Some(i32::MAX), None, Some(i32::MAX)]);
        assert!(!is_valid_bst(dup.as_deref()));
    }

    #[test]
    fn degenerate_chains_strictly_increasing_valid_one_duplicate_breaks_it() {
        let inc = build_tree(&[Some(1), None, Some(2), None, Some(3)]);
        assert!(is_valid_bst(inc.as_deref()));
        let flat = build_tree(&[Some(1), None, Some(2), None, Some(2)]);
        assert!(!is_valid_bst(flat.as_deref()));
    }

    #[test]
    fn stress_agrees_with_in_order_oracle_on_valid_by_construction_and_random_trees() {
        let mut r = Rng::new(0xB57A17);
        for _ in 0..40 {
            let n = r.range_usize(0, 60);

            // Valid BST by insertion of distinct values: both must say true.
            let good = build_random_valid_bst(&mut r, n);
            assert!(oracle_is_bst(good.as_deref()));
            assert!(is_valid_bst(good.as_deref()));

            // Random-shape tree (usually invalid): verdicts must agree either way.
            let any = build_random_tree(&mut r, n);
            assert_eq!(is_valid_bst(any.as_deref()), oracle_is_bst(any.as_deref()));
        }
    }
}
