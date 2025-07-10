(ns bs
  (:require
   [clojure.math :as math]))

(defn search [xs hi lo e]
  (let [mid (+ (quot (- hi lo) 2) lo)]
    (cond
      (> lo hi) false
      (= (get xs mid) e) true
      (< (get xs mid) e) (search xs hi (inc mid) e)
      :else (search xs (dec mid) lo e))))

(defn binary-search [xs e]
  (let [hi (dec (count xs))
        lo 0]
    (search xs hi lo e)))

(defn search2
  "Return the index of e in xs, or -1 if not present.
   xs must be a monotonically _ascending_ vector."
  [xs lo hi e]
  (when (<= lo hi)                     ;; stop when interval is empty
    (let [mid (quot (+ lo hi) 2)       ;; midpoint
          v   (nth xs mid)]            ;; value at midpoint
      (cond
        (= v e) mid                    ;; found!
        (< v e) (recur xs (inc mid) hi e)  ;; search upper half
        :else   (recur xs lo (dec mid) e))))) ;; search lower half

(defn binary-search2 [xs e]
  (or (search2 xs 0 (dec (count xs)) e) false))

(defn bs [xs e]
  (loop [xs xs
         lo 0
         hi (dec (count xs))
         mid (quot (+ lo hi) 2)
         needed e]
    (cond
      (> lo hi) false
      (= (nth xs mid) needed) true
      (< (nth xs mid) needed) (recur xs (inc mid) hi
                                     (quot (+ lo hi) 2)
                                     needed)
      :else (recur xs lo (dec mid) (quot (+ lo hi) 2)
                   needed))))

(comment

  (= (binary-search [1 2 3 4 5 6 8] 6) true)
  (= (bs [1 2 3 4 5 6 8] 6) true)
  (= (binary-search2 [1 2 3 4 5 6 8] 16) false))

