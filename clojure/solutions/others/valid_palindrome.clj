(ns others.valid-palindrome)

(def s "abba")

;;O(n)
(defn valid_palindrome [string]
  (loop [left 0
         right (dec (count string))]
    (if  (< left right)
      (if (= (nth string left) (nth string right))
        (recur (inc left) (dec right))
        false)
      true)))

(= (valid_palindrome s) true)
(= (valid_palindrome "aaada") false)

(defn is_valid [s])


