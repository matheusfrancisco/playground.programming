(ns lecture-6.avl2
  (:require
   [clojure.string :as string]))

(defn height
  "Returns height of the given tree"
  ([tree] (height tree 0))
  ([tree count]
   (if tree
     (max (height (:left tree) (inc count))
          (height (:right tree) (inc count)))
     count)))

(defn factor
  "Returns the balance factor of root node of the given tree"
  [{:keys [left right]}]
  (- (height left) (height right)))

(defn is-left-case?
  "Returns true if left subtree is imbalanced else false"
  [tree]
  (> (factor tree) 1))

(defn is-right-case?
  "Returns true if right sub tree is imbalanced else false"
  [tree]
  (< (factor tree) -1))

(defn is-left-right-case?
  "Returns true if right sub tree of left child is imbalanced else false"
  [tree]
  (and (is-left-case? tree) (< (factor (:left tree)) 0)))

(defn is-left-left-case?
  "Returns true if left sub tree of left child is imbalanced else false"
  [tree]
  (and (is-left-case? tree) (> (factor (:left tree)) 0)))

(defn is-right-right-case?
  "Returns true if right sub tree of right child is imbalanced else false"
  [tree]
  (and (is-right-case? tree) (< (factor (:right tree)) 0)))

(defn is-right-left-case?
  "Returns true if right sub tree of left child is imbalanced else false"
  [tree]
  (and (is-right-case? tree) (> (factor (:right tree)) 0)))

(defn rotate-left
  "Returns the left rotated tree "
  [{:keys [root left right]}]
  (let [pivot (:root right)
        left-pivot (:left right)
        right-pivot (:right right)]
    {:root pivot
     :left {:root root
            :left left
            :right left-pivot}
     :right right-pivot}))

(defn rotate-right
  "Returns the right rotated tree"
  [{:keys [root left right]}]
  (let [pivot (:root left)
        left-pivot (:left left)
        right-pivot (:right left)]
    {:root pivot
     :left left-pivot
     :right {:root root
             :left right-pivot
             :right right}}))

(defn balance
  "Returns a balanced bst"
  [{:keys [left right] :as tree}]
  (cond
    (is-right-left-case? tree) (rotate-left
                                (assoc tree :right (rotate-right right)))

    (is-left-right-case? tree) (rotate-right
                                (assoc tree :left (rotate-left left)))

    (is-right-right-case? tree) (rotate-left tree)

    (is-left-left-case? tree) (rotate-right tree)

    :else tree))

(defn insert-node
  "Returns a bst after inserting a new node"
  [{:keys [root] :as tree} value]
  (cond
    (nil? root) {:root value :left nil :right nil}
    (neg? (compare value root)) (balance
                                 (update tree :left insert-node value))
    (pos? (compare value root)) (balance
                                 (update tree :right insert-node value))
    :else tree))

(defn create-bst
  "Returns a bst when given a list of node values "
  [values]
  (reduce insert-node {} values))

(defn has?
  "Returns true if if a given integer is present in the tree else false"
  [{:keys [root left right]} value]
  (cond
    (nil? root) false
    (= value root) true
    (neg? (compare value root)) (has? left value)
    :else (has? right value)))

(defn min-node
  "Find the minimun value in a given tree"
  [{:keys [root left] :as tree}]
  (cond
    (nil? tree) nil
    (nil? left) root
    :else (min-node left)))

(defn remove-node
  "Returns a tree after removing the given node from the given tree"
  [{:keys [root left right] :as tree} value]
  (cond
    (nil? tree) nil
    (neg? (compare value root)) (update tree :left remove-node value)
    (pos? (compare value root)) (update tree :right remove-node value)
    (nil? left) right
    (nil? right) left
    :else (let [min (min-node right)]
            (-> (update tree :right remove-node min)
                (assoc :root min)))))

(defn read-file
  "Returns a vector containing all the words in a file"
  [file-path]
  (let [content (slurp file-path)]
    (string/split content #" ")))

(defn count-nodes
  "Returns the number of nodes in a tree"
  [{:keys [left right] :as tree}]
  (if tree
    (+ 1 (count left) (count right))
    0))

(defn tabs [n]
  (string/join (repeat n "\t")))

(defn visualise
  ([tree] (visualise tree 0))
  ([{:keys [el left right] :as tree} depth]
   (if tree
     (str (visualise right (inc depth)) (tabs depth) el "\n" (visualise left (inc depth)))
     (str (tabs depth) "~\n"))))

(create-bst '(1 2 3))
