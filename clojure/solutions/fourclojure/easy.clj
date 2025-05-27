(ns fourclojure.easy)

(defn fnlast [xs]
  (loop [x xs]
    (if (seq (rest x))
      (recur (rest x))
      (first x))))

(= (fnlast [1 2 3 4 5]) 5)
(= (fnlast '(1 2 3 4 5)) 5)
(= (fnlast '("a" "b" "c")) "c")

(defn penultimate [xs]
  (loop [x xs
         i nil]
    (if (seq (rest x))
      (recur (rest x)
             (first x))
      i)))

(= (penultimate [1 2 3 4 5]) 4)
#_(penultimate [1])
(= (penultimate '(1 2 3 4 5)) 4)
(= (penultimate '("a" "b" "c")) "b")

(defn fn-nth [xs n]
  (first (drop n xs))
  #_(loop [x xs
           i 0]
      (if (= i n)
        (first x)
        (recur (rest x) (inc i)))))

(= (fn-nth [1 2 3 4 5] 2) 3)
(= (fn-nth [:a :b :c] 0) :a)
(= (fn-nth [1 2 3 4] 1) 2)
(= (fn-nth '([1 2] [3 4] [5 6]) 2) [5 6])

(defn fn-count [xs]
  (loop [x xs
         i 0]
    (if (empty? x)
      i
      (recur (rest x) (inc i)))))

(= (fn-count [1 2 3 4 5]) 5)
(= (fn-count [:a :b :c]) 3)
(= (fn-count [1 2 3 4]) 4)
(= (fn-count '([1 2] [3 4] [5 6])) 3)

(defn fn-reverse [xs]
  (loop [x xs
         acc nil]
    (if (empty? x)
      acc
      (recur (rest x) (cons (first x) acc)))))

(= (fn-reverse [1 2 3 4 5]) '(5 4 3 2 1))
(= (fn-reverse '(1 2 3 4 5)) '(5 4 3 2 1))
(= (fn-reverse '("a" "b" "c")) '("c" "b" "a"))
(= (fn-reverse '([1 2] [3 4] [5 6])) '([5 6] [3 4] [1 2]))

(def s (partial apply +))
(defn fn-sumup [xs]
  (apply + xs)
  #_(loop [x xs
           acc 0]
      (if (empty? x)
        acc
        (recur (rest x) (+ acc (first x))))))

(= (s [1 2 3 4 5]) 15)
(= (fn-sumup [1 2 3 4 5]) 15)
(= (fn-sumup (list 0 1 2 3 4 5)) 15)
(= (fn-sumup #{3 2 1}) 6)
(= (fn-sumup #{3 2 -1}) 4)

(defn filter-odd [xs]
  (loop [x xs
         acc []]
    (if (empty? x)
      acc
      (if (odd? (first x))
        (recur (rest x) (conj acc (first x)))
        (recur (rest x) acc)))))

(def f (partial filter odd?))

(= (filter odd? [1 2 3 4 5]) '(1 3 5))
(= (f [1 2 3 4 5]) '(1 3 5))
(= (filter-odd [1 2 3 4 5]) '(1 3 5))
(= (filter-odd '(1 2 3 4 5)) '(1 3 5))
(= (filter-odd #{1 2 3 4 5}) '(1 3 5))

(defn fib-helper [i j]
  (lazy-seq (cons (+ i j) (fib-helper j (+ i j)))))
(take 8 (concat '(1 1) (fib-helper 1 1)))

(defn fib [n]

  (loop [i 0
         mem []]
    (if (= i n)
      mem
      (if (< i 2)
        (recur (inc i) (conj mem 1))
        (recur (inc i) (conj mem (+ (nth mem (- i 1))
                                    (nth mem (- i 2)))))))))

(= (fib 1) '(1))
(= (fib 3) '(1 1 2))
(= (fib 4) '(1 1 2 3))
(= (fib 5) '(1 1 2 3 5))
(= (fib 6) '(1 1 2 3 5 8))

(defn palindrome [xs]
  (loop [x xs]
    (cond
      (empty? x) true
      (not (= (first x) (last x))) false
      :else (recur (rest (butlast x))))))

(= (palindrome [1 2 3 2 1]) true)
(= (palindrome [1 2 3 3 2 1]) true)
(= (palindrome "racecar") true)

(defn my-flatten [xs]
  (loop [x xs
         acc []]
    (if (empty? x)
      acc
      (let [first-x (first x)]
        (if (coll? first-x)
          (recur (concat first-x (rest x)) acc)
          (recur (rest x) (conj acc first-x)))))))

(= (my-flatten [1 [3 4]]) '(1 3 4))
(= (my-flatten '([1 2] [3 4] [5 6])) '(1 2 3 4 5 6))
(= (my-flatten '([1 [2]])) '(1 2))
(= (my-flatten '([1 [2] [3]])) '(1 2 3))
(= (my-flatten '([1 [2] [3] [[4]]])) '(1 2 3 4))


