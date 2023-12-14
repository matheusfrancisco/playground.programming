(ns solutions.common.knapsack
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
  "Computes the maximum value that can be put in a knapsack of capacity W"
  [w weights values n]
  )


(println (= (knapsack 6 [1, 2, 3, 5] [1, 5, 4, 8] 4) 10))

#_(def k (knapsack 10 [10 20 30] [22 33 44] 3))
#_(clojure.pprint/pprint k)

#_(is (= (knapsack 10 [10 20 30] [22 33 44] 3) 30))


