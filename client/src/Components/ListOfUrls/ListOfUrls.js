import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';

import ShortUrl from '../ShortUrl/ShortUrl.js';

import './ListOfUrls.css';

class ListOfUrls extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            urls: []
        }
    }

    render() {
        console.log(this.props);


        let urls = ''

        if (this.props.urls) {
            urls = this.props.urls.map((item) => {
                console.log(item);
                return (<ShortUrl url={item.url} />)
            });
        }

        return (            
            <div className="ListOfUrls">
                { urls }
            </div>

        )
    }
}

ListOfUrls.propTypes = {
    urls: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.number.isRequired,
            url: PropTypes.string.isRequired
        }).isRequired
    ).isRequired
}

const mapStateToProps = (state) => {
    return {
        urls: state.urls
    }
}

export default connect(mapStateToProps)(ListOfUrls);