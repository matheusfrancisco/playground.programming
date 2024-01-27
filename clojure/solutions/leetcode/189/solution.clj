(ns leetcode.189.solution)

(defn reverse [nums start end]
  (loop [nums nums
         start start
         end end]
    (if (>= start end)
      nums
      (let [tmp (nth nums start)
            aux (nth nums end)]
        (recur (->
                nums
                (assoc start aux)
                (assoc end tmp))
               (inc start)
               (dec end))))))

(=
 (reverse [1 2 3 4 5 6 7] 0 6)
 [7 6 5 4 3 2 1])

(=
 (reverse [1 2 3] 0 2)
 [3 2 1])

(defn rotate [nums k]
  (let [n (count nums)
        k (mod k n)]
    (-> nums
        (reverse 0 (dec n))
        (reverse 0 (- k 1))
        (reverse k (dec n)))))

(=
 (rotate [1 2 3 4 5 6 7] 3)
 [5 6 7 1 2 3 4])

(=
 (rotate [-1 -100 3 99] 2)
 [3 99 -1 -100])
