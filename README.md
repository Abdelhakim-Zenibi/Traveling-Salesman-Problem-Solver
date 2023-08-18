# TSP Solver 

## Overview

This repository contains the implementation of two different algorithms to solve the Traveling Salesman Problem (TSP): Dynamic Programming and K-opt Heuristic. The Traveling Salesman Problem is a classic optimization problem where the objective is to find the shortest path that visits a given set of cities exactly once and returns to the starting city.

<p align="center"><img align="center" width=40% height=100% alt="side_sticker" src="https://media.giphy.com/media/TEnXkcsHrP4YedChhA/giphy.gif" /><p/>

## Algorithms

### 1. Dynamic Programming

The dynamic programming approach involves breaking down the problem into smaller subproblems and storing the results to avoid redundant calculations. In the context of TSP, this approach calculates the optimal solution by exploring all possible combinations of cities and minimizing the total distance traveled.

### 2. K-opt Heuristic

The K-opt heuristic is a local search technique that aims to improve the solution by iteratively swapping segments of the route. This heuristic involves selecting a subset of cities and attempting to optimize the path between these cities. The "K" in K-opt represents the number of cities involved in each iteration.



