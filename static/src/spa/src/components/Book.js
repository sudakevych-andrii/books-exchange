import React, {Component} from 'react';

export default class Book extends Component {
    constructor(props) {
        super(props);
        this.state = {
            book: {}
        }
    }

    componentDidMount() {
        let url = window.location.href;
        let id = url.match(/\d+$/g)[0];
        fetch('http://127.0.0.1:5000/books/' + id)
            .then(response => response.json())
            .then(result => this.setState({book: result}))
            .catch(e => console.log(e));
    }

    render() {
        let book = this.state.book;
        return (
            <div className="book">
                <div className="title">{book.title}</div>
                <div className="author">{book.author}</div>
            </div>
        );
    }
}
