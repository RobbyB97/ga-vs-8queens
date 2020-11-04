import React from 'react';
import {connect} from 'react-redux';

export class Queen extends React.Component {
    render() {
        return (
            <div className="Queen">
                <div className="Queen__queen">
                    <img src="/dist/images/queen.png" />
                </div>
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

export default connect(mapStateToProps, mapDispatchToProps)(Queen);