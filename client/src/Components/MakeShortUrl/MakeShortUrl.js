import React from 'react';

import './MakeShortUrl.css';

class MakeShortUrl extends React.Component {

    constructor(props) {
        super(props);

        this.state = {url: null};

        this.handleTextChange = this.handleTextChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleTextChange(event) {
        console.log(event.target.value);
    }

    handleSubmit(event) {
        event.preventDefault();
        console.log('submit');
    }

    render() {
        return (
            <div className="MakeShortUrl">
                <form onSubmit={this.handleSubmit.bind(this)}>
                    <input type='text' 
                           name='url' 
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

export default MakeShortUrl;