(ns lecture-3.sorting
  (:require
   [matcher-combinators.test :refer [match?]]
   [clojure.test :refer [deftest is testing]]))

;; the designing of this sorting with imutable [] is not efficient
;; it will take O(n^2) time to sort the array
;; and also it will take O(n) space to store the sorted array
;;
(defn insert-sort [xs]
  (letfn [(insert [col x]
            (loop [[y & ys] col acc []]
              (cond
                (nil? y) (conj acc x)
                (<= x y) (vec (concat acc [x y] ys))
                :else (recur ys (conj acc y)))))]
    (reduce insert [] xs)))

(defn merge [left right]
  (loop [l left
         r right
         acc []]
    (cond
      (empty? l) (vec (concat acc r))
      (empty? r) (vec (concat acc l))
      (<= (first l) (first r)) (recur (rest l) r (conj acc (first l)))
      :else (recur l (rest r) (conj acc (first r))))))

(defn merge-sort [xs]
  (let [mid (int (/ (count xs) 2))
        left (take mid xs)
        right (drop mid xs)]
    (if (<= (count xs) 1)
      xs
      (merge (merge-sort left) (merge-sort right)))))

(defn merge1 [left right]
  (let [a (first left)
        b (first right)]
    (cond
      (nil? a) right
      (nil? b) left
      :else (if (<= a b)
              (cons a (merge1 (rest left) right))
              (cons b (merge1 left (rest right)))))))

(defn mergesort [xs]
  (if (<= (count xs) 1)
    xs
    (let
     [[low high] (split-at (int (/ (count xs) 2)) xs)]
      (merge1 (mergesort low) (mergesort high)))))

(mergesort [3 4 5 1 2])

(deftest insert-sort-test
  (testing "insert sort O(n^2)"
    (let [arr [3 4 5 1 2]]
      (is (match?
           (insert-sort arr)
           [1 2 3 4 5])))))

(deftest merge-sort-test
  (testing "merge sort O(nlogn)"
    (let [arr [3 4 5 1 2]]
      (is (match?
           (merge-sort arr)
           [1 2 3 4 5])))))

(insert-sort-test)
