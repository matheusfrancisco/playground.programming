(ns others.subset)

(defn make-dp-reduce-map [n m]
  (reduce (fn [dp _]
            (let [row  (mapv (fn [v]
                               (if (= v 0)
                                 true
                                 false)) (range (inc m)))]
              (conj dp row))) [] (range (inc n))))

(defn make-dp-loop [n m]
  (loop [i 0
         dp []]
    (if (= i (inc n))
      dp
      (let [arow
            (loop [row  []
                   j 0]
              (if (= j (inc m))
                row
                (let [r (if (= j 0)
                          (conj row true)
                          (conj row false))]
                  (recur r (inc j)))))]
        (recur (inc i) (conj dp arow))))))

(defn change-dp
  [dp i j v]
  (update-in dp [i j] (fn [_] v)))

;; this it uses the bottom up approach to solve the problem of dp
(defn subset-sum [arr, total]
  (let [dp (make-dp-reduce-map (inc total) (inc (count arr)))]
    (get-in (loop [i 1
                   matrix-dp dp]
              (if (= i (inc (count arr)))
                matrix-dp
                (recur (inc i)
                       (loop [j 1
                              new-dp matrix-dp]
                         (if (= j (inc total))
                           new-dp
                           (let [v (get arr (dec i))
                                 ndp (if (> v  j)
                                       (change-dp new-dp i j (get-in new-dp [(dec i) j]))
                                       (change-dp new-dp i j (or (get-in new-dp [(dec i) j])
                                                                 (get-in new-dp [(dec i) (- j v)]))))]
                             (recur (inc j) ndp)))))))
            [(count arr) total])))

(= (subset-sum [1, 2, 3 ,4], 6) true)
