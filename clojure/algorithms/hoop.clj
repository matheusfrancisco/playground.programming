(ns hoop
  (:require
   [clojure.string :as cs]))

(defn extract-repo-name
  "Extract just the repository name from a full repository path. 
  Example: 'github.com/hoophq/runbooks' -> 'runbooks'"
  [repo-path]
  (when
   (string? repo-path)
    (->> (cs/split repo-path #"/") (remove cs/blank?) last)))

(defn- extract-folder
  "Extract folder from runbook name (e.g., 'ops/update-user.runbook.sh' -> 'ops/')"
  [name]
  (if (string? name)
    (let [parts (cs/split name #"/")]
      (if (> (count parts) 1)
        (str (first parts) "/")
        ""))
    ""))

(def sample-runbooks
  {:status :success
   :data
   [{:repository "github.com/hoophq/runbooks-infra"
     :items [{:name "onboarding/intro.md"}
             {:name "onboarding/checklist.md"}
             {:name "incident/2024_redis_down.md"}
             {:name "README.md"}]}

    {:repository "github.com/hoophq/runbooks-app"
     :items [{:name "deploy/rolling_update.md"}
             {:name "deploy/canary_guide.md"}
             {:name "troubleshooting/login_failures.md"}
             {:name "ROOT.md"}]}

    {:repository "github.com/hoophq/runbooks-internal"
     :items [{:name "security/policies/password_policy.md"}
             {:name "security/policies/2fa_policy.md"}
             {:name "security/rotation.md"}
             {:name "alerts/latency_high.md"}]}]})

(defn- generate-runbook-options
  [runbooks-list]
  (letfn [(folder-option [repo repo-name folder]
            (let [label (str "@" repo-name "/" folder)]
              {:label label
               :value {:repository repo
                       :name folder
                       :label label}}))

          (file-option [repo repo-name file]
            (let [label (str "@" repo-name "/" file)]
              {:label label
               :value {:repository repo
                       :name file
                       :label label}}))]

    (if (= :success (:status runbooks-list))
      (->> (:data runbooks-list)

           ;; flatten all repos
           (mapcat
            (fn [{:keys [repository items]}]
              (let [repo-name      (extract-repo-name repository)
                    folder-names   (->> items
                                        (map (comp extract-folder :name))
                                        (remove empty?)
                                        set)
                    folder-options (map #(folder-option repository repo-name %) folder-names)
                    file-options   (map #(file-option repository repo-name (:name %)) items)]
                (concat folder-options file-options))))

           vec)
      [])))

(generate-runbook-options sample-runbooks)
