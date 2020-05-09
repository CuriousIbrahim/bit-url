import React from 'react';
import PropTypes from 'prop-types';

import './ShortUrl.css';

class ShortUrl extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            url: this.props.url
        }
    }

    render() {
        return (
            <div className="ShortUrl">
                {this.state.url}
            </div>
        )
    }
}

ShortUrl.propTypes = {
    url: PropTypes.string.isRequired,
}

export default ShortUrl;