import { ADD_LINK } from './types';

var id = 1;

export function addLink(url) {
    return {
        type: ADD_LINK,
        url: url,
        id: id++,
    }
}

// export const boundAddLink = url => dispatch(addLink(url));