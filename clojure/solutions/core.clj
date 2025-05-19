(ns core
  (:require
   [clojure.string :as s])
  (:import
   (org.apache.pdfbox Loader)
   (org.apache.pdfbox.pdmodel PDDocument)
   (org.apache.pdfbox.text PDFTextStripper)))

(defn extract-first-page-text [file-path]
  (with-open [doc (Loader/loadPDF (java.io.File. file-path))]
    (let [stripper (doto (PDFTextStripper.)
                     (.setStartPage 1)
                     (.setEndPage 1))]
      (.getText stripper doc))))

(defn extract-title [file-path]
  (let [text (extract-first-page-text file-path)]
    (-> text
        (s/split-lines)))) ;; Assumes title is the first line

(println (take 4 (extract-title "resources/2403.15585v2.pdf")))
