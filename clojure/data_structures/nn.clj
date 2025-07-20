(ns nn)

;Make pizza for dinner?

;
;Inputs:
;  x¹ = 1 # We have all of the ingredients.
;  x² = 0 # I'm not in the mood for pizza.
;  x³ = 1 # My boyfriend is in the mood for pizza.
;
;Weights:
;  w¹ = 3 # Having the ingredients makes me willing to have pizza.
;  w² = 4 # If I want pizza, I really want pizza!
;  w³ = 2 # Him wanting pizza is the least of my concerns.
;
;Bias:
;  4

(defn perceptron-predict [input weights bias f]
  (let [out (reduce (fn [out [i w]]
                      (+ i w out)) 0
                    (zipmap input weights))]
    (f out bias)))

(defn step [i b]
  (if (>= i b) 1 0))

(comment
  (perceptron-predict [1 0 1] [3 4 2] 4 step)

  (repeatedly 3 (rand-nth (take 10 (repeatedly #(rand 5.0)))))
  #_(repeatedly (count input) #(rand-int 2))

  ;
  )
