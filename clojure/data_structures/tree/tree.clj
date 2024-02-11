(ns tree.tree)

(defn node [value left right]
  {:value value
   :left left
   :right right})

(defn binary-tree [root-value]
  (node root-value nil nil))

#_(defn binary-tree-list [x]
    (list (* 2 x) (+ 1 (* 2 x))))

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

(defn pre-order [tree]
  (when tree
    (do
      (print (str " " (:value tree)))
      (pre-order (:left tree))
      (pre-order (:right tree)))))

(pre-order tree)
