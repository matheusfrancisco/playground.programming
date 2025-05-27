(ns fourclojure.easy2
  (:require
   [clojure.string :as string]))

(defn ffilter-caps [s]
  (clojure.string/join (filter #(and (<= (int \A) (int %) (int \Z)) (= (clojure.string/upper-case %) (str %))) s)))

(defn filter-caps [s]
  (clojure.string/join (filter #(Character/isUpperCase %) s)))

(= (filter-caps "$#A(*&987Zf") "AZ")
(= (filter-caps "HeLlO, WoRlD!") "HLOWRD")
(= (filter-caps "HellO") "HO")
(= (filter-caps "HeLLo") "HLL")
(= (filter-caps "Hello") "H")
(= (filter-caps "hello") "")
(= (filter-caps "HELLO") "HELLO")
(= (filter-caps "1234") "")
(= (filter-caps "!@#$%^&*()") "")
(= (filter-caps "") "")



