

# Github Contribution Graph Manager (gcgman)
A python script to write words into your github contribution graph. Chosen word has a length limit
of 8.

Currently supported letters : 
A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, R, S, T, U, V, Y, Z, X, W, Q, space

## Usage
`gcgman WORD [OPTION...]`

## Contribution
Each character can use maximum of 42 days (6 weeks or 6 colums). First and the last column is not
used if they are not necessary. gcgman treats each letter as a list of integers from 0 to 41.
Days used in drawing the letter are included in the list. Days an array numbers are shown in the
picture below.

![Array](tile-numbers.png)
