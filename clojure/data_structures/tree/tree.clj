(ns tree.tree)

(defn node [value left right]
  {:value value
   :left left
   :right right})

(defn binary-tree [root-value]
  (node root-value nil nil))

; binary-search-tree
(defn bst-insert [new-value tree]
  (cond
    (nil? tree) (binary-tree new-value)
    (<= new-value (:value tree)) (assoc tree :left (bst-insert new-value (:left tree)))
    :else (assoc tree :right (bst-insert new-value (:right tree)))))

(def tree
  (-> (binary-tree 50)
      (bst-insert  30)
      (bst-insert  20)
      (bst-insert  40)
      (bst-insert  70)
      (bst-insert  60)
      (bst-insert  80)))

(defn pre-order [tree]
  (when tree
    (do
      (print (str " " (:value tree)))
      (pre-order (:left tree))
      (pre-order (:right tree)))))

(defn inorder [tree]
  (when tree
    (do
      (inorder (:left tree))
      (print (str " " (:value tree)))
      (inorder (:right tree)))))

(inorder tree)
