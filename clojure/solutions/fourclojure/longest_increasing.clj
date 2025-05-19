(ns fourclojure.longest_increasing
  (:require
   [clojure.repl :refer [doc]]))

(defn lis2 [nums]
  (let [n (count nums)
        dp (atom (vec (repeat n 1)))]
    (doseq [i (range (dec n) -1 -1)
            j (range (inc i) n)]
      (when (< (nth nums i) (nth nums j))
        (swap! dp update i #(max % (inc (nth @dp j))))))
    (apply max @dp)))

(lis2 [1 2 3 1 2 3 4])
; i j
; i  j 
; i   j 

;      *ij
#_(= (lis [1 0 1 2 3 0 4 5]) [0 1 2 3])

(defn lis [nums]
  (let [n (count nums)
        lis (atom (vec (repeat n 1)))
        indices (atom (vec (repeat n nil)))]
    (doseq [i (range (dec n) -1 -1)
            j (range (inc i) n)]
      (when (< (nth nums i) (nth nums j))
        (when (>= (inc (nth @lis j)) (nth @lis i))
          (swap! lis update i #(max % (inc (nth @lis j))))
          (swap! indices assoc i j))))
    (loop [seq []
           curr (reduce-kv (fn [m k v]
                             (if (> v (get m 1 0))
                               [k v]
                               m))
                           [0 (nth @lis 0)]
                           @lis)
           idx (first curr)]
      (if (nil? idx)
        seq
        (recur (conj seq (nth nums idx))
               curr
               (nth @indices idx))))))
;;0 1 2 3
;;[1 2 3 4]
;;0      1       2   3
;;1 2 3   2 3 4   3
;;1
;;2 3
;;

(lis [1 0 1 2 3 0 4 5])
(lis [1 0 1 2 3 0 4 5])
(lis [1 2 3 1 1 2 3 4])

;"""
(defn lis3 [nums]
  (loop [start nums
         out []]
    (let [f (first start)
          s (second start)]
      (if (and s (< f s))
        (recur (rest start) (conj out f))
        (conj out f)))))

;Given a vector of integers, find the longest consecutive sub-sequence of increasing numbers. 
;If two sub-sequences have the same length, use the one that occurs first. An increasing sub-sequence must 
;have a length of 2 or greater to qualify.

(lis3 [1 2 3])
(lis3 [1 2 3 1])
(lis3 [1 2 3 1 4])
(lis3 [1 2 1])

(apply
 max-key
 count
 (loop [s [1 2 1 1 2 3]
        out []]
   (if (seq s)
     (recur
      (rest s)
      (conj out (lis3 s)))
     out)))

;[[1 2] [2] [1] [1 2 3] [2 3] [3]]



(defn largest-sub-seq [inseq]
  (loop [pending (rest inseq)
         candidate (list (first inseq)) ret '()]
    (if (seq pending)
      (let [this-candidate (if (> (first pending)
                                  (first candidate))
                             (conj candidate (first pending))
                             (list (first pending)))
            this-ret (if (> (count this-candidate)
                            (count ret))
                       this-candidate
                       ret)]
        (recur (rest pending)
               this-candidate
               this-ret))
      (reverse ret))))

