//! Max depth of a binary tree is the longest root-to-leaf path. Given a binary
//! tree, find its max depth. The length of a path is the number of EDGES on
//! that path, NOT the number of nodes (the study page is explicit about this).
//!
//! Example (mirrors the study page's 3-level tree): a root with two children,
//! where one child has two children of its own → max depth 2.
//!
//! Convention here: empty tree → 0, single node → 0 (zero edges).
//!
//! Requirements
//! - O(n) time (visit each node once), O(h) space for the recursion stack.
//! - No allocation needed for the recursive solution.
//!

const std = @import("std");

pub const TreeNode = struct {
    val: i32,
    left: ?*TreeNode = null,
    right: ?*TreeNode = null,
};

/// Return the number of edges on the longest root-to-leaf path.
/// Empty tree → 0. Single node → 0.
pub fn maxDepth(root: ?*const TreeNode) usize {
    const h = struct {
        pub fn helper(node: ?*const TreeNode) usize {
            const n = node orelse return 0;
            const left_depth = helper(n.left);
            const right_depth = helper(n.right);
            //return std.math.max(left_depth, right_depth) + 1;
            return @max(left_depth, right_depth) + 1;
        }
    }.helper;
    const edges = h(root);
    return if (edges > 0) edges - 1 else 0;
}

/// Build a tree from a level-order array where `null` marks a missing child.
/// Children slots are only consumed for nodes that exist (LeetCode-style).
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

/// Insert n nodes at random positions — used by the stress test.
fn buildRandomTree(alloc: std.mem.Allocator, r: std.Random, n: usize) !?*TreeNode {
    var root: ?*TreeNode = null;
    var count: usize = 0;
    while (count < n) : (count += 1) {
        const node = try alloc.create(TreeNode);
        node.* = .{ .val = r.intRangeAtMost(i32, -50, 50) };
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

// ── Test-only oracle: iterative BFS level count (independent of your DFS) ──

fn oracleDepthEdges(alloc: std.mem.Allocator, root: ?*TreeNode) !usize {
    const r = root orelse return 0;
    var q: std.ArrayList(*TreeNode) = .empty;
    defer q.deinit(alloc);
    try q.append(alloc, r);
    var head: usize = 0;
    var levels: usize = 0;
    while (head < q.items.len) {
        const level_end = q.items.len;
        levels += 1;
        while (head < level_end) : (head += 1) {
            const node = q.items[head];
            if (node.left) |l| try q.append(alloc, l);
            if (node.right) |rt| try q.append(alloc, rt);
        }
    }
    return levels - 1;
}

// ── Tests (the spec) ────────────────────────────────────────────────────────

test "example from the study page: 3-level tree has depth 2 (edges)" {
    const alloc = std.testing.allocator;
    const root = try buildTree(alloc, &[_]?i32{ 1, 2, 3, null, null, 4, 5 });
    defer freeTree(alloc, root);
    try std.testing.expectEqual(@as(usize, 2), maxDepth(root));
}

test "empty tree and single node both have depth 0" {
    const alloc = std.testing.allocator;
    try std.testing.expectEqual(@as(usize, 0), maxDepth(null));
    const one = try buildTree(alloc, &[_]?i32{42});
    defer freeTree(alloc, one);
    try std.testing.expectEqual(@as(usize, 0), maxDepth(one));
}

test "degenerate left-leaning tree: depth == node count - 1" {
    const alloc = std.testing.allocator;
    // 5 → 4 → 3 all via left children.
    const root = try buildTree(alloc, &[_]?i32{ 5, 4, null, 3, null });
    defer freeTree(alloc, root);
    try std.testing.expectEqual(@as(usize, 2), maxDepth(root));
}

test "stress: matches BFS level-count oracle on random trees" {
    var prng = std.Random.DefaultPrng.init(0xBEEF16);
    const r = prng.random();
    const alloc = std.testing.allocator;

    var round: usize = 0;
    while (round < 40) : (round += 1) {
        const n = r.intRangeAtMost(usize, 0, 60);
        const root = try buildRandomTree(alloc, r, n);
        defer freeTree(alloc, root);
        const want = try oracleDepthEdges(alloc, root);
        const got = maxDepth(root);
        try std.testing.expectEqual(want, got);
        // Sanity relationship: a tree with n nodes has depth < n.
        if (n > 0) try std.testing.expect(got < n);
    }
}
