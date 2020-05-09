import { createStore, applyMiddleware } from 'redux';

import rootReducer from './reducers';

export const initialState = {
    urls: []
};

const middleware = [];

// export const store = createStore(rootReducer, initialState, applyMiddleware());
export const store = createStore(
    rootReducer,
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);
