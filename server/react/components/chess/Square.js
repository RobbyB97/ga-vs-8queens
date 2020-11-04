import React from 'react';
import {connect} from 'react-redux';

import Queen from './Queen';

export class Square extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            queen: false,
        }
    }

    hasQueen() {
        return this.state.queen;
    }

    placeQueen() {
        this.setState({
            ...state,
            queen: true
        });
    }

    removeQueen() {
        this.setState({
            ...state,
            queen: false
        });
    }

    render() {
        return (
            <div className="Square" data-row={this.props.row} data-col={this.props.col}>
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