(ns hackerrank.simple-array-sum.solution
  (:require
   [clojure.string :as string]))

(defn simple-array-sum [ar]
  (reduce + 0 ar))

(defn main []
  (let [_ (Integer/parseInt (read-line))
        arr (vec (map #(Integer/parseInt %) (clojure.string/split (clojure.string/trimr (read-line)) #" ")))]
    (simple-array-sum arr)))

(println (main))
