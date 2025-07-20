
(ns sk
  (:import (java.util Random)))

(def ^:const max-level 16)
(def ^:const p 0.5)

(defn random-level
  [random]
  (loop [level 1]
    (if (or (>= level max-level) (>= (.nextDouble random) p))
      level
      (recur (inc level)))))

(defn node
  [key value level]
  {:key key :value value :next (atom (vec (repeat level nil)))})

(defn skip-list
  []
  {:header (node "HEAD" nil max-level) :random (Random.)})

(defn insert
  [skip-list key value]
  (let [level (random-level (:random skip-list))
        new-node (node key value level)
        update (atom (vec (repeat level (:header skip-list))))]
    (loop [curr (:header skip-list) i (dec level)]
      (if (and (>= i 0) (get (:next curr) i) (<= (:key (get (:next curr) i)) key))
        (do
          (swap! update assoc i curr)
          (recur (get (:next curr) i) i))
        (do
          (when (>= i 0)
            (swap! (:next new-node) assoc i (get (:next (get @update i)) i))
            (swap! (:next (get @update i)) assoc i new-node)
            (recur curr (dec i))))))))

(defn search
  [skip-list key]
  (loop [curr (:header skip-list) i (dec max-level)]
    (if (and (>= i 0) (get (:next curr) i) (< (:key (get (:next curr) i)) key))
      (recur (get (:next curr) i) i)
      (if (and (= i 0) (get (:next curr) 0) (= (:key (get (:next curr) 0)) key))
        (:value (get (:next curr) 0))
        nil))))

(def s (skip-list))
(insert s "A" 1)
(insert s "k" 1)

(search s "k") ; => 1
; (out) {:header {:key "HEAD", :value nil, :next #atom[[{:key "k", :value 1, :next #atom[[nil nil nil nil nil] 0xe47d871]} {:key "k", :value 1, :next #atom[[nil nil nil nil nil] 0xe47d871]} {:key "k", :value 1, :next #atom[[nil nil nil nil nil] 0xe47d871]} {:key "k", :value 1, :next #atom[[nil nil nil nil nil] 0xe47d871]} {:key "k", :value 1, :next #atom[[nil nil nil nil nil] 0xe47d871]} nil nil nil nil nil nil nil nil nil nil nil] 0x1b4300b3]}, :random #object[java.util.Random 0x7cdb54af "java.util.Random@7cdb54af"]}
