[x] POST api/authenticate should perform user authentication and return a JWT token.
    [x] INPUT: Email, Password
    [x] RETURN: JWT token
    ➡️ **NOTE:** Use dummy email & password for authentication. No need to create endpoint for registering new user.

[x] POST api/follow/{id} authenticated user would follow user with {id}
[x] POST api/unfollow/{id} authenticated user would unfollow a user with {id}

[x] GET api/user should authenticate the request and return the respective user profile.
    [x] RETURN: User Name.
    [x] RETURN: Number of followers & followings.

[x] POST api/posts/ would add a new post created by the authenticated user.
    [x] Input: Title, Description
    [x] RETURN: Post[]ID, Title, Description, Created Time(UTC).

[x] DELETE api/posts/{id} would delete post with {id} created by the authenticated user.

[x] GET api/posts/{id} would return a single post 
    [x] with {id} populated 
    [x] with its number of likes 
    [x] with its comments

[x] GET api/all_posts would return all posts created by authenticated user sorted by post time.
    [x] RETURN: For each post return the following values
        [x] id: ID of the post
        [x] title: Title of the post
        [x] desc: Description of the post
        [x] created_at: Date and time when the post was created
        [x] comments: Array of comments, for the particular post
        [x] likes: Number of likes for the particular post

[x] POST api/like/{id} would like the post with {id} by the authenticated user.
[x] POST api/unlike/{id} would unlike the post with {id} by the authenticated user.

[x] POST api/comment/{id} add comment for post with {id} by the authenticated user.
    [x] Input: Comment
    [x] Return: Comment ID