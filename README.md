# Playground Algorithms
This is a playground to play with competitive programming and algorithms and 
use it to learn you favorite language.

To add a solutions for a problem you need it must be passing in its website

### TODO
- [ ] Add zig dockerfile
- [ ] migrate sh to clojure babashka
- [ ] Create a website to show the solutions solved and solutions not solved


Usually the code here already pass in all test case at:

- [Hackerrank]()
- [Beecrowd](https://www.beecrowd.com.br/)
- [Codeforces](https://codeforces.com/)
- [Leetcode]()
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
make run # run solutions on ci
make wrong  # show all solutions that are not complete yet
```
each folder could have been created in another github repository. (but I was too lazy to do it)

```
/clojure/
  - ds/
    - bst.clj
  - algorithms/
  - solutions/
    - codeforces/
      - solution.clj
      - 01.txt
      - 01-out.txt
    - beecrowd/
      - 1000/
        - solution.clj
        - in.txt
        - 01-out.txt
    - deps.edn
/zig/
  - ds/
    - bst.zig
  - algorithms/
  - solutions/
    - codeforces/
      - solution.zig
      - 01.txt
      - 01-out.txt
    - beecrowd/
      - solution.zig
      - 01.txt
      - 01-out.txt
```

if you want learn with me just send me an email:
matheusmachadoufsc@gmail.com


