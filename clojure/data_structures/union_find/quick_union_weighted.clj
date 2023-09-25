(ns union-find.quick-union-weighted)

(defprotocol IQuickUnion
  (root [this p])
  (is-connected? [this p q])
  (union [this p q])
  (print-arr [this]))

(deftype UnionFind [xs rank]
  IQuickUnion
  (root [_ p]
          (let [parent (get xs p)]
            (if (= parent p)
              p
              (recur parent))))

  #_(root [_ p]
    "Path compression: make every other node in path point to its grandparent"
    ; #TODO implement path compression
    ; kinda hard beacuse it requires mutable state
    )

  (is-connected? [this p q]
    (= (root this p) (root this q)))

  (union [this p q]
    (let [p-root (root this p)
          q-root (root this q)]
      (when (= p-root q-root)
        (UnionFind. xs rank))
      (if (< (get rank p-root) (get rank q-root))
        (let [n-xs (assoc xs p-root q-root)
              rank (assoc rank q-root (+ (get rank p-root) 
                                         (get rank q-root)))]
          (UnionFind. n-xs rank))
        (let [n-xs (assoc xs q-root p-root)
              rank (assoc rank p-root (+ (get rank p-root) (get rank q-root)))]
          (UnionFind. n-xs rank)))))

  (print-arr [_]
    {:rank (mapv (fn [e] e) rank)
     :xs (mapv (fn [e] e) xs)})

  #_java.lang.Object
  #_(toString [this])

  ;
  )

(defn new-union-find [n]
  (UnionFind. (vec (range n)) (vec (repeat n 1))))

(comment
  (-> (new-union-find 10)
      (union 4 3)
      (union 3 8)
      (union 6 5)
      (union 9 4)
      (union 2 1)
      (union 5 0)
      (union 8 9)
      (union 7 2)
      (union 6 1)
      (union 7 3)
      (print-arr))

#_{:rank [1 1 3 1 4 1 10 1 1 1], 
 :xs [6 2 6 4 6 6 6 2 4 4]}
;[6 2 6 4 6 6 6 2 4 4]
  )


