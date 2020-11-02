import React from 'react';

import DesktopNavigationLink from './DesktopNavigationLink';

export class DesktopNavigation extends React.Component {
    constructor(props) {
        super(props);
    };

    render() {
        return (
            <section id="DesktopNavigation">
                <nav className="DesktopNavigation__nav">
                    <ul className="DesktopNavigation__list">
                        {/* Links */}
                        {this.props.links &&
                            this.props.links.map((link) => (
                                <DesktopNavigationLink 
                                    key={link.text}
                                    {...link}
                                />
                            ))
                        }                 
                    </ul>
                </nav>
            </section>
        );
    };
};

export default DesktopNavigation;