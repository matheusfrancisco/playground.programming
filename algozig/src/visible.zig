//! In a binary tree, a node is "visible" if on the path from the root to that
//! node there isn't any node with a value STRICTLY higher than this node's
//! value (ties are fine: 8 stays visible even after passing another 8).
//! The root is always visible. Count the visible nodes.
//!
//! Example (mirrors the study page): tree
//!         5
//!        / \
//!       4   6
//!      / \
//!     3   8
//! Output: 3. Node 4 is not visible (5>4), node 3 is not visible (5>3, 4>3),
//! node 8 is visible (5<=8, 4<=8, 8<=8). Visible: {5, 6, 8}.
//!
//! Requirements
//! - O(n) time, O(h) recursion space. No allocation.
//!

const std = @import("std");

pub const TreeNode = struct {
    val: i32,
    left: ?*TreeNode = null,
    right: ?*TreeNode = null,
};

/// Count nodes with no strictly-greater ancestor on their root path.
pub fn countVisible(root: ?*const TreeNode) usize {
    const count = struct {
        pub fn helper(node: ?*const TreeNode, max_so_far: ?i32) usize {
            const n = node orelse return 0;
            const visible = max_so_far == null or n.val >= max_so_far.?;
            const new_max: i32 = if (max_so_far) |m| @max(m, n.val) else n.val;
            return @as(usize, @intFromBool(visible)) +
                helper(n.left, new_max) + helper(n.right, new_max);
        }
    }.helper;
    return count(root, null);
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
        node.* = .{ .val = r.intRangeAtMost(i32, -20, 20) };
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

fn oracleCount(node: ?*const TreeNode, max_so_far: ?i32) usize {
    const n = node orelse return 0;
    const visible = max_so_far == null or n.val >= max_so_far.?;
    const new_max: i32 = if (max_so_far) |m| @max(m, n.val) else n.val;
    return @as(usize, @intFromBool(visible)) +
        oracleCount(n.left, new_max) + oracleCount(n.right, new_max);
}

test "example from the study page: answer is 3" {
    const alloc = std.testing.allocator;
    const root = try buildTree(alloc, &[_]?i32{ 5, 4, 6, 3, 8 });
    defer freeTree(alloc, root);
    try std.testing.expectEqual(@as(usize, 3), countVisible(root));
}

test "empty tree → 0; single node (root) is always visible" {
    const alloc = std.testing.allocator;
    try std.testing.expectEqual(@as(usize, 0), countVisible(null));
    const one = try buildTree(alloc, &[_]?i32{-7});
    defer freeTree(alloc, one);
    try std.testing.expectEqual(@as(usize, 1), countVisible(one));
}

test "ties count as visible: equal values down a chain" {
    const alloc = std.testing.allocator;
    // 5 → 5 → 5 down the left spine: all three visible.
    const root = try buildTree(alloc, &[_]?i32{ 5, 5, null, 5, null });
    defer freeTree(alloc, root);
    try std.testing.expectEqual(@as(usize, 3), countVisible(root));
}

test "strictly decreasing chain: only the root is visible" {
    const alloc = std.testing.allocator;
    const root = try buildTree(alloc, &[_]?i32{ 9, 8, null, 7, null });
    defer freeTree(alloc, root);
    try std.testing.expectEqual(@as(usize, 1), countVisible(root));
}

test "stress: matches path-max oracle; count bounded by [1, n]" {
    var prng = std.Random.DefaultPrng.init(0xCAFE17);
    const r = prng.random();
    const alloc = std.testing.allocator;

    var round: usize = 0;
    while (round < 40) : (round += 1) {
        const n = r.intRangeAtMost(usize, 1, 80);
        const root = try buildRandomTree(alloc, r, n);
        defer freeTree(alloc, root);
        const got = countVisible(root);
        try std.testing.expectEqual(oracleCount(root, null), got);
        try std.testing.expect(got >= 1 and got <= n);
    }
}
