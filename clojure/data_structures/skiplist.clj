(ns skiplist)

;level
;[
;
;
;  
;-level2
;- level1
;- level0
;]

(defn search
  "Skiplist-style search that maintains position across levels"
  [xs e]
  (loop [level (dec (count xs))  ; Start from highest level
         pos 0]                  ; Current position in the level
    (if (>= level 0)
      (let [current-level (nth xs level)
            level-size (count current-level)]
        (cond
          ;; If position is beyond current level, move to next level
          (>= pos level-size)
          (recur (dec level) pos)

          ;; Found exact match
          (= (nth current-level pos) e) (list true pos level e)

          ;; Current element is less than target
          (< (nth current-level pos) e)
          (cond
            ;; At end of level, move to next level
            (= pos (dec level-size))
            (recur (dec level) pos)

            ;; Next element exists and is greater than target
            (and (< (inc pos) level-size)
                 (> (nth current-level (inc pos)) e))
            (recur (dec level) pos)

            ;; Continue searching in current level
            :else
            (recur level (inc pos)))

          ;; Current element is greater than target, move to next level
          (> (nth current-level pos) e)
          (recur (dec level) (max 0 (dec pos)))))
      (list false pos level nil))))

(defn insert-at-level
  "Insert element e at position pos in level-vec"
  [level-vec pos e]
  (let [before (take pos level-vec)
        after (drop pos level-vec)]
    (vec (concat before [e] after))))

(defn insert
  "Insert element e into skiplist xs with random level promotion"
  [xs e]
  (let [[found? pos level item] (search xs e)]
    (if found?
      xs
      (let [xs (vec (reverse xs))]
        (loop [current-level 0
               result-xs (assoc xs 0 (insert-at-level (nth xs 0) pos e))]
          (let [coin-flip (inc (rand-int 2))]  ; Random 1 or 2
            (println (str "Level " current-level " - coin flip: " coin-flip))
            (if (and (= coin-flip 1)
                     (< (inc current-level) (count xs)))  ; Can promote to next level
              (recur (inc current-level)
                     (assoc result-xs (inc current-level)
                            (insert-at-level (nth result-xs (inc current-level)) pos e)))
              (reverse result-xs))))))))

(defn lookup [xs e] (nth (search xs e) 3))

(comment
  (insert [[0 1 12] [0 1 12] [0 1 12 22] [0 1 2 12 22 29 33]] 3)
  (insert [[0 1 12] [0 1 12] [0 1 12 22] [0 1 2 12 22 29 33]] 32)

  (lookup [[0 1 12] [0 1 12] [0 1 12 22] [0 1 2 12 22 29 33]] 11)
  (search [[0 1 12] [0 1 12] [0 1 12 22] [0 1 2 12 22 29 33]] 12)
  (search [[0 1 12] [0 1 12] [0 1 12 22] [0 1 2 12 22 29 33]] 11))



