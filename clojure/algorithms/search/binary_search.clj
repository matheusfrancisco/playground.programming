(ns search.binary-search
  (:require
   [clojure.math :as math]))

(defn binary-search
  ([arr n]
   (let [lo 0
         hi (count arr)]
     (binary-search arr n lo hi)))
  ([arr n lo hi]
   (let [mid (int (math/floor (/ (+  lo (- hi lo)) 2)))]
     (cond
       (>= lo hi) -1
       (> (arr mid) n) (binary-search arr n (inc mid) hi)
       (< (arr mid) n) (binary-search arr n lo mid)
       (= (arr mid) n) [mid, n]
       :else -1))))

(= (binary-search [1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20] 11) [10 11])
