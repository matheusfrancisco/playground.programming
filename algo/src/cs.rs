//! There are `n` courses numbered 0..n-1. Each prerequisite pair `[a, b]`
//! means you must take course `b` BEFORE course `a`. Decide whether it is
//! possible to finish all courses i.e. whether the dependency digraph is
//! acyclic.

/// Return true iff all `n` courses can be finished, i.e. the digraph of
/// "prereqs[i][0] depends on prereqs[i][1]" edges has no cycle.
/// Course numbers in `prereqs` are asserted to be < n.
pub fn can_finish(n: usize, prereqs: &[[usize; 2]]) -> bool {
    let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
    let mut indeg = vec![0usize; n];
    let mut n_course = n;

    for [course, pre] in prereqs {
        adj[*pre].push(*course);
        indeg[*course] += 1;
    }

    let mut q: Vec<usize> = (0..n).filter(|&i| indeg[i] == 0).collect();

    while let Some(c) = q.pop() {
        n_course -= 1;
        for &next in &adj[c] {
            indeg[next] -= 1;
            if indeg[next] == 0 {
                q.push(next);
            }
        }
    }

    n_course == 0
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::prng::Rng;

    // Kahn's BFS topological sort (spec keep it green)

    /// Independent cycle check: repeatedly take courses whose remaining
    /// in-degree is zero; the digraph is acyclic iff every course gets taken.
    fn oracle_kahn(n: usize, prereqs: &[[usize; 2]]) -> bool {
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        let mut indeg = vec![0usize; n];

        for &[course, pre] in prereqs {
            assert!(course < n && pre < n);
            adj[pre].push(course); // edge: prerequisite → dependent
            indeg[course] += 1;
        }

        // Index-based queue: Vec + head cursor.
        let mut q: Vec<usize> = (0..n).filter(|&i| indeg[i] == 0).collect();

        let mut head = 0;
        let mut taken = 0;
        while head < q.len() {
            let c = q[head];
            head += 1;
            taken += 1;
            for &next in &adj[c] {
                indeg[next] -= 1;
                if indeg[next] == 0 {
                    q.push(next);
                }
            }
        }
        taken == n
    }

    #[test]
    fn examples_from_the_study_page_one_prereq_ok_mutual_dependency_not() {
        // Example 1: n = 2, [[0, 1]] → true (take 1 first, then 0).
        assert!(can_finish(2, &[[0, 1]]));
        // Example 2: n = 2, [[0, 1], [1, 0]] → false (they depend on each other).
        assert!(!can_finish(2, &[[0, 1], [1, 0]]));
    }

    #[test]
    fn diamond_dependency_is_fine_two_state_visited_would_cry_cycle() {
        // 1 and 2 both need 0; 3 needs both 1 and 2. DFS from 3 reaches 0 twice —
        // the second arrival hits a BLACK node, not a gray one. Acyclic.
        let diamond = [[1, 0], [2, 0], [3, 1], [3, 2]];
        assert!(can_finish(4, &diamond));
    }

    #[test]
    fn no_prerequisites_at_all_always_finishable_including_n_0() {
        assert!(can_finish(0, &[]));
        assert!(can_finish(5, &[]));
    }

    #[test]
    fn self_loop_and_longer_cycle_are_both_unfinishable() {
        // A course requiring itself: gray→gray on the very first edge.
        assert!(!can_finish(3, &[[1, 1]]));
        // 0 → 1 → 2 → 0, plus an innocent bystander course 3.
        let ring = [[0, 1], [1, 2], [2, 0]];
        assert!(!can_finish(4, &ring));
    }

    #[test]
    fn stress_random_digraphs_match_kahns_algorithm_oracle() {
        let mut r = Rng::new(0xC0DE20B);
        for round in 0..60 {
            // Even rounds force acyclic edges (dependent > prerequisite), which
            // needs n >= 2; odd rounds are fully random (cycles likely).
            let dag_only = round % 2 == 0;
            let n = r.range_usize(if dag_only { 2 } else { 1 }, 12);
            let e = r.range_usize(0, 20);
            let prereqs: Vec<[usize; 2]> = (0..e)
                .map(|_| {
                    if dag_only {
                        let course = r.range_usize(1, n - 1);
                        [course, r.range_usize(0, course - 1)]
                    } else {
                        [r.range_usize(0, n - 1), r.range_usize(0, n - 1)]
                    }
                })
                .collect();

            let want = oracle_kahn(n, &prereqs);
            let got = can_finish(n, &prereqs);
            assert_eq!(got, want);
            // Forced-acyclic rounds must always be finishable.
            if dag_only {
                assert!(got);
            }
        }
    }
}
