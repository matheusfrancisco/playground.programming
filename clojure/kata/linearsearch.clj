(ns linearsearch)

(defn lookup [xs e]
  (loop [col xs]
    (if (empty? col)
      nil
      (if (= (first col) e)
        (first col)
        (recur (rest col))))))

(defn lookup2 [xs e]
  (loop [xs xs]
    (if (= (first xs) e)
      true
      (if (seq (rest xs))
        (recur (rest xs))
        false))))

(defn lookup3 [xs e]
  (or false
      (loop [xs xs]
        (when-let [x (first xs)]
          (if (= x e)
            x
            (recur (rest xs)))))))

(lookup3 [1 2 3 4 5] 3)
(lookup [1 2 3 4 5] 33)
(lookup [1 2 3 4 5] 3)
