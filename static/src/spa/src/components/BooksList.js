import React, {Component} from 'react';
import BooksListItem from './BooksListItem'
import List from '@material-ui/core/List';

export default class BooksList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            books: []
        };
    }

    componentDidMount() {
        fetch('http://127.0.0.1:5000/books')
            .then(response => response.json())
            .then(result => this.setState({books: result}))
            .catch(e => console.log(e));
    }

    render() {
        let book = this.state.books.map((book, index) => {
            return (
                <BooksListItem key={index} info={book}/>
            );
        });
        return (
            <div className="main">
                <List className="books-list">
                    {book}
                </List>
            </div>
        );
    }
}
