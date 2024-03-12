(ns lecture-4.heap)

(defn swap* [v i j]
  (assoc v i (v j) j (v i)))

(defn left [i]
  (inc (* 2 i)))

(defn right [i]
  (+ (* 2 i) 2))

(defn largest-idx [arr i j]
  (if (>= (get arr i)
          (get arr j))
    i
    j))

(defn heapify [arr i size]
  (let [left (left i)
        right (right i)
        largest (if (and (< left size) (> (arr left) (arr i)))
                  left
                  i)
        largest (if (and (< right size) (> (arr right) (arr largest)))
                  right
                  largest)]
    (if (not= i largest)
      (recur (swap* arr i largest) largest size)
      arr)))

(defn build-heap [v]
  (let [n (count v)
        start (quot (dec n) 2)]
    (reduce (fn [acc i] (heapify acc i n)) v (range start -1 -1))))

(defn heap-sort [v]
  (let [n (count v)
        v (build-heap v)]
    (loop [i (dec n)
           v v
           arr []]
      (if (>= i 0)
        (let [m (get v 0)
              v (swap* v 0 i)]
          (recur (dec i) (heapify v 0 i) (conj arr m)))
        arr))))

#_(quot (dec (count [5 1 2 6 3 4])) 2)
#_(range 2 -1 -1)

;; Example usage:
(def my-vec [3 2 1 4 5])
(build-heap my-vec) ;[5 4 1 3 2]
(build-heap [5 1 2 6 3 4]) ;[6 5 4 1 3 2]

(heap-sort [5 1 2 6 3 4]) ; [6 5 4 3 2 1]
