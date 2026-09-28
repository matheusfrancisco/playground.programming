//! Given a ternary tree (each node has up to THREE children), return every
//! root-to-leaf path as a string of values joined by "->", e.g. "1->2->4".
//!
//! Example (mirrors the study page): root 1 with children 2, 4, 6, where
//! node 2 has one child 3 → paths ["1->2->3", "1->4", "1->6"].
//!
//! Paths are emitted in DFS order, visiting children slot 0, then 1, then 2.
//! Empty tree → empty Vec.
//!
//! Requirements
//! - O(n) node visits; each leaf materializes ONE string of its full path.
//! - The shared-path version keeps O(h) extra state (plus the output);
//!   the copy-per-call version allocates a fresh path at every step.
//! - Recursion depth O(h).

#[derive(Debug)]
pub struct Node {
    pub val: i32,
    pub children: [Option<Box<Node>>; 3],
}

/// Return all root-to-leaf paths as "v1->v2->...->vk" strings, in DFS order
/// (children visited slot 0, 1, 2). Empty tree → empty Vec.
pub fn ternary_tree_paths(root: Option<&Node>) -> Vec<String> {
    let mut out = Vec::<String>::new();

    // this algorithm has mutation over a shared path string
    // which is more efficient than the copy-per-call version,
    // which allocates a new string at every recursive call
    // but there is mutation
    fn dfs(node: &Node, prefix_str: &mut String, out: &mut Vec<String>) {
        let old_len = prefix_str.len();
        let sep = if prefix_str.is_empty() { "" } else { "->" };
        prefix_str.push_str(sep);
        prefix_str.push_str(&node.val.to_string());
        let is_leaf = node.children.iter().all(Option::is_none);
        if is_leaf {
            out.push(prefix_str.clone());
        } else {
            for child in node.children.iter().flatten() {
                dfs(child, prefix_str, out);
            }
        }
        prefix_str.truncate(old_len);
    }

    if let Some(r) = root {
        let mut prefix_str = String::new();
        dfs(r, &mut prefix_str, &mut out);
    }

    out
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::prng::Rng;

    fn mk(val: i32) -> Box<Node> {
        Box::new(Node {
            val,
            children: [None, None, None],
        })
    }

    /// Attach n nodes at random free child slots  used by the stress test.
    fn build_random_ternary(r: &mut Rng, n: usize) -> Option<Box<Node>> {
        if n == 0 {
            return None;
        }
        // Arena of (val, child indices), materialized into boxes at the end.
        let mut nodes: Vec<(i32, [Option<usize>; 3])> = vec![(r.range_i32(-99, 99), [None; 3])];
        while nodes.len() < n {
            let val = r.range_i32(-99, 99);
            let idx = nodes.len();
            // With k nodes placed, at most k-1 of the 3k slots are taken,
            // so a free slot always exists and this retry loop terminates.
            loop {
                let parent = r.below(nodes.len());
                let slot = r.below(3);
                if nodes[parent].1[slot].is_none() {
                    nodes[parent].1[slot] = Some(idx);
                    break;
                }
            }
            nodes.push((val, [None; 3]));
        }

        fn materialize(nodes: &[(i32, [Option<usize>; 3])], idx: usize) -> Box<Node> {
            let (val, kids) = nodes[idx];
            Box::new(Node {
                val,
                children: kids.map(|k| k.map(|j| materialize(nodes, j))),
            })
        }
        Some(materialize(&nodes, 0))
    }

    // ── Test-only oracle: copy-path-per-call collector (the allocate-heavy ──
    // ── version from the page, independent of your shared-path solution)   ──

    fn oracle_dfs(node: &Node, prefix: &str, out: &mut Vec<String>) {
        let sep = if prefix.is_empty() { "" } else { "->" };
        let full = format!("{}{}{}", prefix, sep, node.val);
        let is_leaf = node.children.iter().all(Option::is_none);
        if is_leaf {
            out.push(full);
            return;
        }
        for child in node.children.iter().flatten() {
            oracle_dfs(child, &full, out);
        }
    }

    fn oracle_paths(root: Option<&Node>) -> Vec<String> {
        let mut out = Vec::new();
        if let Some(r) = root {
            oracle_dfs(r, "", &mut out);
        }
        out
    }

    #[test]
    fn example_from_the_study_page_1_2_4_6_2_3() {
        let mut root = mk(1);
        root.children[0] = Some(mk(2));
        root.children[1] = Some(mk(4));
        root.children[2] = Some(mk(6));
        root.children[0].as_mut().unwrap().children[0] = Some(mk(3));

        let paths = ternary_tree_paths(Some(&root));
        assert_eq!(paths.len(), 3);
        assert_eq!(paths[0], "1->2->3");
        assert_eq!(paths[1], "1->4");
        assert_eq!(paths[2], "1->6");
    }

    #[test]
    fn empty_tree_and_single_node_negative_value_keeps_its_sign() {
        let none = ternary_tree_paths(None);
        assert_eq!(none.len(), 0);

        let one = mk(-5);
        let paths = ternary_tree_paths(Some(&one));
        assert_eq!(paths.len(), 1);
        assert_eq!(paths[0], "-5");
    }

    #[test]
    fn deterministic_order_slot_index_0_2_decides_not_the_values() {
        // slot 0 empty, slot 1 holds 5, slot 2 holds 2 → "1->5" before "1->2".
        let mut root = mk(1);
        root.children[1] = Some(mk(5));
        root.children[2] = Some(mk(2));

        let paths = ternary_tree_paths(Some(&root));
        assert_eq!(paths.len(), 2);
        assert_eq!(paths[0], "1->5");
        assert_eq!(paths[1], "1->2");
    }

    #[test]
    fn degenerate_chain_through_the_middle_slot_one_long_path() {
        let mut root = mk(1);
        root.children[1] = Some(mk(2));
        root.children[1].as_mut().unwrap().children[1] = Some(mk(3));
        root.children[1].as_mut().unwrap().children[1]
            .as_mut()
            .unwrap()
            .children[1] = Some(mk(4));

        let paths = ternary_tree_paths(Some(&root));
        assert_eq!(paths.len(), 1);
        assert_eq!(paths[0], "1->2->3->4");
    }

    #[test]
    fn stress_matches_the_copy_per_call_oracle_on_random_ternary_trees() {
        let mut r = Rng::new(0x7E12A47);
        for _ in 0..30 {
            let n = r.range_usize(0, 50);
            let root = build_random_ternary(&mut r, n);

            let want = oracle_paths(root.as_deref());
            let got = ternary_tree_paths(root.as_deref());

            // Both walk children in slot order, so visit order is identical.
            assert_eq!(got.len(), want.len());
            for (w, g) in want.iter().zip(&got) {
                assert_eq!(g, w);
            }
        }
    }
}
