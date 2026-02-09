(ns path-finder)

(def maze ["E.#..#"
           "#...#"
           "#.#.#"
           "#...#"
           "###S#"])

(def directions [[0 1] [1 0] [0 -1] [-1 0]])

(defn walk [maze [x y] visited path]
  (let [curr (get-in maze [x y])]

    #_(cond
        (= curr \S) (cons [x y] path) ; Found the start
        (= curr \#) (rest path) ; Hit a wall
        (= \. (get-in maze [x y])) (cons [x y] path) ; Empty cell, add to path
        (visited [x y])  path; Already visited this cell

        :else
        (let [news (for [[dx dy] directions
                         :when (and (>= (+ x dx) 0)
                                    (< (+ x dx) (count maze))
                                    (>= (+ y dy) 0)
                                    (< (+ y dy) (count (first maze))))]
                     [(+ x dx) (+ y dy)])
              path (walk maze [x y] (conj visited [x y]) path)]

          news))))

(defn path-finder [maze start]
  (walk maze start #{} []))

(path-finder maze [0 0])



