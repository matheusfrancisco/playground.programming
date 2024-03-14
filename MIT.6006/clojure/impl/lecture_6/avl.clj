(ns lecture-6.avl)

(defrecord Node [value left right bf height])

(defn height [node]
  (if (nil? node)
    0
    (:height node)))

(defn get-balance [node]
  (if (nil? node)
    0
    (- (height (:left node))
       (height (:right node)))))

(defn rotate-left [z]
  (let [y (:right z)
        t2 (:left y)
        y (assoc y :left (assoc z :right t2))
        y (assoc y :height (+ 1 (max (height (:left y))
                                     (height (:right y))))
                 :balance-factor (get-balance y))]
    y))

(defn rotate-right [z]
  (let [y (:left z)
        t3 (:right y)
        y (assoc y :right (assoc z :left t3))
        y (assoc y :height (+ 1 (max (height (:left y))
                                     (height (:right y))))
                 :balance-factor (get-balance y))]
    y))

(defn insert [node value]
  (let [tree (->
              (cond
                (nil? node) (Node. value nil nil 0 1)
                (< value (:value node)) (do
                                          (assoc node :left
                                                 (insert (:left node) value)
                                                 :height (+ 1 (max (height (:left node))
                                                                   (height (:right node))))
                                                 :balance-factor (get-balance node)))
                (> value (:value node)) (do
                                          (-> (assoc node
                                                     :right (insert (:right node) value)
                                                     :height (+ 1 (max (height (:left node))
                                                                       (height (:right node))))
                                                     :balance-factor (get-balance node))))))

        _d (prn tree)
        tree (assoc tree :height (+ 1 (max (height (:left tree))
                                           (height (:right tree))))
                    :balance-factor (get-balance tree))
        _d (prn tree)
        balance (get-balance tree)
        _ (prn balance value "<" (-> tree :right :value))
        tree (cond
               (and (> balance 1)
                    (> value (-> tree :left :value))) (do
                                                        (prn 22)
                                                        (-> (rotate-right tree)))

               (and (< balance -1)
                    true
                    #_(< value (-> tree :right :value))) (do
                                                           (prn 100)
                                                           (-> (rotate-left tree)
                                                               (rotate-left)))
               (and (> balance 1)
                    true
                    #_(< value (-> tree :right :value))) (do
                                                           (prn 10)
                                                           (rotate-right tree))
               :else tree)]

    (prn tree)
    tree))

(-> (insert nil 10)
    (insert 30)
    (insert 40))
