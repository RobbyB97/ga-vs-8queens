# GA Vs. 8 Queens

# Abstract
The goal of this project is to create a [Genetic Algorithm *(GA)*](https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3?gi=32270bab8b8#:~:text=A%20genetic%20algorithm%20is%20a,offspring%20of%20the%20next%20generation.) that can solve the [8 Queens toy problem](https://en.wikipedia.org/wiki/Eight_queens_puzzle#:~:text=The%20eight%20queens%20puzzle%20is,row%2C%20column%2C%20or%20diagonal.) as efficiently as possible.

> Note: WIP. 

---

# Design
## 8 Queens Environment (./chessboard)
The 8 queens environment which the algorithms are using consist of 3 different objects. A *board*, *square* and *queen*.

-   ### Board
    -   Data:
        -   __board__: An 8x8 matrix, more specifically a list of lists contain square objects. This represents the physical chess board. To reference the square on the third row, second column, you would say...
        ``` python
            x = Board()
            x.board[2][1]
        ```
    - Functions:
        -   __place__(*row*, *col*): This runs the place function on the corresponding square of the board.

-   ### Square
    -   Data:
        -   __queen__: The queen object that may or may not be in any given square.
        -   __sum__: The sum of queens that are able to capture a piece on this square.
        -   __row__: Which row of the board the square is placed in.
        -   __col__: Which column of the board the square is placed in.
    -   Functions:
        -   __place__: Add a queen to the square instance.
        -   __canCapture__: increments the sum variable of the square instance.

-   ### Queen
    -   Data:
        -   __row__: The row of the Square the Queen is occupying
        -   __col__: The column of the Square the Queen is occupying