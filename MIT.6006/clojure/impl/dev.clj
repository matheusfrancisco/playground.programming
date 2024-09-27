(ns dev
  (:require [clojure.pprint :as pprint]
            [portal.api :as portal]))

(def p (portal/open))
(portal/tap)

(tap> {:a 1
       :b 2
       :c-plus-b (+ 2 3)})

(tap> (map-indexed #(hash-map :x %1 :y %2)  (range 10 20)))

(def graph {:nodes {1 {:label "Node 1"}
                    2 {:label "Node 2"}
                    3 {:label "Node 3"}}
            :edges #{#{1 2}
                     #{3 1}}})

(def h (slurp "https://google.com.br"))

(tap> h)

(portal/clear)
(portal/close p)

