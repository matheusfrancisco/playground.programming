(ns solutions.others.knapsack
  (:require
   [clojure.test :refer [is]]))

;https://www.youtube.com/watch?v=xCbYmUPvc2Q&list=PLiQ766zSC5jM2OKVr8sooOuGgZkvnOCTI&index=21&pp=iAQB

; trying to do without mutability with mutability it will be mucher easier
#_(defn doseq-forr [n capacity f dp]
    (doseq [i (range n)
            j (range capacity)]
      (f i j dp)))

#_(defn loop-recur [n k f dp]
    (loop [i 0]
      (when (< i n)
        (loop [j 0]
          (when (< j k)
            (f i j dp)
            (recur (inc j))))
        (recur (inc i)))))

(defn knapsack
  "this is a dynamic programming solution to the knapsack problem
   it takes a capacity and a list of weights and a list of values
   and returns the maximum value that can be carried in the knapsack
   with the given capacity
   it has more additional time complexity then usual
   O(nm) time and O(nm) space
   wher n is the number of items and m is the capacity
   "
  [k weights values n]

  (let [values (reduce
                (fn [dp i]
                  (reduce
                   (fn [acc j]
                     (cond
                       (or (= i 0)
                           (= j 0)) (assoc-in acc [i j] 0)
                       (<= (get-in weights [(- i 1)])  j)
                       (let [max-value (max
                                        (+
                                         (get-in values [(- i 1)])
                                         (get-in acc
                                                 [(- i 1)
                                                  (- j (get weights
                                                            (- i 1)))]))
                                        (get-in acc [(dec i) j]))
                             acc (assoc-in acc [i j] max-value)]
                         acc)
                       :else (assoc-in acc [i j] (get-in acc [(- i 1) j]))))
                   dp (range (inc k))))
                (vec (repeat (inc n) (vec (repeat (+ 1 k) 0))))
                (range (inc n)))]
    (get-in values [n k])))

(defn
  ^{:doc "knapsack time: o(nm) "}
  knapsack-topdown
  [k weights values i]
  (let [lookup {}
        value  (cond
                 (contains? lookup [i k]) (let [v (get lookup [i k])]  v)
                 (or (= i (count values)) (<= k 0)) 0
                 (>  (get weights i) k) (let [v (first (knapsack-topdown k weights values (inc i)))]
                                          v)
                 :else (let [v (max
                                (+ (first (knapsack-topdown (- k (get weights i)) weights values (inc i))) (get values i))
                                (first (knapsack-topdown k weights values (inc i))))]
                         v))]

    [value (assoc lookup [i k] value)]))

(is (= (first (knapsack-topdown 6  [1, 2, 3, 5] [1, 5, 4, 8] 0)) 10))
(is (= (knapsack 6 [1, 2, 3, 5] [1, 5, 4, 8] 4) 10))
(is (= (knapsack 10 [10 20 30] [22 33 44] 3) 22))


