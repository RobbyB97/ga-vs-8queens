import React from 'react';
import {connect} from 'react-redux';

import Square from './Square'
import Queen from './Queen';

export class Board extends React.Component {
    render() {
        return (
            <div className="Board">
                {Array.from(Array(8), (e, i) => { 
                    return <div className="Board__row">
                    {
                        Array.from(Array(8), (e, j) => {
                            //return console.log(`row: ${i}, col: ${j}`)
                            return <Square row={i} col={j}/>
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