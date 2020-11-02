import React from 'react';
import {connect} from 'react-redux';
import {BrowserRouter, Route, Switch} from 'react-router-dom';

import Header from '../components/common/Header';
import Footer from '../components/common/Footer';

import Home from './pages/Home';

export class Router extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            loaded: false,
            loading: false
        };
    };

    componentWillMount() {
        const $pageLoader = document.querySelector('.page-loader');

        // Disable loader
        if ($pageLoader) {
            $pageLoader.setAttribute('data-loading', true);
            this.setState({
                loading: true
            });
        };

        // Fade in React app
        setTimeout(() => {
            $pageLoader.setAttribute('data-loaded', true);
            this.setState({
                loaded: true
            });
        }, 300);
    };

    render() {
        return (
            <BrowserRouter>
                <div 
                    id="Router"
                    data-page_id={this.props.page_ID}
                    data-loading={this.state.loading}
                    data-loaded={this.state.loaded}
                >
                    <Header />

                    <Switch>
                        <Route 
                            path="/"
                            component={Home}
                            exact
                        />
                    </Switch>

                    <Footer />
                </div>
            </BrowserRouter>
        );
    };
};

const mapStateToProps = (state) => {
    return {
        page_ID: state.page.id
    };
};

export default connect(mapStateToProps, undefined)(Router);