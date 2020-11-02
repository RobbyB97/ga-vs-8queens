import {createStore, combineReducers} from 'redux'

import UI_Reducer from '../reducers/ui';
import Page_Reducer from '../reducers/page';

export default () => {
    return createStore(
        combineReducers({
            ui: UI_Reducer,
            page: Page_Reducer
        })
    );
};