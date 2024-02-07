(ns sorting.bubble-sort)

(defn swap-items!  [arr i j]
  (let [temp (get arr i)]
    (assoc! arr i (get arr j))
    (assoc! arr j temp)))

(defn bubble-sort
  [arr]
  (when (not (= (type arr) clojure.lang.PersistentVector$TransientVector))
    (throw (IllegalArgumentException. "Input must be a transient vector.")))
  (loop [i 1
         modded false]
    (when (or (< i  (count arr)) modded)
      (cond
        (= i (count arr)) (recur 1 false)
        (< (get arr i) (get arr (dec i)))
        (do
          (swap-items! arr i (dec i))
          (recur (inc i) true))
        :else (recur (inc i) modded))))
  (persistent! arr))

(bubble-sort (transient [3 2 1 4 5 8 9 6]))
;[1 2 3 4 5 6 8 9]

(defn subvector
  "Returns a sub-vector v[i;j["
  [v i n]
  (cond (empty? v) []
        (< n 1) []
        (< i 0) []
        (< (count v) (+ i n)) []
        (= i 0) (vec (take n v))
        :else (recur (rest v) (dec i) n)))

; this can show use  modify the vector imutable is not a good idea
; for sorting algorithms since we will be creating a lot of new vectors
(defn swap
  "Swaps the two elements at position i and j in v."
  [v i j]
  (let [n (count v)]
    (cond (or (neg? i) (neg? j)) v
          (= i j) v
          (> i j) (recur v j i)
          (or (>= i n) (>= j n)) v
          :else
          (let [x (nth v i)
                y (nth v j)
                l (subvector v 0 i)
                m (subvector v (inc i) (dec (- j i)))
                r (subvector v (inc j) (dec (- n j)))]
            (vec (flatten [l [y] m [x] r]))))))

(defn bubble-sort-2
  ([arr]
   (let [n (count arr)]
     (if (<= n 1)
       arr
       (bubble-sort-2 arr n 0 (dec n)))))
  ([arr n i j]
   (cond
     (= i (dec n)) arr
     (= j i) (recur arr n (inc i) (dec n))
     :else (let [r (nth arr j)
                 l (nth arr (dec j))]
             (if (< r l)
               (recur (swap arr (dec j) j) n i (dec j))
               (recur arr n i (dec j)))))))

(bubble-sort-2 [3 2 1 4 5 8 9 6])
;[1 2 3 4 5 6 8 9]

;more simple swap
(defn swap-inplace [arr i j]
  (let [temp (get arr i)
        arr-temp (assoc arr i (get arr j))]
    (assoc arr-temp j temp)))

(swap-inplace [2 3] 0 1)
;[3 2]

(defn bubble-sort-3
  ([arr]
   (let [n (count arr)]
     (if (<= n 1)
       arr
       (bubble-sort-2 arr n 0 (dec n)))))
  ([arr n i j]
   (cond
     (= i (dec n)) arr
     (= j i) (recur arr n (inc i) (dec n))
     :else (let [r (nth arr j)
                 l (nth arr (dec j))]
             (if (< r l)
               (recur (swap-inplace arr (dec j) j) n i (dec j))
               (recur arr n i (dec j)))))))
(bubble-sort-3 [3 2 1 4 5 8 9 6])
;[1 2 3 4 5 6 8 9]
