(ns lecture-6.avl
  (:require
   [clojure.string :as string]))

(defrecord Node [el left right])

(defn height
  ([tree]
   (height tree 0))
  ([tree count]
   (if tree
     (max (height (:left tree) (inc count))
          (height (:right tree) (inc count)))
     count)))

(defn factor [{:keys [left right]}]
  (- (height left) (height right)))

(defn rotate-left [{:keys [el left right] :as tree}]
  (if right
    (->Node (:el right) (->Node el left (:left right)) (:right right))
    tree))

(defn rotate-right [{:keys [el left right] :as tree}]
  (if left
    (->Node (:el left) (:left left) (->Node el (:right left) right))
    tree))

(defn is-left-case? [tree]
  (< (factor tree) -1))

(defn is-left-right-case? [tree]
  (and (is-left-case? tree) (> (factor (:right tree)) 0)))

(defn is-right-case? [tree]
  (> (factor tree) 1))

(defn is-right-left-case? [tree]
  (and (is-right-case? tree) (< (factor (:left tree)) 0)))

(defn insert [{:keys [el left right] :as tree} value]
  (cond
    (nil? tree) (Node. value nil nil)
    (< value el) (Node. el (insert left value) right)
    (> value el) (Node. el left (insert right value))
    :else tree))

(defn balance [{:keys [el left right] :as tree}]
  (cond
    (is-right-left-case? tree) (rotate-right (->Node el (rotate-left left) right))
    (is-left-right-case? tree) (rotate-left (->Node el left (rotate-right right)))
    (is-right-case? tree) (rotate-right tree)
    (is-left-case? tree) (rotate-left tree)
    :else tree))

(defn remove-element [{:keys [el left right] :as tree} value]
  (cond
    (nil? tree) nil
    (< value el) (Node. el (remove left value) right)
    (> value el) (Node. el left (remove right value))
    (nil? left) right
    (nil? right) left
    :else (let [min-value (min right)]
            (Node. min-value left (remove-element right min-value)))))

(def avl-insert (comp balance insert))
(def avl-remove (comp balance remove-element))
(def seq->avl (partial reduce avl-insert nil))

(defn tabs [n]
  (string/join (repeat n "\t")))

(defn visualise
  ([tree] (visualise tree 0))
  ([{:keys [el left right] :as tree} depth]
   (if tree
     (str (visualise right (inc depth)) (tabs depth) el "\n" (visualise left (inc depth)))
     (str (tabs depth) "~\n"))))

(visualise (seq->avl [1 2 3]))

#_(comment
    (defn min [{:keys [el left]}]
      (if left
        (recur left)
        el))

    (defn max [{:keys [el right]}]
      (if right
        (recur right)
        el))

    (defn contains? [{:keys [el left right] :as tree} value]
      (cond
        (nil? tree) false
        (< value el) (recur left value)
        (> value el) (recur right value)
        :else true))

    #_(defn count [{:keys [left right] :as tree}]
        (if tree
          (+ 1 (count left) (count right))
          0))

;; assert invariant
    (defn bst?
      ([tree] (bst? tree Integer/MIN_VALUE Integer/MAX_VALUE))
      ([{:keys [el left right] :as tree} min max]
       (cond
         (nil? tree) true
         (or (< el min) (> el max)) false
         :else (and (bst? left min (dec el))
                    (bst? right (inc el) max)))))
  ;
    )
