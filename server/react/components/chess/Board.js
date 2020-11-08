import React from 'react';
import {connect} from 'react-redux';

import Square from './Square'
import Queen from './Queen';

export class Board extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            board: this.addSquares()
        };
    }

    addSquares() {
        let board = [];
        Array.from(Array(8), (e, i) => {
            let row = []
            Array.from(Array(8), (e, j) => {
                row.push(<Square 
                    row={i} col={j} 
                    key={`${i}${j}`}
                    placeQueen={this.placeQueen.bind(this)}
                    removeQueen={this.removeQueen.bind(this)}
                />)
            });
            board.push(row);
        });
        return board;

    }

    placeQueen(row = 0, col = 0) {
        return
    }

    removeQueen(row = 0, col = 0) {
        return
    }

    render() {
        return (
            <div className="Board">
                {Array.from(Array(8), (e, i) => { 
                    return <div className="Board__row">
                    {
                        Array.from(Array(8), (e, j) => {
                            //return console.log(`row: ${i}, col: ${j}`)
                            return this.state.board[i][j];
                        })
                    }
                </div>
                })}
            </div>
        );
    };
};

const mapStateToProps = (state) => {
    return {
        page_ID: state.page.id
    };
};

const mapDispatchToProps = (dispatch) => ({

})

export default connect(mapStateToProps, mapDispatchToProps)(Board);