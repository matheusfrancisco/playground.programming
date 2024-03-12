(ns lecture-5.bst)

(defrecord Node [value left right])

(defn insert [tree value]
  (cond
    (nil? tree) (->Node value nil nil)
    (<= value (:value tree)) (assoc tree :left (insert (:left tree) value))
    :else (assoc tree :right (insert (:right tree) value))))

(defn min-tree [tree]
  (if (nil? (:left tree))
    tree
    (min-tree (:left tree))))

(defn search [t e]
  (cond
    (nil? t) nil
    (= e (:value t)) t
    (< e (:value t)) (search (:left t) e)
    :else (search (:right t) e)))

(defn search-1 [t e]
  (if (or (nil?  (:value t))
          (= e (:value t)))
    t
    (recur (if (< e (:value t))
             (:left t)
             (:right t)) e)))

(defn delete [tree element]
  (let [left (:left tree)
        right (:right tree)]
    (cond
      (nil? (:value tree)) nil
      (< element (:value tree)) (assoc tree :left (delete left element))
      (> element (:value tree)) (assoc tree :right (delete right element))
      (nil? left) right
      (nil? right) left
      :else (let [min (min-tree right)]
              (assoc tree :value (:value min) :right (delete right (:value min)))))))

(defn from-arr [[initial & rest-values]]
  (reduce #(insert %1 %2) (->Node initial nil nil) rest-values))

(def t (from-arr [5 2 6 1 10]))

#_{:val 5,
   :left {:val 2, :left {:val 1, :left nil, :right nil}, :right nil},
   :right {:val 6, :left nil, :right {:val 10, :left nil, :right nil}}}

;     5
;    / \
;   2   6
; /      \
;1       10
;
(delete t 10)
#_{:value 5,
   :left {:value 2, :left {:value 1, :left nil, :right nil}, :right nil},
   :right {:value 6, :left nil, :right nil}}

(def t1 (from-arr [5 2 6 1 10]))
(delete t1 5)

#_{:value 6,
   :left {:value 2, :left {:value 1, :left nil, :right nil}, :right nil},
   :right {:value 10, :left nil, :right nil}}

(def t2 (from-arr [5 2 6 1 10]))
#_(delete t2 6)

(search t2 10)
#_{:value 10, :left nil, :right nil}
(search-1 t2 10)
#_{:value 10, :left nil, :right nil}
(search-1 t2 6)
#_{:value 6, :left nil, :right {:value 10, :left nil, :right nil}}
