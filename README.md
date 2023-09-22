# Playground Programming

![CI](https://github.com/matheusfrancisco/playground.programming/actions/workflows/ci.yaml/badge.svg)

This is a playground to play with competitive programming and algorithms and 
use it to learn you favorite language.

To add a solutions for a problem you need it must be passing in its website

### TODO
- [ ] Make it easier to add new language to run on CI
- [ ] add all my solutions (from those sites)
- [ ] Add zig dockerfile
- [ ] migrate .sh to clojure babashka (or another thing)
- [ ] Create a website to show the solutions solved and solutions not solved
- [ ] Add a backend to run submission inside dockerfile


Usually the code here already pass in all test case at:

- [Hackerrank](https://www.hackerrank.com)
- [Beecrowd](https://www.beecrowd.com.br/)
- [Codeforces](https://codeforces.com/)
- [Leetcode](https://leetcode.com)
- [Facebook Hacker Cup](https://www.facebook.com/codingcompetitions/hacker-cup)
- [GeeksForGeeks](https://www.geeksforgeeks.org/)
- [Google Code Jam](https://codingcompetitions.withgoogle.com/codejam/)
- [OverTheWire](https://overthewire.org/wargames/)
- [Project Euler](https://projecteuler.net/)
- [Rosalind](http://rosalind.info/problems/locations/)
- [SPOJ-br](https://br.spoj.com/)
- [SPOJ](https://www.spoj.com/)
- [UVA](https://onlinejudge.org/)
- [Cracking The Code Interview- Book]()

## Folder structure
```
make clean  # remove files created by the run task
make run [FOLDER=path/to/run] [LANGUAGES='language extensions']  # run solutions
make run # run solutions inside docker
make run_local #it will run in your machine without docker this mean you need to have those language installed
```
each folder could have been created in another github repository. (but I was too lazy to do it)

```
/clojure/
  - data_structure/
    - tree-bst.clj # it is an data_structure
  - algorithms/
    - bst.clj # it is a algorithms
  - solutions/
    - beecrowd/
      - 1000/ # number of the problem in the beecrowd website
        - solution.clj
        - in.txt
        - out.txt
        - problem.md
    - deps.edn
/zig/
  - data_structures/
  - algorithms/
  - solutions/
    - beecrowd/
    - codeforces/
    - google-code-jam/
```
