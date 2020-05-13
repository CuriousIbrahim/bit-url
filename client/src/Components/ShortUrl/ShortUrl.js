import React from 'react';
import PropTypes from 'prop-types';

import './ShortUrl.css';

class ShortUrl extends React.Component {

    constructor(props) {
        super(props);

    }

    render() {
        return (
            <div className="ShortUrl">
                {this.props.url}
            </div>
        )
    }
}

ShortUrl.propTypes = {
    url: PropTypes.string.isRequired,
}

export default ShortUrl;