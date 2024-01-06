(ns sorting.quicksort
  (:refer-clojure :exclude [compare]))

;; |------------+-----------------+---------------+-------------|
;; | Algorithm  | Time complexity |               |             |
;; |            | Best cases      | Average cases | Worst cases |
;; |------------+-----------------+---------------+-------------|
;; | Quick Sort | O(n log(n))     | O(n log(n))   | O(n2)       |
;; |------------+-----------------+---------------+-------------|

(defn compare [f xs]
  (filter f xs))

(defn quicksort [xs]
  (let [pivot (last xs)
        lower (compare  #(<= % pivot) (butlast xs))
        higher (compare #(> % pivot) (butlast xs))]

    (if (empty? xs)
      xs
      (concat (quicksort lower)
              [pivot]
              (quicksort higher)))))

(= (quicksort [1 2 4 3 6 4 8 7 5])
   [1 2 3 4 4 5 6 7 8])

(= (quicksort [2 1]) [1 2])

(= (quicksort []) [])

