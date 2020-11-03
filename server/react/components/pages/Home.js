import React from 'react';
import {connect} from 'react-redux';

import {page_ID__Set} from '../../redux/actions/page';

export class Home extends React.Component {
    constructor(props) {
        super(props);
    };

    componentWillMount() {
        this.page_ID__Set('Home');
    };

    page_ID__Set = (id) => {
        this.props.page_ID__Set(id);
    };

    render() {
        return (
            <div id="Home">
                <section className="Home__header">
                    <div className="Home__headerContent">
                        
                    </div>

                    <div className="Home__github">
                        <a href="https://github.com/RobbyB97/ga-vs-8queens" target="_blank" rel="noopener">
                            <img src="/dist/images/github-corner-right.svg" alt="GitHub"/>
                        </a>
                    </div>
                </section>

                <section className="Home__content">
                    
                </section>
            </div>
        );
    };
};

const mapDispatchToProps = (dispatch) => ({
    page_ID__Set: (id) => {
        dispatch(page_ID__Set(id));
    }
});

export default connect(undefined, mapDispatchToProps)(Home);