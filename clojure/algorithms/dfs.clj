(ns dfs)

#_(def system {:system1 {:depends [:system2 :system3]}
               :system2 {:depends [:system4]}
               :system3 {:depends [:system1]}
               :system4 {:depends []}})

(defn dfs [system start visited]
  (if (contains? visited start)
    visited
    (let [new-visited (conj visited start)
          dependencies (:depends (get system start))]
      (reduce #(dfs system  %2 %1) new-visited dependencies))))

; (out) {:system1 {:depends [:system2 :system3]}, :system2 {:depends [:system4]}, :system3 {:depends []}, :system4 {:depends []}} #{:system1} :system2
#_(dfs system :system1 #{})

(def sample
  {:systems {:system1 {:on-start (fn [depends] (prn depends))
                       :on-change (fn [depends] (prn depends))
                       :data {:initial "data"}}
             :system2 {:depends [:system3]
                       :on-start (fn [depends] (prn depends))
                       :on-change (fn [depends] (prn depends))}
             :system3 {:depends [:system1]
                       :watch [:system1 :system2]
                       :on-start (fn [depends] (prn depends))
                       :on-change (fn [depends] (prn depends))}}})
(defn has-cycle? [system start visited]
  (prn "Checking for cycle starting at:" start)
  (prn "Visited nodes:" visited)
  (if (contains? visited start)
    (do 
      (prn "Cycle detected at:" start)
      [true, visited])
    (let [new-visited (conj visited start)
          dependencies (:depends (get system start))]
      (prn "Current dependencies:" dependencies)
      (some #(has-cycle? system % new-visited) dependencies))))

(has-cycle? (:systems sample) :system1 #{})

(def sample-system
  {:systems {:system1 {:on-start (fn [depends] (prn depends))
                       :on-change (fn [depends] (prn depends))
                       :data {:initial "data"}}
             :system2 {:depends [:system3]
                       :on-start (fn [depends] (prn depends))
                       :on-change (fn [depends] (prn depends))}
             :system3 {:depends [:system1]
                       :watch [:system1 :system2]
                       :on-start (fn [depends] (prn depends))
                       :on-change (fn [depends] (prn depends))}}})

(def s {:systems {:system1 {:depends []}
                  :system2 {:depends [:system1]}
                  :system3 {:depends [:system1 :system2]}
                  :system4 {:depends [:system3]}
                  :system5 {:depends [:system4 :system3 :system2]}}})


(defn cycle-for-all? [system]
  (let [systems (keys (:systems system))]
    (reduce (fn [acc system-name]
              (let [[has-cycle visited] (has-cycle? (:systems system) system-name #{})]
                (if has-cycle
                  (do
                    (prn "Cycle found in:" system-name)
                    true)
                  acc)))
            false
            systems)))

(cycle-for-all? (:systems s))

