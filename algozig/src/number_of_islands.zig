//! Given a 2-D matrix of '0' and '1' cells, count the number of islands of
//! '1'. An island is a maximal group of '1' cells connected horizontally or
//! vertically (NOT diagonally), surrounded by '0' cells or the grid edge.
//!
//! API note: this file uses a FLAT grid — `grid` is a row-major []const u8 of
//! '1'/'0' bytes with grid.len == rows * cols. Cell (r, c) lives at
//! grid[r * cols + c]. Chosen over []const []const u8 because it makes test
//! construction and the stress generator far simpler.
//!
//! Example (study page picture, flattened):
//!   1 1 0 0        "1100"
//!   1 1 0 0    →   "1100"   → 2 islands
//!   0 0 1 0        "0010"
//!
//! Requirements
//! ------------
//! - O(rows*cols) time; visited bookkeeping allowed (allocate via `alloc`).
//! - Each cell must be visited a bounded number of times — no rescanning.
//!

const std = @import("std");
const print = std.debug.print;

fn visit(
    alloc: std.mem.Allocator,
    queue: *std.ArrayList(usize),
    visited: []bool,
    grid: []const u8,
    idx: usize,
) !void {
    if (grid[idx] == '1' and !visited[idx]) {
        visited[idx] = true;
        try queue.append(alloc, idx);
    }
}
/// Count 4-connected islands of '1' bytes in a row-major flat grid.
/// Asserts grid.len == rows * cols.
pub fn countIslands(alloc: std.mem.Allocator, grid: []const u8, rows: usize, cols: usize) !usize {
    const visited = try alloc.alloc(bool, grid.len);
    defer alloc.free(visited);
    @memset(visited, false);

    var queue: std.ArrayList(usize) = .empty;
    defer queue.deinit(alloc);
    //print("countIslands: grid = \"{s}\", rows = {}, cols = {}\n", .{ grid, rows, cols });
    //    "012345678"
    //g = "110011000010"; 3 rows, 4 cols
    //g[0*4...][0..4] = [0..][0..4] = "1100"
    //g = "10011000010"; 3 rows, 4 cols
    //g[1*4..][0..4] = [4..][0..4] = "1100"
    //g = "10011000010"; 3 rows, 4 cols
    //g[2*4..][0..4] = [8..][0..4] = "0010"

    var islands: usize = 0;
    for (grid, 0..) |cell, start| {
        //print("countIslands: cell = {c}, start = {}, visited[start] = {}\n", .{ cell, start, visited[start] });
        if (cell != '1' or visited[start]) continue;
        print("countIslands: found new island at start = {}\n", .{start});

        islands += 1;
        visited[start] = true;
        queue.clearRetainingCapacity();
        try queue.append(alloc, start);
        var head: usize = 0;
        while (head < queue.items.len) : (head += 1) {
            const idx = queue.items[head];
            const r = idx / cols;
            const c = idx % cols;
            print("countIslands: visiting idx = {}, r = {}, c = {}\n", .{ idx, r, c });

            if (r > 0) try visit(alloc, &queue, visited, grid, idx - cols);
            if (r + 1 < rows) try visit(alloc, &queue, visited, grid, idx + cols);
            if (c > 0) try visit(alloc, &queue, visited, grid, idx - 1);
            if (c + 1 < cols) try visit(alloc, &queue, visited, grid, idx + 1);
            print("countIslands: queue = {any}\n", .{queue.items});
        }
    }
    return islands;
}

fn oracleIslands(alloc: std.mem.Allocator, grid: []const u8, rows: usize, cols: usize) !usize {
    std.debug.assert(grid.len == rows * cols);
    const visited = try alloc.alloc(bool, grid.len);
    defer alloc.free(visited);
    @memset(visited, false);

    var stack: std.ArrayList(usize) = .empty;
    defer stack.deinit(alloc);

    var islands: usize = 0;
    for (grid, 0..) |cell, start| {
        if (cell != '1' or visited[start]) continue;
        islands += 1;
        visited[start] = true;
        try stack.append(alloc, start);
        while (stack.pop()) |idx| {
            const r = idx / cols;
            const c = idx % cols;
            // Up, down, left, right.
            if (r > 0) try oracleVisit(alloc, &stack, visited, grid, idx - cols);
            if (r + 1 < rows) try oracleVisit(alloc, &stack, visited, grid, idx + cols);
            if (c > 0) try oracleVisit(alloc, &stack, visited, grid, idx - 1);
            if (c + 1 < cols) try oracleVisit(alloc, &stack, visited, grid, idx + 1);
        }
    }
    return islands;
}

fn oracleVisit(
    alloc: std.mem.Allocator,
    stack: *std.ArrayList(usize),
    visited: []bool,
    grid: []const u8,
    idx: usize,
) !void {
    if (grid[idx] == '1' and !visited[idx]) {
        visited[idx] = true;
        try stack.append(alloc, idx);
    }
}

test "example from the study page: two islands" {
    const alloc = std.testing.allocator;
    const grid = "1100" ++ "1100" ++ "0010";
    try std.testing.expectEqual(@as(usize, 2), try countIslands(alloc, grid, 3, 4));
}

test "all water → 0; all land → 1" {
    const alloc = std.testing.allocator;
    try std.testing.expectEqual(@as(usize, 0), try countIslands(alloc, "000000", 2, 3));
    try std.testing.expectEqual(@as(usize, 1), try countIslands(alloc, "111111", 2, 3));
}

test "diagonals do NOT connect" {
    const alloc = std.testing.allocator;
    const grid = "10" ++ "01";
    try std.testing.expectEqual(@as(usize, 2), try countIslands(alloc, grid, 2, 2));
}

test "single row: alternating cells" {
    const alloc = std.testing.allocator;
    try std.testing.expectEqual(@as(usize, 4), try countIslands(alloc, "1010101", 1, 7));
}

test "empty grid (0x0) → 0" {
    const alloc = std.testing.allocator;
    try std.testing.expectEqual(@as(usize, 0), try countIslands(alloc, "", 0, 0));
}

test "stress: random grids match independent flood-fill oracle" {
    var prng = std.Random.DefaultPrng.init(0x15AA1D19);
    const r = prng.random();
    const alloc = std.testing.allocator;

    var round: usize = 0;
    while (round < 40) : (round += 1) {
        const rows = r.intRangeAtMost(usize, 1, 12);
        const cols = r.intRangeAtMost(usize, 1, 12);
        const grid = try alloc.alloc(u8, rows * cols);
        defer alloc.free(grid);
        for (grid) |*cell| {
            cell.* = if (r.intRangeAtMost(u8, 0, 9) < 5) '1' else '0';
        }

        const want = try oracleIslands(alloc, grid, rows, cols);
        const got = try countIslands(alloc, grid, rows, cols);
        try std.testing.expectEqual(want, got);

        // Relationship: island count never exceeds the number of '1' cells.
        const ones = std.mem.count(u8, grid, "1");
        try std.testing.expect(got <= ones);
    }
}
