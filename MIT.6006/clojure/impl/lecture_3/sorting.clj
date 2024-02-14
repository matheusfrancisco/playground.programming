(ns lecture-3.sorting
  (:require
   [matcher-combinators.test :refer [match?]]
   [clojure.test :refer [deftest is testing]]))

;; the designing of this sorting with imutable [] is not efficient
;; it will take O(n^2) time to sort the array
;; and also it will take O(n) space to store the sorted array
(defn insert-sort [arr]
  :not-implemented-yet)

(deftest insert-sort-test
  (testing "insert sort O(n^2)"
    (let [arr [3 4 5 1 2]]
      (is (match?
           (insert-sort arr)
           [1 2 3 4 5])))))

(insert-sort-test)

