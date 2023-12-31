(ns leetcode.target-sum.solution
  (:require
   [clojure.string :as string]))

;;d[(i target)] = f(i - 1, target - nums[i]) + f(i - 1, target + nums[i])

(def target 4)
(def dp (atom {}))

(defn backtracking [nums i t]
  (if (contains? @dp [i t])
    (get @dp [i t])
    (if (= i (dec (count nums)))
      (if (= t target)
        1
        0)
      (let [r (backtracking nums (inc i) (- t (nums i)))
            r2 (backtracking nums (inc i) (+ t (nums i)))
            result (+ r r2)
            _ (swap! dp assoc  [i t] result)]
        (get @dp [i t])))))

(defn calculate [nums target]
  (backtracking nums 0 target))

(calculate [1 1 1 1 1] 2)

#_(defn return-stored [store k v]
  (let [store (cond-> store
                (not (contains? store k))
                (assoc k v))]
    [store (get store k)]))

#_(defn bck [nums i t]
  (reduce  (fn [{:keys [store acc]} n]
             (let [[store v] (return-stored store [i t] n)]
               {:store store
                :acc (conj acc v)})) nums))

#_(bck [1 1 1 1 1] 0 2)

#_(defn main []
    (let [[size target] (string/split
                         (Integer/parseInt) #" ")
          nums  (loop [i 0 nums []]
                  (if (< i (Integer/parseInt size))
                    (recur (inc i) (conj nums (Integer/parseInt
                                               (read-line))))
                    nums))]

      nums))

