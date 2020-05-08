import React from 'react';

import ShortUrl from '../ShortUrl/ShortUrl.js';

import './ListOfUrls.css';

class ListOfUrls extends React.Component {

    render() {
        return (
            <div className="ListOfUrls">
                <ShortUrl url='www.biturl.com/sCcLvF8' />
                <ShortUrl url='www.biturl.com/zqnDuRr' />
                <ShortUrl url='www.biturl.com/sCcLvF8' />
                <ShortUrl url='www.biturl.com/zqnDuRr' />
            </div>
        )
    }
}

export default ListOfUrls;