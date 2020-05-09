import { ADD_LINK } from '../actions/types';

export const urls = (urls = [], action) => {
    switch (action.type) {
        case ADD_LINK:
            return [{
                id: action.id,
                url: action.url
            }, ...urls];
        default:
            return urls;
    }
}