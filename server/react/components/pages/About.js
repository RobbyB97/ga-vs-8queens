import React from 'react';
import {connect} from 'react-redux';

import {page_ID__Set} from '../../redux/actions/page';

export class About extends React.Component {
    constructor(props) {
        super(props);
    };

    componentWillMount() {
        this.page_ID__Set('About');
    };

    page_ID__Set = (id) => {
        this.props.page_ID__Set(id);
    };

    render() {
        return (
            <div id="About">
                <section className="About__header">
                    <div className="About__headerContent">
                        <h1 className="About__title">
                            About this project
                        </h1>
                    </div>
                </section>

                <section className="About__content">
                    <p>
                        This web application has several different AI algorithms built in Python that are competing against each other as you read this. They are vying for the title of 'fastest solver of the 8 queens problem'. You can watch these algorithms compete in real time, see what they are thinking and how they approach the problem, or track their performance history.
                    </p>

                    <p>
                        If you would like more information on how each of the algorithms in this contest work, check the about section. (TODO: Add subpages on About section for each of the algorithms)To watch these algorithms compete in real time, you can head on over to the watch section.
                    </p>

                    <p>
                        This project is open source and able to be run on any local machine or cloud provider. If you have any interest at all in learning about AI or programming, I highly encourage to fork this repository on GitHub, follow the installation instructions and try altering the algorithms. I challenge you to make a genetic algorithm that solves the problem faster than any of the algorithms currently running on this server.
                    </p>
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

export default connect(undefined, mapDispatchToProps)(About);