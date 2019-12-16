import React, {Component} from 'react';

export default class User extends Component {
    constructor(props) {
        super(props);
        this.state = {
            user: {},
        };
        this.url = window.location.href
    }

    componentDidMount() {
        console.log(this.url);
        let id = this.url.match(/\d+$/g)[0];
        console.log(id);
        fetch('http://127.0.0.1:5000/users/' + id)
            .then(response => response.json())
            .then(result => this.setState({user: result}))
            .catch(e => console.log(e));
    }

    render() {
        let user = this.state.user;
        console.log(user)
        return (
            <div className="user">
                <div className="name">{user.name}</div>
                <div className="email">
                    <a href={"mailto:" + user.email}>{user.email}</a>
                </div>
                <div>
                    <a href={this.url + "/library"}>Library</a>
                </div>
                <div>
                    <a href={this.url + "/wishlist"}>Wishlist</a>
                </div>
            </div>
        );
    }
}