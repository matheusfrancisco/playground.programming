(ns union-find.impl)
; Author: matheusfrancisco

#_(defprotocol IQuickFind
    (is-connected? [this p q])
    (union [this p q]))

#_(defrecord QuickFindUF [n]
    IQuickFind
    (is-connected? [this p q]
      (= (get (:arr this) p) (get (:arr this) q)))

    (union [this p q]
      (let [pval (get (:arr this) p)
            qval (get (:arr this) q)]
        (vec (mapv (fn [x] (if (= x pval) qval x)) (:arr this))))))

(defn make-union-find [n]
  (vec (range n)))

(defn is-connected? [arr p q]
  (= (get arr p) (get arr q)))

(defn union [arr p q]
  (let [pval (get arr p)
        qval (get arr q)]
    (vec (mapv (fn [x] (if (= x pval) qval x)) arr))))

(defn main [n]
  (let [arr (make-union-find n)
        arr (union arr 1 2)
        arr (union arr 3 4)]
    (is-connected? arr 1 2)))

(println (main 10))
