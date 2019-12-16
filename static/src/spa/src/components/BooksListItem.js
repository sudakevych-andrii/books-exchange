import React, {Component} from 'react';
import ListItem from '@material-ui/core/ListItem';

export default class BooksListItem extends Component {
    render() {
        let url = window.location.href;
        let info = this.props.info;
        return (
            <ListItem className="book">
                <div className="author">{info.author}</div>
                <div className="title">
                    <a href={url + "/" + info.id}>{info.title}</a>
                </div>
            </ListItem>
        );
    }
}