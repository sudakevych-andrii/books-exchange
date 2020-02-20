# Books exchange. Flask project.

## Authorization

POST

/auth/register  
Registration

POST

/auth/login  
Login

## Users

GET

/users  
The list of all users

/users/<user_id>  
Single user

## Books

GET

/books  
The list of all books except books that are hidden by the users. 
Only admin user can see all books;

/books/<book_id>  
Single book

POST

/books  
Only admin user (it will be checked on frontend) can create new book. 
All users can add book to their library or wishlist

PUT

/books  
Only admin user (it will be checked on frontend) can update book

DELETE

/books  
Only admin user (it will be checked on frontend) delete book

## Library

GET

/users/<user_id>/library  
Get user library

## Wishlist

GET

/users/<user_id>/wishlist  
Get user wishlist

## Account Library

/account/library

GET

User gets his library

PUT

User can change status of visibility and status of exchange of book

DELETE

User can delete book from his library

## Account Wishlist

/account/wishlist

GET

User gets his wishlist

DELETE

User can delete book from his wishlist