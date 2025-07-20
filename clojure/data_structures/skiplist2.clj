(ns skiplist2
  (:require
   [clojure.zip :as zip]))

(defn make-node [v]
  {:value v :next nil})

;; [1] -> 
;; inserting [3]
;; [1] -> [3]
;; inserting [2]
;; [1] -> [2] -> [3]

(defn insert [value head]
  (cond
    (nil? head) (make-node value)

    (< value (:value head))
    (let [new-node (make-node value)]
      (assoc new-node :next head))

    :else
    (let [next-node (:next head)]
      (assoc head :next (insert value next-node)))))


;; Represent skiplist as a tree-like zipper structure
(defn skiplist-zip [skiplist]
  (zip/zipper
   (fn [node] (seq (:forward node)))  ; branch?
   (fn [node] (:forward node))        ; children
   (fn [node children] (assoc node :forward children))  ; make-node
   skiplist))

(defn search-path [zloc target compare-fn]
  (->> zloc
       (iterate zip/right)
       (take-while some?)
       (take-while #(neg? (compare-fn (zip/node %) target)))))


