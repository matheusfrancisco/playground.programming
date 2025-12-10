# Some avoid problems in Go programming language

## Problem 1: avoid stop the world pauses from garbage collection

- GC pauses correlate directly with allocation behavior.
less allocation -> fewer GC cycles -> fewer pauses -> smoother latency.

for latency-sensitive systems( gateways, protocol proxies, session handler, lsm tree memtable writes, tcp websocket multiplexrs)
- break tail-latency guarantees,
- cause backpressure,
- affect streaming protocols (RDP/MySQL/Postgres),
- inflate p99/p999 latency,

Some solutions:

Reduce allocations
Reuse buffers with sync.Pool
Avoid large short-lived objects

Every request that produces: (new slices, new structs, new temporary buffers, JSON objects, byte copies, maps)
adds pressure on both:( allocation (malloc), garbage collection (mark/sweep))

Reducing allocation rate reduces the wake frequency of the GC cycle.

- sync.Pool is not a cache — it is a temporary object reuse tool

for e.g:
```go
var bufPool = sync.Pool{
    New: func() interface{} { return make([]byte, 0, 4096) },
}

func write(w io.Writer, b []byte) {
    buf := bufPool.Get().([]byte)
    buf = append(buf[:0], b...)
    w.Write(buf)
    bufPool.Put(buf)
}

```
- Avoid large short-lived allocations

Large allocations (≥ 32 KB) bypass tiny allocators and go into the heap large object area.
If you allocate large slices for temporary work:

- they increase heap size instantly
- GC must trace them
- they may trigger a GC cycle earlier than expected
- STW phases become longer because scanning large memory regions dominates

Patterns that cause accidental allocations:

- strings.Split, fmt.Sprintf, fmt.Fprintf
- coercing []byte → string or vice versa
- map literals inside hot paths
- append patterns that reallocate

Use tools:

`go build -gcflags '-m'` to see escape analysis
pprof, benchstat, alloc_space
