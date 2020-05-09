import React from 'react';
import axios from 'axios';
import { connect } from 'react-redux';

import { addLink } from '../../actions';

import './MakeShortUrl.css';

const DOMAIN_NAME = 'http://localhost:5000'

class MakeShortUrl extends React.Component {

    constructor(props) {
        super(props);

        this.state = {url: null};

        this.handleTextChange = this.handleTextChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleTextChange(event) {
        console.log(event.target.value);

        this.setState({url: event.target.value});
    }

    handleSubmit(event) {
        event.preventDefault();
        
        let url = `${DOMAIN_NAME}/create?url=${this.state.url}`;

        axios.get(url)
            .then(res => {
                let id = res.data.id;
                let shortUrl = `${DOMAIN_NAME}/${id}`

                this.props.addLink(shortUrl);
                
                this.setState({url: ''});
            });

    }

    clearInput() {
        document.getElementsByClassName('url-input')[0].reset();
    }

    render() {
        return (
            <div className="MakeShortUrl">
                <form onSubmit={this.handleSubmit.bind(this)}>
                    <input type='text' 
                           name='url'
                           value={this.state.url} 
                           className='url-input' 
                           placeholder='www.example.com' 
                           onChange={this.handleTextChange.bind(this)}/>
                    {/* <br />
                    // <input type="submit" value="Submit" class='url-submit'/> */}
                </form>
            </div>
        )
    }
}

export default connect(
    null,
    { addLink }
)(MakeShortUrl);