import React, {Component} from 'react';


export default class BooksListItem extends Component {
    render() {
        let url = window.location.href;
        let info = this.props.info;

        return (
            <li className="user">
                <a href={url + "/" + info.id}>{info.name}</a>
            </li>
        );
    }
}