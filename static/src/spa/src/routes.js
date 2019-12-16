import React from 'react';
import { BrowserRouter, Route } from 'react-router-dom'

import Header from './components/Header'
import Home from './components/Home'
import BooksList from './components/BooksList'
import Book from './components/Book'
import UsersList from './components/UsersList'
import User from './components/User'
import Login from './components/Login'

export default (
    <BrowserRouter>
        <Header />
        <Route exact path="/" component={Home}/>
        <Route exact path="/login" component={Login} />
        <Route exact path="/books" component={BooksList} />
        <Route exact path="/books/:book_id" component={Book} />
        <Route exact path="/users" component={UsersList} />
        <Route exact path="/users/:user_id" component={User} />
    </BrowserRouter>
)
