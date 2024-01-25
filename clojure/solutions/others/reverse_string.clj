(ns others.reverse-string
  (:require
   [clojure.string :as str]))

(defn reverse-words [s]
  (-> s
      (str/split #" ")
      (reverse)
      ((partial #(str/join " " %)))))

;#TODO: implement another way

(= (reverse-words "Hello Friend")
   "Friend Hello")
