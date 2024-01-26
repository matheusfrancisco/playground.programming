(ns others.valid-palindrome)

(def s "abba")

;;O(n)
;; improve this function 
;; make more readable
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

; remove at most one character make the string a palindrome
(defn palindrome? [s]
  (loop [left 0
         right (dec (count s))]
    (if (< left right)
      (if (= (nth s left) (nth s right))
        (recur (inc left) (dec right))
        (or (valid_palindrome (subs s (inc left) (inc right)))
            (valid_palindrome (subs s left right))))
      true)))

(= (palindrome? "abceba") true)

