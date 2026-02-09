package misc

// design  simple loack strategy for high update map
// Go map is not for concurent writes, so we usully protect it with sync.Mutex or sync.RWMutex
// under a write heavy workload, a coarse lock becames a global serialization point:
//

// - only one goroutine can updte at a time
// all other gorutines are blocked waiting for the lock to be released
// cpu cores stay idle during blocking
// throughput drops significantly


//This is especially damaging in:
//counters / metrics aggregators
//rate limiters
//protocol session stores
//caches
//shared redactor/anonymizer tables
//hot paths in proxies (your use cases)
