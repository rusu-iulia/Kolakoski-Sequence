# Kolakoski Sequence Generator
This Python script was developed as a university project to study the behavior of the Kolakoski sequence and generate it efficiently. The Kolakoski sequence is a self-generating sequence of 1s and 2s, where the run lengths are determined by the sequence itself. 

## 🔍 Observations and Sequence Behavior
I observed that the combination of XOR and left-shift operations produces the characteristic variability and structure of the Kolakoski sequence.

## 🛠️ Algorithm
This script generates a sequence aimed to act similar to the the Kolakoski sequence using integer arithmetic, XOR, and bitwise shifts.

1. Initialization
- Both variables start at -1 to seed the self-referential computation.
- x controls the output, while y modulates the evolution of x.

2. Iteration Loop
- Bitwise XOR (^) with y introduces self-dependency, making each new value depend on the previous state.
- Left-shift y by 0 or 1, depending on the parity of x, modulates the influence of y in subsequent iterations.

``` 
output = x % 2 + 1
```
- The previous variable converts the result to 1 or 2, producing valid sequence elements, so each output is deterministic based on the previous states of x and y.

## ⚡ Performance

Time Complexity: O(n) — each iteration involves a fixed number of integer operations (division, XOR, modulo, shift).

Space Complexity: O(1).

## 🖥️ How to Use

1. Run the script
2. Enter the number of elements you want:
```
Enter number of iterations: 20
```
3. Get the result: 
```
1 2 2 1 1 2 1 2 2 1 2 2 1 1 2 1 1 2 2 1 
```

## 📊 Conclusion 
Through this university study, it was observed that the interaction of XOR and left-shift operations naturally reveals self-referential patterns, producing a sequence with the same structural properties as the classical Kolakoski sequence.
