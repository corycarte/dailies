#!/bin/bash

# Creates files for the following algorithms
# MergeSort
# QuickSort
# Dijkstra
# AStar
# BinarySearch
# BFS-recursive
# BFS-iterative
# DFS-recursive
# DFS-iterative
# KnapsackProblem

# For the languages:
# c#
# cpp
# java
# javascript
# kotlin -- new!
# python

# C# Algorithms

if [ ! -d "c-sharp" ]
then
    printf "Directory c-sharp doesn't exist, creating."
    mkdir c-sharp
fi

pushd ./c-sharp

#MergeSort
if [ ! -f MergeSort.cs ]; then
    touch MergeSort.cs
fi

# QuickSort
if [ ! -f QuickSort.cs ]; then
    touch QuickSort.cs
fi

# Dijkstra
if [ ! -f Dijkstra.cs ]; then
    touch Dijkstra.cs
fi

# AStar
if [ ! -f AStar.cs ]; then
    touch AStar.cs
fi
# BinarySearch
if [ ! -f BinarySearch.cs ]; then
    touch BinarySearch.cs
fi
# BFS-recursive
if [ ! -f BFS-recursive.cs ]; then
    touch BFS-recursive.cs
fi

# BFS-iterative
if [ ! -f BFS-iterative.cs ]; then
    touch BFS-iterative.cs
fi

# DFS-recursive
if [ ! -f DFS-recursive.cs ]; then
    touch DFS-recursive.cs
fi

# DFS-iterative
if [ ! -f DFS-iterative.cs ]; then
    touch DFS-iterative.cs
fi

# KnapsackProblem
if [ ! -f KnapsackProblem.cs ]; then
    touch KnapsackProblem.cs
fi
popd


# C++ Algorithms

if [ ! -d "cpp" ]
then
    printf "Directory cpp doesn't exist, creating."
    mkdir cpp
fi

pushd ./cpp

#MergeSort
if [ ! -f MergeSort.cpp ]; then
    touch MergeSort.cpp
fi

# QuickSort
if [ ! -f QuickSort.cpp ]; then
    touch QuickSort.cpp
fi

# Dijkstra
if [ ! -f Dijkstra.cpp ]; then
    touch Dijkstra.cpp
fi

# AStar
if [ ! -f AStar.cpp ]; then
    touch AStar.cpp
fi
# BinarySearch
if [ ! -f BinarySearch.cpp ]; then
    touch BinarySearch.cpp
fi
# BFS-recursive
if [ ! -f BFS-recursive.cpp ]; then
    touch BFS-recursive.cpp
fi

# BFS-iterative
if [ ! -f BFS-iterative.cpp ]; then
    touch BFS-iterative.cpp
fi

# DFS-recursive
if [ ! -f DFS-recursive.cpp ]; then
    touch DFS-recursive.cpp
fi

# DFS-iterative
if [ ! -f DFS-iterative.cpp ]; then
    touch DFS-iterative.cpp
fi

# KnapsackProblem
if [ ! -f KnapsackProblem.cpp ]; then
    touch KnapsackProblem.cpp
fi
popd

# Java

if [ ! -d "java" ]
then
    printf "Directory java doesn't exist, creating."
    mkdir java
fi

pushd ./java

#MergeSort
if [ ! -f MergeSort.java ]; then
    touch MergeSort.java
fi

# QuickSort
if [ ! -f QuickSort.java ]; then
    touch QuickSort.java
fi

# Dijkstra
if [ ! -f Dijkstra.java ]; then
    touch Dijkstra.java
fi

# AStar
if [ ! -f AStar.java ]; then
    touch AStar.java
fi
# BinarySearch
if [ ! -f BinarySearch.java ]; then
    touch BinarySearch.java
fi
# BFS-recursive
if [ ! -f BFS-recursive.java ]; then
    touch BFS-recursive.java
fi

# BFS-iterative
if [ ! -f BFS-iterative.java ]; then
    touch BFS-iterative.java
fi

# DFS-recursive
if [ ! -f DFS-recursive.java ]; then
    touch DFS-recursive.java
fi

# DFS-iterative
if [ ! -f DFS-iterative.java ]; then
    touch DFS-iterative.java
fi

# KnapsackProblem
if [ ! -f KnapsackProblem.java ]; then
    touch KnapsackProblem.java
fi
popd


# Javascript Algorithms

if [ ! -d "javascript" ]
then
    printf "Directory javascript doesn't exist, creating."
    mkdir javascript
fi

pushd ./javascript

#MergeSort
if [ ! -f MergeSort.js ]; then
    touch MergeSort.js
fi

# QuickSort
if [ ! -f QuickSort.js ]; then
    touch QuickSort.js
fi

# Dijkstra
if [ ! -f Dijkstra.js ]; then
    touch Dijkstra.js
fi

# AStar
if [ ! -f AStar.js ]; then
    touch AStar.js
fi
# BinarySearch
if [ ! -f BinarySearch.js ]; then
    touch BinarySearch.js
fi
# BFS-recursive
if [ ! -f BFS-recursive.js ]; then
    touch BFS-recursive.js
fi

# BFS-iterative
if [ ! -f BFS-iterative.js ]; then
    touch BFS-iterative.js
fi

# DFS-recursive
if [ ! -f DFS-recursive.js ]; then
    touch DFS-recursive.js
fi

# DFS-iterative
if [ ! -f DFS-iterative.js ]; then
    touch DFS-iterative.js
fi

# KnapsackProblem
if [ ! -f KnapsackProblem.js ]; then
    touch KnapsackProblem.js
fi
popd

# Kotlin

if [ ! -d "kotlin" ]
then
    printf "Directory kotlin doesn't exist, creating."
    mkdir kotlin
fi

pushd ./kotlin

#MergeSort
if [ ! -f MergeSort.kt ]; then
    touch MergeSort.kt
fi

# QuickSort
if [ ! -f QuickSort.kt ]; then
    touch QuickSort.kt
fi

# Dijkstra
if [ ! -f Dijkstra.kt ]; then
    touch Dijkstra.kt
fi

# AStar
if [ ! -f AStar.kt ]; then
    touch AStar.kt
fi
# BinarySearch
if [ ! -f BinarySearch.kt ]; then
    touch BinarySearch.kt
fi
# BFS-recursive
if [ ! -f BFS-recursive.kt ]; then
    touch BFS-recursive.kt
fi

# BFS-iterative
if [ ! -f BFS-iterative.kt ]; then
    touch BFS-iterative.kt
fi

# DFS-recursive
if [ ! -f DFS-recursive.kt ]; then
    touch DFS-recursive.kt
fi

# DFS-iterative
if [ ! -f DFS-iterative.kt ]; then
    touch DFS-iterative.kt
fi

# KnapsackProblem
if [ ! -f KnapsackProblem.kt ]; then
    touch KnapsackProblem.kt
fi
popd

# Python

if [ ! -d "python" ]
then
    printf "Directory python doesn't exist, creating."
    mkdir python
fi

pushd ./python

#MergeSort
if [ ! -f MergeSort.py ]; then
    touch MergeSort.py
fi

# QuickSort
if [ ! -f QuickSort.py ]; then
    touch QuickSort.py
fi

# Dijkstra
if [ ! -f Dijkstra.py ]; then
    touch Dijkstra.py
fi

# AStar
if [ ! -f AStar.py ]; then
    touch AStar.py
fi
# BinarySearch
if [ ! -f BinarySearch.py ]; then
    touch BinarySearch.py
fi
# BFS-recursive
if [ ! -f BFS-recursive.py ]; then
    touch BFS-recursive.py
fi

# BFS-iterative
if [ ! -f BFS-iterative.py ]; then
    touch BFS-iterative.py
fi

# DFS-recursive
if [ ! -f DFS-recursive.py ]; then
    touch DFS-recursive.py
fi

# DFS-iterative
if [ ! -f DFS-iterative.py ]; then
    touch DFS-iterative.py
fi

# KnapsackProblem
if [ ! -f KnapsackProblem.py ]; then
    touch KnapsackProblem.py
fi
popd

# GoLang

if [ ! -d "go" ]
then
    printf "Directory go doesn't exist, creating."
    mkdir python
fi

pushd ./go

#MergeSort
if [ ! -f MergeSort.go ]; then
    touch MergeSort.go
fi

# QuickSort
if [ ! -f QuickSort.go ]; then
    touch QuickSort.go
fi

# Dijkstra
if [ ! -f Dijkstra.go ]; then
    touch Dijkstra.go
fi

# AStar
if [ ! -f AStar.go ]; then
    touch AStar.go
fi
# BinarySearch
if [ ! -f BinarySearch.go ]; then
    touch BinarySearch.go
fi
# BFS-recursive
if [ ! -f BFS-recursive.go ]; then
    touch BFS-recursive.go
fi

# BFS-iterative
if [ ! -f BFS-iterative.go ]; then
    touch BFS-iterative.go
fi

# DFS-recursive
if [ ! -f DFS-recursive.go ]; then
    touch DFS-recursive.go
fi

# DFS-iterative
if [ ! -f DFS-iterative.go ]; then
    touch DFS-iterative.go
fi

# KnapsackProblem
if [ ! -f KnapsackProblem.go ]; then
    touch KnapsackProblem.go
fi
popd