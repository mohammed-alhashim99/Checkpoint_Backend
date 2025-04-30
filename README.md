
# 🎮 Checkpoint - Capstone Project

## 👤 User Story

As a user, I want to add the games I play to my personal list and track whether I have completed them or not, including the playtime, so I can monitor my progress easily. I also want to rate and review the games and see other users' reviews.

---

## 🎯 Project Goals

- User registration and login
- Add games to a user’s profile
- Track game completion status
- Log playtime
- Review and rate games
- View personal game list

---

## 🧱 ERD - Entity Relationship Diagram

- `User`: Stores user information
- `Games`: Stores game details
- `UserGame`: Join table connecting users and games with:
  - Completion status
  - Playtime hours
  - Date added
  - Date completed
- `Reviews`: User-written reviews and ratings
- `Platform`: Platform related to the game or review

---

## 🔁 API Endpoints

### User
| HTTP Verb | Path           | Action   | Description                |
|-----------|----------------|----------|----------------------------|
| POST      | /register       | create   | Register new user          |
| POST      | /login          | create   | Login user                 |
| GET       | /user/:id/games | index    | Get user's games list      |

---

### Game
| HTTP Verb | Path          | Action   | Description               |
|-----------|---------------|----------|---------------------------|
| GET       | /games        | index    | List all games            |
| GET       | /games/:id    | show     | Show single game          |
| POST      | /games        | create   | Add a new game            |
| PUT       | /games/:id    | update   | Update game information   |
| DELETE    | /games/:id    | destroy  | Delete a game             |

---

### UserGame
| HTTP Verb | Path                     | Action   | Description                       |
|-----------|--------------------------|----------|-----------------------------------|
| POST      | /usergame                | create   | Add game to user's list           |
| PUT       | /usergame/:id            | update   | Update playtime or completion     |
| DELETE    | /usergame/:id            | destroy  | Remove game from user's list      |

---

### Reviews
| HTTP Verb | Path              | Action   | Description               |
|-----------|-------------------|----------|---------------------------|
| POST      | /games/:id/review | create   | Add a review to a game     |
| GET       | /games/:id/review | index    | Get reviews for a game     |

---

## 🛠️ Tech Stack

- Backend: Django REST Framework
- Frontend: React
- Auth: JWT
- Database: PostgreSQL

---
