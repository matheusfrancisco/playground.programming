//! MS-Paint's bucket tool. Given a grid of colors, a seed coordinate (r, c)
//! and a replacement color, repaint every cell connected to the seed
//! horizontally or vertically (NOT diagonally) through cells of the seed's
//!
//! Example: seed (2, 2) holds color 8, replacement 9. The
//! 4-connected 8-region {(1,1),(1,2),(2,2),(2,3),(3,2)} becomes 9; the cell
//! (3,3) that was ALREADY 9 is untouched, and so is every cell outside the
//! region.

/// Repaint, in place, the 4-connected region of grid[r][c]'s color with
/// `color`. Asserts the seed is in bounds and rows are equal length.
/// Must terminate (as a no-op) when `color` equals the seed's color.
pub fn flood_fill(grid: &mut [Vec<u8>], r: usize, c: usize, color: u8) {
    let Some(&original) = grid.get_mut(r).and_then(|row| row.get(c)) else {
        return;
    };

    if original == color {
        return;
    }
    let mut stack = vec![(r, c)];
    grid[r][c] = color;

    while let Some((r, c)) = stack.pop() {
        for (dr, dc) in [(-1isize, 0isize), (1, 0), (0, -1), (0, 1)] {
            let Some(nr) = r.checked_add_signed(dr) else {
                continue;
            };
            let Some(nc) = c.checked_add_signed(dc) else {
                continue;
            };

            let Some(cell) = grid.get_mut(nr).and_then(|row| row.get_mut(nc)) else {
                continue;
            };

            if *cell == original {
                *cell = color;

                stack.push((nr, nc))
            }
        }
    }
}


#[cfg(test)]
mod tests {
    use super::*;
    use crate::prng::Rng;

    /// Build a rows×cols grid of mutable rows from row-major flat data.
    fn make_grid(rows: usize, cols: usize, flat: &[u8]) -> Vec<Vec<u8>> {
        assert_eq!(flat.len(), rows * cols);
        flat.chunks(cols).map(<[u8]>::to_vec).collect()
    }

    fn assert_grid_equals(grid: &[Vec<u8>], flat: &[u8], cols: usize) {
        for (i, row) in grid.iter().enumerate() {
            assert_eq!(&row[..], &flat[i * cols..(i + 1) * cols]);
        }
    }

    /// Flat mask of the 4-connected same-color component of (r, c), computed on
    /// a PRISTINE grid with an index-queue BFS (independent of the solution).
    fn oracle_component(grid: &[Vec<u8>], r: usize, c: usize) -> Vec<bool> {
        let rows = grid.len();
        let cols = grid[0].len();
        let mut mask = vec![false; rows * cols];

        let old = grid[r][c];
        let mut q: Vec<usize> = Vec::new();
        mask[r * cols + c] = true;
        q.push(r * cols + c);
        let mut head = 0;
        while head < q.len() {
            let idx = q[head];
            head += 1;
            let cr = idx / cols;
            let cc = idx % cols;
            // Up, down, left, right.
            if cr > 0 {
                oracle_visit(&mut q, &mut mask, grid, old, idx - cols);
            }
            if cr + 1 < rows {
                oracle_visit(&mut q, &mut mask, grid, old, idx + cols);
            }
            if cc > 0 {
                oracle_visit(&mut q, &mut mask, grid, old, idx - 1);
            }
            if cc + 1 < cols {
                oracle_visit(&mut q, &mut mask, grid, old, idx + 1);
            }
        }
        mask
    }

    fn oracle_visit(q: &mut Vec<usize>, mask: &mut [bool], grid: &[Vec<u8>], old: u8, idx: usize) {
        let cols = grid[0].len();
        if !mask[idx] && grid[idx / cols][idx % cols] == old {
            mask[idx] = true;
            q.push(idx);
        }
    }

    /// After the fill: cells in the component are exactly `color`, everything
    /// else exactly matches the pristine copy.
    fn assert_exact_fill(pristine: &[Vec<u8>], filled: &[Vec<u8>], mask: &[bool], color: u8) {
        let cols = pristine[0].len();
        for (i, row) in filled.iter().enumerate() {
            for (j, &cell) in row.iter().enumerate() {
                let want = if mask[i * cols + j] {
                    color
                } else {
                    pristine[i][j]
                };
                assert_eq!(cell, want);
            }
        }
    }

    #[test]
    fn example_from_the_study_page_repaint_the_8_region_at_2_2_with_9() {
        let before = [
            0, 1, 3, 4, 1, //
            3, 8, 8, 3, 3, //
            6, 7, 8, 8, 3, //
            12, 2, 8, 9, 1, //
            12, 3, 1, 3, 2, //
        ];
        let after = [
            0, 1, 3, 4, 1, //
            3, 9, 9, 3, 3, //
            6, 7, 9, 9, 3, //
            12, 2, 9, 9, 1, //
            12, 3, 1, 3, 2, //
        ];
        let mut grid = make_grid(5, 5, &before);
        flood_fill(&mut grid, 2, 2, 9);
        assert_grid_equals(&grid, &after, 5);
    }

    #[test]
    fn trap_replacement_equals_the_seeds_color_terminates_grid_unchanged() {
        let flat = [
            5, 5, 3, //
            5, 5, 5, //
            3, 5, 5, //
        ];
        let mut grid = make_grid(3, 3, &flat);
        flood_fill(&mut grid, 1, 1, 5); // new color == old color
        assert_grid_equals(&grid, &flat, 3);
    }

    #[test]
    fn edges_1x1_grid_corner_seed_whole_grid_one_color() {
        {
            let mut one = make_grid(1, 1, &[7]);
            flood_fill(&mut one, 0, 0, 2);
            assert_grid_equals(&one, &[2], 1);
        }
        {
            // Seed in the bottom-right corner; region hugs two borders.
            let flat = [
                1, 2, 2, //
                1, 1, 2, //
            ];
            let mut grid = make_grid(2, 3, &flat);
            flood_fill(&mut grid, 1, 2, 6);
            assert_grid_equals(&grid, &[1, 6, 6, 1, 1, 6], 3);
        }
        {
            // Uniform grid: everything repaints.
            let mut grid = make_grid(2, 2, &[4, 4, 4, 4]);
            flood_fill(&mut grid, 0, 1, 8);
            assert_grid_equals(&grid, &[8, 8, 8, 8], 2);
        }
    }

    #[test]
    fn diagonals_do_not_connect() {
        let flat = [
            1, 0, //
            0, 1, //
        ];
        let mut grid = make_grid(2, 2, &flat);
        flood_fill(&mut grid, 0, 0, 9);
        // Only the seed changes; the diagonal 1 at (1,1) is NOT connected.
        assert_grid_equals(&grid, &[9, 0, 0, 1], 2);
    }

    #[test]
    fn stress_exactly_the_seeds_component_changes_per_independent_bfs_oracle() {
        let mut rand = Rng::new(0xF100DF11);
        for _ in 0..40 {
            let rows = rand.range_usize(1, 10);
            let cols = rand.range_usize(1, 10);
            // Few colors → large components; occasionally color == old (the trap).
            let flat: Vec<u8> = (0..rows * cols)
                .map(|_| rand.range_i32(0, 3) as u8)
                .collect();

            let pristine = make_grid(rows, cols, &flat);
            let mut grid = make_grid(rows, cols, &flat);

            let r = rand.range_usize(0, rows - 1);
            let c = rand.range_usize(0, cols - 1);
            let color = rand.range_i32(0, 3) as u8;

            let mask = oracle_component(&pristine, r, c);

            flood_fill(&mut grid, r, c, color);
            assert_exact_fill(&pristine, &grid, &mask, color);
        }
    }
}
