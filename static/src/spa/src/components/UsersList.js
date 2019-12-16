import React, {Component} from 'react';
import UsersListItem from './UsersListItem'

export default class UsersList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            users: []
        };
    }

    componentDidMount() {
        fetch('http://127.0.0.1:5000/users')
            .then(response => response.json())
            .then(result => this.setState({users: result}))
            .catch(e => console.log(e));
    }

    render() {
        let user = this.state.users.map((user, index) => {
            return (
                <UsersListItem key={index} info={user}/>
            )
        });
        return (
            <div className="main">
                <ul className="users-list">
                    {user}
                </ul>
            </div>
        );
    }
}