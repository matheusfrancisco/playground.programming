(ns skip-list)

(defrecord Node [key value next])
(defrecord SkipList [head max-level level])

(defn skiplist-search [^SkipList sl key]
  (loop [current (:head sl)
         level (:level sl)]
    (if (neg? level)
      (let [next-node (nth (:next current) 0)]
        (if (and next-node (= (:key next-node) key))
          (:value next-node)
          nil))
      (let [_ (prn current)
            _ (prn level)
            next-node (nth (:next current) level)]
        (prn :a next-node)
        (if (and next-node (< (:key next-node) key))
          (recur next-node level) ;; move forward
          (recur current (dec level))))))) ;; drop down a level
;Level 2:  [nil] -> [10] -> [nil]
;Level 1:  [nil] -> [5] -> [10] -> [15] -> [nil]
;Level 0:  [nil] -> [1] -> [5] -> [10] -> [15] -> [20] -> [nil]

;; Level 0 nodes
(def node20 (->Node 20 "twenty" [nil nil]))
(def node15 (->Node 15 "fifteen" [node20 nil]))
(def node10 (->Node 10 "ten" [node15 nil]))
(def node5  (->Node 5  "five" [node10 nil]))
(def node1  (->Node 1  "one"  [node5]))

;; Level 1 nodes
(def node15-l1 (->Node 15 "fifteen" [nil nil]))
(def node10-l1 (->Node 10 "ten" [node15-l1 nil]))
(def node5-l1  (->Node 5  "five" [node10-l1 nil]))

;; Level 2 nodes
(def node10-l2 (->Node 10 "ten" [nil nil]))

;; Head node
(def head (->Node nil nil [node10-l2 node5-l1 node1]))

(def my-skiplist (->SkipList head 3 2)) ;; max-level = 3, current level = 2

(skiplist-search my-skiplist 10) ;; => "ten"
;#skip_list.SkipList{:head #skip_list.Node{:key nil, :value nil, :next [#skip_list.Node{:key 10, :value "ten", :next [nil]} #skip_list.Node{:key 5, :value "five", :next [#skip_list.Node{:key 10, :value "ten", :next [#skip_list.Node{:key 15, :value "fifteen", :next [nil]}]}]} #skip_list.Node{:key 1, :value "one", :next [#skip_list.Node{:key 5, :value "five", :next [#skip_list.Node{:key 10, :value "ten", :next [#skip_list.Node{:key 15, :value "fifteen", :next [#skip_list.Node{:key 20, :value "twenty", :next [nil]}]}]}]}]}]},
;                    :max-level 3, :level 2}

;#skip_list.Node{:key nil, :value nil,
;                :next [#skip_list.Node{:key 10, :value "ten", :next [nil]}
;                       #skip_list.Node{:key 5, :value "five", :next [#skip_list.Node{:key 10, :value "ten", :next [#skip_list.Node{:key 15, :value "fifteen", :next [nil]}]}]}
;                       #skip_list.Node{:key 1, :value "one", :next [#skip_list.Node{:key 5, :value "five", :next [#skip_list.Node{:key 10, :value "ten", :next [#skip_list.Node{:key 15, :value "fifteen", :next [#skip_list.Node{:key 20, :value "twenty", :next [nil]}]}]}]}]}]}

