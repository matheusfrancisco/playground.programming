//! The study page puts a knight at [0, 0] on an infinitely large chessboard
//! and asks for the minimum number of knight moves to reach a destination
//! [x, y]. A knight moves in the eight (±1, ±2) / (±2, ±1) L-shapes.
//!

use std::collections::VecDeque;

/// The 8 knight-move deltas.
pub const KNIGHT_MOVES: [[i64; 2]; 8] = [
    [1, 2],
    [2, 1],
    [-1, 2],
    [-2, 1],
    [1, -2],
    [2, -1],
    [-1, -2],
    [-2, -1],
];

/// Minimum number of knight moves from `start` to `target` on an n×n board,
/// or None if unreachable. Squares are [row, col]. Asserts n > 0 and both
/// squares are on the board.
pub fn knight_shortest_path(n: usize, start: [usize; 2], target: [usize; 2]) -> Option<usize> {
    assert!(n > 0);
    assert!(start[0] < n && start[1] < n);
    assert!(target[0] < n && target[1] < n);

    if start == target {
        return Some(0);
    }
    let mut queue = VecDeque::<(usize, usize, usize)>::new();
    queue.push_back((start[0], start[1], 0));
    let mut visited = vec![vec![false; n]; n];
    visited[start[0]][start[1]] = true;

    while let Some((r, c, d)) = queue.pop_front() {
        if [r, c] == target {
            return Some(d);
        }

        for kmove in KNIGHT_MOVES {
            let nr = r as i64 + kmove[0];
            let nc = c as i64 + kmove[1];
            if nr < 0 || nc < 0 {
                continue;
            }
            let (ur, uc) = (nr as usize, nc as usize);
            if ur >= n || uc >= n {
                continue;
            }
            if !visited[ur][uc] {
                visited[ur][uc] = true;
                queue.push_back((ur, uc, d + 1));
            }
        }
    }
    None
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::prng::Rng;

    // Deliberately NOT a BFS: repeatedly relax every square over the 8-move edge
    // set until no distance improves. Slow but obviously correct.

    fn oracle_knight_dist(n: usize, start: [usize; 2], target: [usize; 2]) -> Option<usize> {
        assert!(n > 0);
        let inf = usize::MAX;
        let mut dist = vec![inf; n * n];
        dist[start[0] * n + start[1]] = 0;

        let mut changed = true;
        while changed {
            changed = false;
            for r in 0..n {
                for c in 0..n {
                    let d = dist[r * n + c];
                    if d == inf {
                        continue;
                    }
                    for m in KNIGHT_MOVES {
                        let nr = r as i64 + m[0];
                        let nc = c as i64 + m[1];
                        if nr < 0 || nc < 0 {
                            continue;
                        }
                        let (ur, uc) = (nr as usize, nc as usize);
                        if ur >= n || uc >= n {
                            continue;
                        }
                        if dist[ur * n + uc] > d + 1 {
                            dist[ur * n + uc] = d + 1;
                            changed = true;
                        }
                    }
                }
            }
        }

        let td = dist[target[0] * n + target[1]];
        if td == inf { None } else { Some(td) }
    }

    #[test]
    fn example_from_the_study_page_knight_at_0_0_small_destinations() {
        // The page's destinations [1,2] and [2,4] fit on an 8×8 board without the
        // boundary mattering, so the answers match the infinite-board ones.
        assert_eq!(knight_shortest_path(8, [0, 0], [1, 2]), Some(1));
        assert_eq!(knight_shortest_path(8, [0, 0], [2, 4]), Some(2));
        // Already there → zero moves.
        assert_eq!(knight_shortest_path(8, [3, 3], [3, 3]), Some(0));
    }

    #[test]
    fn corner_to_corner_on_the_full_8x8_board_takes_6_moves() {
        assert_eq!(knight_shortest_path(8, [0, 0], [7, 7]), Some(6));
    }

    #[test]
    fn degenerate_boards_1x1_is_trivial_2x2_knight_cannot_move() {
        assert_eq!(knight_shortest_path(1, [0, 0], [0, 0]), Some(0));
        // Every knight move leaves a 2×2 board → any other square is unreachable.
        assert_eq!(knight_shortest_path(2, [0, 0], [1, 1]), None);
    }

    #[test]
    fn board_3x3_the_center_is_cut_off_corners_still_connect() {
        // No knight move enters or leaves (1,1) on a 3×3 board.
        assert_eq!(knight_shortest_path(3, [0, 0], [1, 1]), None);
        // Opposite corner is reachable, but only the long way round.
        assert_eq!(knight_shortest_path(3, [0, 0], [2, 2]), Some(4));
    }

    #[test]
    fn stress_matches_bellman_ford_relaxation_oracle_on_random_boards() {
        let mut r = Rng::new(0x20A417ED);
        for _ in 0..60 {
            let n = r.range_usize(1, 8);
            let start = [r.range_usize(0, n - 1), r.range_usize(0, n - 1)];
            let target = [r.range_usize(0, n - 1), r.range_usize(0, n - 1)];

            let want = oracle_knight_dist(n, start, target);
            let got = knight_shortest_path(n, start, target);
            assert_eq!(got, want);

            // Sanity relationships: distance fits on the board; symmetric moves
            // mean the reverse trip has the same length.
            if let Some(d) = got {
                assert!(d < n * n);
                let back = knight_shortest_path(n, target, start);
                assert_eq!(back, Some(d));
            }
        }
    }
}
