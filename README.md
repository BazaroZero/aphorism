![logo_small](https://user-images.githubusercontent.com/64976988/168271445-6a5958af-d534-49cc-8187-4190a12d546b.svg)

Yandex.Lyceum Flask project

Aphorism is the REST API of a new social networking concept or we can call it a podcast platform. Posts can only consist of short captions and a voice message. At the moment the backend is ready. The web version will most likely be developed later.

## Description 📋
 - Each user will have his own profile with gravatar, where you can post, see statistics, change status
 - The feed will consist of posts by people the user is subscribed to. You can "Like" a post as usual
 - Using the search will allow to find new authors 

## Using 🎧
```sh
git clone https://github.com/xDiaym/aphorism.git
```
Move to project's directory
```sh
docker-compose up
```
Check swagger documentation on http://localhost:8000/api/v1/docs

## Testing ✔️
To run the tests, simply do the following in a Linux environment (in Windows it can be WSL)
```sh
tests/test.sh
```

## Approximate web version design 🖥️
You can see the progress in the ```feature/frontend``` branch

- Index page
![index_page](https://user-images.githubusercontent.com/64976988/171383461-1f0aa4fa-3b19-4999-a0dc-6f7c137a7ff4.png)

- Sign up page
![sign_up](https://user-images.githubusercontent.com/64976988/171384598-a979cf15-a04f-47bc-a595-e9dfb524ecd6.png)

- Feed page
![feed](https://user-images.githubusercontent.com/64976988/171388994-8ce5add6-6c03-4185-a4ca-96bcbb3da4be.png)


