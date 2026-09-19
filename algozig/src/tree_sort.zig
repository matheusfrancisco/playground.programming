const std = @import("std");
const mem = std.mem;

fn TreeNode(comptime T: type) type {
    return struct {
        val: T,
        left: ?*TreeNode(T) = null,
        right: ?*TreeNode(T) = null,
    };
}

fn freeTree(alloc: std.mem.Allocator, node: ?*TreeNode(i32)) void {
    const n = node orelse return;
    freeTree(alloc, n.left);
    freeTree(alloc, n.right);
    alloc.destroy(n);
}

fn checkHeight(node: ?*const TreeNode(i32)) ?i64 {
    const n = node orelse return -1;
    const l = checkHeight(n.left) orelse return null;
    const r = checkHeight(n.right) orelse return null;
    if (@max(l, r) - @min(l, r) > 1) return null;
    return 1 + @max(l, r);
}

pub fn isBalanced(root: ?*const TreeNode(i32)) bool {
    // binary tree is balanced if for every
    // node in the tree, thed diff in the height of
    // its left and right subtrees is at most 1.
    return checkHeight(root) != null;
}

fn buildTree(alloc: std.mem.Allocator, level: []const ?i32) !?*TreeNode(i32) {
    if (level.len == 0) return null;
    var nodes: std.ArrayList(?*TreeNode(i32)) = .empty;
    defer nodes.deinit(alloc);
    const root = try alloc.create(TreeNode(i32));
    root.* = .{ .val = level[0].? };
    try nodes.append(alloc, root);
    var head: usize = 0;
    var i: usize = 1;
    while (i < level.len and head < nodes.items.len) : (head += 1) {
        const parent = nodes.items[head].?;
        if (level[i]) |v| {
            const n = try alloc.create(TreeNode(i32));
            n.* = .{ .val = v };
            parent.left = n;
            try nodes.append(alloc, n);
        }
        i += 1;
        if (i >= level.len) break;
        if (level[i]) |v| {
            const n = try alloc.create(TreeNode(i32));
            n.* = .{ .val = v };
            parent.right = n;
            try nodes.append(alloc, n);
        }
        i += 1;
    }

    return root;
}

test "example from the study page: full 2-level tree is balanced" {
    const alloc = std.testing.allocator;
    const root = try buildTree(alloc, &[_]?i32{ 1, 2, 3, 4, 5, 6, 7 });
    defer freeTree(alloc, root);
    try std.testing.expect(isBalanced(root));
}

test "example from the study page: node 3 with empty left and height-2 right is not balanced" {
    const alloc = std.testing.allocator;
    // 1 → (3, 2); 3 has only a right child 4, which has only a right child 5.
    // At node 3: right height 2, left height -1 → difference 3.
    const root = try buildTree(alloc, &[_]?i32{ 1, 3, 2, null, 4, null, null, null, 5 });
    defer freeTree(alloc, root);
    try std.testing.expect(!isBalanced(root));
}

test "empty tree, single node, and two-node tree are all balanced" {
    const alloc = std.testing.allocator;
    try std.testing.expect(isBalanced(null));
    const one = try buildTree(alloc, &[_]?i32{42});
    defer freeTree(alloc, one);
    try std.testing.expect(isBalanced(one));
    const two = try buildTree(alloc, &[_]?i32{ 1, 2, null });
    defer freeTree(alloc, two);
    try std.testing.expect(isBalanced(two));
}

test "degenerate left-leaning chain of 3 nodes is not balanced" {
    const alloc = std.testing.allocator;
    // 5 → 4 → 3 all via left children: root's left height 1 vs right -1.
    const root = try buildTree(alloc, &[_]?i32{ 5, 4, null, 3, null });
    defer freeTree(alloc, root);
    try std.testing.expect(!isBalanced(root));
}

test "stress: matches the naive two-pass oracle on random trees" {
    var prng = std.Random.DefaultPrng.init(0xBA1A16A);
    const r = prng.random();
    const alloc = std.testing.allocator;

    var round: usize = 0;
    while (round < 60) : (round += 1) {
        const n = r.intRangeAtMost(usize, 0, 40);
        const root = try buildRandomTree(alloc, r, n);
        defer freeTree(alloc, root);
        const want = oracleBalanced(root);
        try std.testing.expectEqual(want, isBalanced(root));
        // Sanity: trees with fewer than 3 nodes are always balanced.
        if (n < 3) try std.testing.expect(want);
    }
}

fn oracleHeight(node: ?*const TreeNode(i32)) i64 {
    const n = node orelse return -1;
    return 1 + @max(oracleHeight(n.left), oracleHeight(n.right));
}

fn oracleBalanced(node: ?*const TreeNode(i32)) bool {
    const n = node orelse return true;
    const diff = oracleHeight(n.left) - oracleHeight(n.right);
    if (diff > 1 or diff < -1) return false;
    return oracleBalanced(n.left) and oracleBalanced(n.right);
}

fn buildRandomTree(alloc: std.mem.Allocator, r: std.Random, n: usize) !?*TreeNode(i32) {
    var root: ?*TreeNode(i32) = null;
    var count: usize = 0;
    while (count < n) : (count += 1) {
        const node = try alloc.create(TreeNode(i32));
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
