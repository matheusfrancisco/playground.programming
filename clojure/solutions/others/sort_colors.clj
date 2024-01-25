(ns others.sort-colors)

;; o(n)
;; space o(n)
(defn sort-colors [colors]
  (let [counts (reduce (fn [counts color]
                         (if (contains? counts color)
                           (update counts color inc)
                           (assoc counts color 1)))
                       {} colors)]

    (concat (repeat (counts 0) 0)
            (repeat (counts 1) 1)
            (repeat (counts 2) 2))))

(= (sort-colors [0 1 2 0 1 2 0 1 2])
   [0 0 0 1 1 1 2 2 2])
