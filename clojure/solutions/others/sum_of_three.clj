(ns others.sum-of-three
  (:require
   [clojure.test :refer [deftest is testing]]))

(defn two-sum-hash
  [inputs target]
  (loop [l  inputs
         seen #{}]
    (when-let [curr (first l)]
      (if-let [_ (seen (- target curr))]
        [curr (- target curr)]
        (recur (rest l) (conj seen curr))))))

(defn three-sum [target nums]
  (letfn [(search [x]
            (when-let [yz (two-sum-hash (rest nums) #_(sort (rest nums))
                                        (- target x))]
              (conj yz x)))]
    (some search nums)))

;;two pointer approach with sorted array
(defn two-sum [nums
               start
               end
               target]
  (loop [low start
         high end]
    (cond
      (< high low) false
      :else (let [sum (+ (nth nums low) (nth nums high))]
              (cond
                (= sum target) true
                (< sum target) (recur (inc low) high)
                (> sum target) (recur low (dec high)))))))

;; using two pointer approach
(defn find-triplet [arr target]
  (let [sorted-arr (sort arr)]
    (loop [i 0]
      (if (>= i (- (count sorted-arr) 2))
        false
        (if (two-sum sorted-arr
                     (inc i)
                     (dec (count sorted-arr))
                     (- target (nth sorted-arr i)))
          true
          (recur (inc i)))))))

(deftest test-sum
  (testing "sum"
    (is (= true (find-triplet [1 2 3] 6)))
    (is (= true (find-triplet [2 3 4 5 6] 10)))
    (is (= true (two-sum [1 2 3] 0 2 3)))
    (is (= (sort [5 4 1]) (sort (three-sum 10 [5 4 3 4 1]))))
    (is (= [2 1] (two-sum-hash [1 2 3] 3)))))
