//! The lowest common ancestor (LCA) of two nodes v and w in a tree is the
//! lowest (deepest) node that has both v and w as descendants  and each node
//! counts as a descendant of ITSELF, so a node directly connected to the other
//! is already the LCA. Node values are unique and both targets are guaranteed
//! to exist in the tree. Given the root and the two target VALUES p and q,
//! return the LCA node.
//!

const std = @import("std");

pub const TreeNode = struct {
    val: i32,
    left: ?*TreeNode = null,
    right: ?*TreeNode = null,
};

pub fn lowestCommonAncestor(root: ?*const TreeNode, p: i32, q: i32) ?*const TreeNode {
    const n = root orelse return null;

    if (n.val == p or n.val == q) return n;

    const l = lowestCommonAncestor(n.left, p, q);
    const r = lowestCommonAncestor(n.right, p, q);
    if (l != null and r != null) return n;
    return l orelse r;

    // for bst
    //if (root == null) return null;
    //var curr = root;
    //while (curr) |n| {
    //    if (p < n.val and q < n.val) {
    //        curr = n.left;
    //    } else if (p > n.val and q > n.val) {
    //        curr = n.right;
    //    } else {
    //        return n;
    //    }
    //}
    //return curr; // Should never happen if p and q are guaranteed to exist.
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

/// Insert n nodes at random positions with UNIQUE values 0..n-1 — used by the
/// stress test (LCA requires unique values).
fn buildRandomTree(alloc: std.mem.Allocator, r: std.Random, n: usize) !?*TreeNode {
    var root: ?*TreeNode = null;
    var count: usize = 0;
    while (count < n) : (count += 1) {
        const node = try alloc.create(TreeNode);
        node.* = .{ .val = @intCast(count) };
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

/// Find the node holding `target` (values are unique) — for pointer asserts.
fn findNode(node: ?*const TreeNode, target: i32) ?*const TreeNode {
    const n = node orelse return null;
    if (n.val == target) return n;
    return findNode(n.left, target) orelse findNode(n.right, target);
}

fn findPath(
    alloc: std.mem.Allocator,
    node: ?*const TreeNode,
    target: i32,
    path: *std.ArrayList(*const TreeNode),
) !bool {
    const n = node orelse return false;
    try path.append(alloc, n);
    if (n.val == target) return true;
    if (try findPath(alloc, n.left, target, path)) return true;
    if (try findPath(alloc, n.right, target, path)) return true;
    _ = path.pop();
    return false;
}

fn oracleLca(alloc: std.mem.Allocator, root: ?*const TreeNode, p: i32, q: i32) !?*const TreeNode {
    var path_p: std.ArrayList(*const TreeNode) = .empty;
    defer path_p.deinit(alloc);
    var path_q: std.ArrayList(*const TreeNode) = .empty;
    defer path_q.deinit(alloc);
    if (!try findPath(alloc, root, p, &path_p)) return null;
    if (!try findPath(alloc, root, q, &path_q)) return null;
    var ans: ?*const TreeNode = null;
    var i: usize = 0;
    while (i < path_p.items.len and i < path_q.items.len) : (i += 1) {
        if (path_p.items[i] != path_q.items[i]) break;
        ans = path_p.items[i];
    }
    return ans;
}

test "targets split across the root: LCA is where the paths diverge" {
    const alloc = std.testing.allocator;
    //         3
    //       /   \
    //      5     1
    //     / \   / \
    //    6   2 0   8
    //       / \
    //      7   4
    const root = try buildTree(alloc, &[_]?i32{ 3, 5, 1, 6, 2, 0, 8, null, null, 7, 4 });
    defer freeTree(alloc, root);
    // 5 and 1 sit in different subtrees of 3 → both sides non-null at 3.
    try std.testing.expectEqual(findNode(root, 3).?, lowestCommonAncestor(root, 5, 1).?);
    // 7 and 0 diverge at the root too.
    try std.testing.expectEqual(findNode(root, 3).?, lowestCommonAncestor(root, 7, 0).?);
    // 7 and 4 share parent 2.
    try std.testing.expectEqual(findNode(root, 2).?, lowestCommonAncestor(root, 7, 4).?);
}

test "a node is a descendant of itself: direct connection from the study page" {
    const alloc = std.testing.allocator;
    const root = try buildTree(alloc, &[_]?i32{ 3, 5, 1, 6, 2, 0, 8, null, null, 7, 4 });
    defer freeTree(alloc, root);
    // Example from the study page: when one target is directly connected to
    // the other, the upper one is already the LCA (a node is its own
    // descendant). 4 lives under 5 → LCA(5, 4) is node 5 itself.
    try std.testing.expectEqual(findNode(root, 5).?, lowestCommonAncestor(root, 5, 4).?);
    // p == q: the node is its own LCA.
    try std.testing.expectEqual(findNode(root, 6).?, lowestCommonAncestor(root, 6, 6).?);
}

test "single node and empty tree" {
    const alloc = std.testing.allocator;
    const one = try buildTree(alloc, &[_]?i32{42});
    defer freeTree(alloc, one);
    try std.testing.expectEqual(findNode(one, 42).?, lowestCommonAncestor(one, 42, 42).?);
    try std.testing.expectEqual(@as(?*const TreeNode, null), lowestCommonAncestor(null, 1, 2));
}

test "degenerate left-leaning chain: LCA is the shallower target" {
    const alloc = std.testing.allocator;
    // 5 → 4 → 3 → 2, all via left children: every node is an ancestor of the
    // ones below it, so the LCA of any pair is the shallower node.
    const root = try buildTree(alloc, &[_]?i32{ 5, 4, null, 3, null, 2, null });
    defer freeTree(alloc, root);
    try std.testing.expectEqual(findNode(root, 4).?, lowestCommonAncestor(root, 4, 2).?);
    try std.testing.expectEqual(findNode(root, 5).?, lowestCommonAncestor(root, 2, 5).?);
}

test "stress: matches the path-prefix oracle on random trees" {
    var prng = std.Random.DefaultPrng.init(0x1CA17B);
    const r = prng.random();
    const alloc = std.testing.allocator;

    var round: usize = 0;
    while (round < 40) : (round += 1) {
        const n = r.intRangeAtMost(usize, 1, 60);
        const root = try buildRandomTree(alloc, r, n);
        defer freeTree(alloc, root);
        var pair: usize = 0;
        while (pair < 8) : (pair += 1) {
            const p = r.intRangeAtMost(i32, 0, @intCast(n - 1));
            const q = r.intRangeAtMost(i32, 0, @intCast(n - 1));
            const want = (try oracleLca(alloc, root, p, q)).?;
            const got = lowestCommonAncestor(root, p, q).?;
            try std.testing.expectEqual(want, got);
        }
    }
}
