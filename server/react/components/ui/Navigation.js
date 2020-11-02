import React from 'react';

import HomeButton from './HomeButton';
import DesktopNavigation from './DesktopNavigation/DesktopNavigation';
import MobileNavigation from './MobileNavigation/MobileNavigation';

import links from '../../config/navigation';

export class Navigation extends React.Component {
    constructor(props) {
        super(props);
    };

    render() {
        return (
            <section id="Navigation">
                <HomeButton />

                <DesktopNavigation 
                    links={links}
                />
                
                <MobileNavigation 
                    links={links}                  
                />
            </section>
        );
    };
};

export default Navigation;