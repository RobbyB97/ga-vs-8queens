import React from 'react';
import {connect} from 'react-redux';

import Queen from './Queen';

export class Square extends React.Component {
    constructor(props) {
        super(props);
        /*  props:
         *  row - int
         *  col - int
         * placeQueen -
         */
        this.state = {
            queen: false,
        }
    }

    hasQueen() {
        return this.state.queen;
    }

    placeQueen() {
        if (this.state.queen) {
            return new Error("Can't place multiple queens on the same board")
        }

        this.props.placeQueen();
        this.setState({
            ...this.state,
            queen: true
        });
    }

    removeQueen() {
        this.props.removeQueen();
        this.setState({
            ...this.state,
            queen: false
        });
    }

    toggleQueen() {
        if (this.state.queen) {
            return this.removeQueen();
        }
        this.placeQueen();
    }

    render() {
        return (
            <div 
                className="Square"
                onClick={this.toggleQueen.bind(this)}
                key={this.props.key}
                data-row={this.props.row} 
                data-col={this.props.col}
            >
                {this.state.queen &&
                    <Queen />
                }
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

export default connect(mapStateToProps, mapDispatchToProps)(Square);