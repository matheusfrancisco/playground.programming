(ns tree.tree)

(defn node [value left right]
  {:value value
   :left left
   :right right})

(defn binary-tree [root-value]
  (node root-value nil nil))

#_(defn binary-tree-list [x]
    (list (* 2 x) (+ 1 (* 2 x))))

;"simple we are inserting to left and then to the right"
; a bad way to insert a value in a tree
#_(defn insert [tree value]
    (let [node (node value nil nil)]
      (cond
        (nil? (:left tree)) (assoc tree :left node)
        (nil? (:right tree)) (assoc tree :right node)
        :else (let [left (insert (:left tree) value)
                    branch (if (nil? left)
                             (insert (:right tree) value)
                             left)]
                (assoc tree
                       (if (nil? left)
                         :right
                         :left)
                       branch)))))

; binary-search-tree
(defn bst-insert [root value]
  (let [tree (cond
               (= root nil) (node value nil nil)
               (> value (:value root))  (-> root
                                            (assoc :left (bst-insert (:left root) value)))
               (< value (:value root))   (-> root
                                             (assoc :right (bst-insert (:right root) value))))]
    tree))

(def tree
  (-> (binary-tree 5)
      (bst-insert  3)
      (bst-insert  7)
      (bst-insert  2)))

(defn print-tree [tree]
  (let [e (tree :value)]))

(print-tree tree)
