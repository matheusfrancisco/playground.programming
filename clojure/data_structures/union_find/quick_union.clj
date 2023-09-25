(ns union-find.quick-union)

(defprotocol IQuickUnion
  (root [this p])
  (is-connected? [this p q])
  (union [this p q])
  (print-arr [this]))

(deftype UnionFind [xs]
  IQuickUnion
  (root [this p]
    (let [parent (get xs p)]
      (if (= parent p)
        p
        (recur parent))))
  (is-connected? [this p q]
    (= (root this p) (root this q)))

  (union [this p q]
    "Time complexity: O(n) - worst case
    Change root of p to point to root of q."
    (let [p-root (root this p)
          q-root (root this q)]
      (UnionFind.
       (assoc xs p-root q-root))))

  (print-arr [this]
    (mapv (fn [e] e) xs))

  #_java.lang.Object
  #_(toString [this])

  ;
  )

(defn quick-find [n]
  (->UnionFind (vec (range n))))

(comment
  (-> (quick-find 10)
      (union 1 2)
      (is-connected? 1 2))
  ;=> true

  (-> (quick-find 10)
      (union 4 3)
      (union 3 8)
      (union 6 5)
      (union 9 4)
      (union 2 1)
      (union 5 0)
      (union 7 2)
      (union 6 1)
      (union 7 3)
      (print-arr))

  ;=> [1 8 1 8 3 0 5 1 8 8]

;
  )
