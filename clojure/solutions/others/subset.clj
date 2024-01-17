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

(defn subset-sum [arr, total]
  (let [dp (make-dp-reduce-map (inc total) (inc (count arr)))]
    (loop [i 1
           mdp dp]
      (if (= i (inc (count arr)))
        mdp
        (recur (inc i)
               (loop [j 1
                      ndp mdp]
                 (let [v (get arr (dec i))
                       ndp (if (> v  j)
                             (change-dp ndp i j (get-in ndp [(dec i) j]))
                             (change-dp ndp i j (or (get-in ndp [(dec i) j])
                                                    (get-in ndp [(dec i) (- j v)]))))]
                   (recur (inc j) ndp))))))))

(subset-sum [1, 2, 3 ,4], 6)
(= (subset-sum [1, 2, 3 ,4], 6) true)

#_(defn subset-sum-01
    [ttl [item & items]]
    (cond
      (zero? ttl) [[]]
      (or (neg? ttl) (nil? item)) []
      :else (concat
             (map #(conj % item) (subset-sum-01 (- ttl item) items))
             (subset-sum-01 ttl items))))

#_(subset-sum-01 6 [1 2 2 3 3])
