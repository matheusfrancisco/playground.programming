(ns tree.btree)
#_"used by database systems
 large volume of data
 reduce disk operations
 disk I/O is proportional to tree height
 runtime of O(logn ) for many operations
 height can be less than red-black trees
 due to branching factor (nubmer of cildren)
"

;btree node = disk page
;root kept in main memory
;root
;      [ 30]  <- main node 
;   /            \
; [15 22       [40 55 63]
; /   \          /      \
;[9]   [17 21] [35 38] [45 50 60 70]
;

;first each node has n keys
;keys are stored in increasing order
;n +1 pointers to children
;
;the keys in each node dictate the range of keys in each child
;all leaves have the same depth
;
;
;lower and upper bound on the nubmer of keys
; minimum degree of tree
; called t
; t >= 2

; nubmer of keys
; - lower bound (except root) t-1)
;   - at least t - 1 keys
;   internal nods at least t children
;
;
;- upper bound
;  at most 2t - 1 keys
;  internal nodes at most 2t children
;
;
;b-tree node - disk page 
;height <= logt(n+1) / 2 = O(logn)

(defrecord Node [keys children])

(defprotocol IBtree
  (search [this k]))

(defrecord Btree [t keys children]
  IBtree
  (search [this k]
    :not-implemented))

(defn create-btree
  "Create a new btree"
  [t]
  (Btree. t [] []))

(create-btree 4)

