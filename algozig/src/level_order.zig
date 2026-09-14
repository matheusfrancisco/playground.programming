//! Problem
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
//! API: takes an allocator; returns an allocated slice of allocated slices.
//! Caller frees inner slices then the outer slice  use the provided
//! `freeLevels` helper (it is spec).
//!
//! Requirements
//! - O(n) time, O(w) queue space where w = max level width.
//!

const std = @import("std");

pub const TreeNode = struct {
    val: i32,
    left: ?*TreeNode = null,
    right: ?*TreeNode = null,
};

pub fn levelOrder(alloc: std.mem.Allocator, root: ?*const TreeNode) ![][]i32 {
    std.debug.print("levelOrder: root = {any}\n", .{root});
    if (root == null) return alloc.alloc([]i32, 0);
    //  [1]
    //  [2, 3]
    //  [4, 5]
    var q: std.ArrayList(*const TreeNode) = .empty;
    defer q.deinit(alloc);

    var out: std.ArrayList([]i32) = .empty;
    errdefer {
        for (out.items) |lvl| alloc.free(lvl);
        out.deinit(alloc);
    }

    if (root) |r| try q.append(alloc, r);

    var head: usize = 0;
    while (head < q.items.len) {
        const n = q.items.len - head;
        const level = try alloc.alloc(i32, n);
        errdefer alloc.free(level);

        for (0..n) |i| {
            const node = q.items[head + i];
            level[i] = node.val;
            if (node.left) |l| try q.append(alloc, l);
            if (node.right) |r| try q.append(alloc, r);
        }
        head += n;
        try out.append(alloc, level);
    }

    return out.toOwnedSlice(alloc);
}

/// Free the result of levelOrder (spec — matches its ownership contract).
pub fn freeLevels(alloc: std.mem.Allocator, levels: [][]i32) void {
    for (levels) |level| alloc.free(level);
    alloc.free(levels);
}

fn buildTree(alloc: std.mem.Allocator, level: []const ?i32) !?*TreeNode {
    if (level.len == 0 or level[0] == null) return null;
    var nodes: std.ArrayList(*TreeNode) = .empty;
    defer nodes.deinit(alloc);
    const root = try alloc.create(TreeNode);
    root.* = .{ .val = level[0].? };
    try nodes.append(alloc, root);
    var head: usize = 0;
    var i: usize = 1;
    while (i < level.len and head < nodes.items.len) : (head += 1) {
        const parent = nodes.items[head];
        if (level[i]) |v| {
            const n = try alloc.create(TreeNode);
            n.* = .{ .val = v };
            parent.left = n;
            try nodes.append(alloc, n);
        }
        i += 1;
        if (i >= level.len) break;
        if (level[i]) |v| {
            const n = try alloc.create(TreeNode);
            n.* = .{ .val = v };
            parent.right = n;
            try nodes.append(alloc, n);
        }
        i += 1;
    }
    return root;
}

fn freeTree(alloc: std.mem.Allocator, node: ?*TreeNode) void {
    const n = node orelse return;
    freeTree(alloc, n.left);
    freeTree(alloc, n.right);
    alloc.destroy(n);
}

fn buildRandomTree(alloc: std.mem.Allocator, r: std.Random, n: usize) !?*TreeNode {
    var root: ?*TreeNode = null;
    var count: usize = 0;
    while (count < n) : (count += 1) {
        const node = try alloc.create(TreeNode);
        node.* = .{ .val = @as(i32, @intCast(count)) }; // distinct values
        if (root == null) {
            root = node;
            continue;
        }
        var cur = root.?;
        while (true) {
            if (r.boolean()) {
                if (cur.left) |l| cur = l else {
                    cur.left = node;
                    break;
                }
            } else {
                if (cur.right) |rt| cur = rt else {
                    cur.right = node;
                    break;
                }
            }
        }
    }
    return root;
}

fn countNodes(node: ?*const TreeNode) usize {
    const n = node orelse return 0;
    return 1 + countNodes(n.left) + countNodes(n.right);
}

fn depthOfValue(node: ?*const TreeNode, val: i32, depth: usize) ?usize {
    const n = node orelse return null;
    if (n.val == val) return depth;
    if (depthOfValue(n.left, val, depth + 1)) |d| return d;
    return depthOfValue(n.right, val, depth + 1);
}

test "example from the study page: [[1],[2,3],[4,5]]" {
    const alloc = std.testing.allocator;
    const root = try buildTree(alloc, &[_]?i32{ 1, 2, 3, 4, 5 });
    defer freeTree(alloc, root);

    const levels = try levelOrder(alloc, root);
    defer freeLevels(alloc, levels);

    try std.testing.expectEqual(@as(usize, 3), levels.len);
    try std.testing.expectEqualSlices(i32, &[_]i32{1}, levels[0]);
    try std.testing.expectEqualSlices(i32, &[_]i32{ 2, 3 }, levels[1]);
    try std.testing.expectEqualSlices(i32, &[_]i32{ 4, 5 }, levels[2]);
}

test "empty tree → empty outer slice" {
    const alloc = std.testing.allocator;
    const levels = try levelOrder(alloc, null);
    defer freeLevels(alloc, levels);
    try std.testing.expectEqual(@as(usize, 0), levels.len);
}

test "single node and missing children keep left-to-right order" {
    const alloc = std.testing.allocator;
    // 1 has only a right child 3, which has only a left child 4.
    const root = try buildTree(alloc, &[_]?i32{ 1, null, 3, 4, null });
    defer freeTree(alloc, root);

    const levels = try levelOrder(alloc, root);
    defer freeLevels(alloc, levels);

    try std.testing.expectEqual(@as(usize, 3), levels.len);
    try std.testing.expectEqualSlices(i32, &[_]i32{1}, levels[0]);
    try std.testing.expectEqualSlices(i32, &[_]i32{3}, levels[1]);
    try std.testing.expectEqualSlices(i32, &[_]i32{4}, levels[2]);
}

test "stress: every value lands on the level equal to its depth" {
    var prng = std.Random.DefaultPrng.init(0xD00D18);
    const r = prng.random();
    const alloc = std.testing.allocator;

    var round: usize = 0;
    while (round < 25) : (round += 1) {
        const n = r.intRangeAtMost(usize, 1, 50);
        const root = try buildRandomTree(alloc, r, n);
        defer freeTree(alloc, root);

        const levels = try levelOrder(alloc, root);
        defer freeLevels(alloc, levels);

        // Total emitted values equals node count.
        var total: usize = 0;
        for (levels) |level| {
            try std.testing.expect(level.len > 0); // no empty levels
            total += level.len;
        }
        try std.testing.expectEqual(countNodes(root), total);

        // Each value appears on the level matching its true depth.
        for (levels, 0..) |level, li| {
            for (level) |v| {
                try std.testing.expectEqual(@as(?usize, li), depthOfValue(root, v, 0));
            }
        }
    }
}
