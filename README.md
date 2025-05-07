# 🎮 Checkpoint - Game Tracker API

Checkpoint is a full-featured backend API that allows users to:
- Add games to their personal list
- Track playtime and completion status
- Submit and read reviews
- Search for games via the RAWG API
- Authenticate via JWT

---

## 🔧 Technologies

- Django & Django REST Framework
- PostgreSQL
- JWT Authentication (`djangorestframework-simplejwt`)
- RAWG API integration
- Unit Testing with Django's `TestCase`

---

## 📦 Models

### `User`
Built-in Django user model for registration and authentication.

### `Game`
```python
- game_id: int (unique)
- game_name: str
- release_date: date
- rating: float
- platform: str
- image_url: URL
```

### `UserGame`
Tracks user's interaction with a game.
```python
- user: FK to User
- game: FK to Game
- is_completed: bool
- playtime_hours: int
- added_at: datetime (auto)
- completed_at: datetime (nullable)
```

### `Review`
```python
- user: FK to User
- game: FK to Game
- rating: float
- description: str
- created_at: datetime (auto)
```

---

## 🔐 Auth Endpoints

| Method | Endpoint         | Description         |
|--------|------------------|---------------------|
| POST   | `/users/signup/` | Register new user   |
| POST   | `/users/login/`  | Login + JWT tokens  |

---

## 🕹️ Game Endpoints

| Method | Endpoint                     | Description             |
|--------|------------------------------|-------------------------|
| GET    | `/games/`                    | List all games          |
| POST   | `/games/`                    | Add a new game          |
| GET    | `/games/<id>/`               | Game detail             |
| PUT    | `/games/<id>/`               | Update game             |
| DELETE | `/games/<id>/`               | Delete game             |
| GET    | `/games/by-game-id/<gid>/`   | Fetch by RAWG game ID   |
| GET    | `/search/?q=term`            | Search games (RAWG API) |

---

## 🎯 UserGame Endpoints

| Method | Endpoint              | Description                  |
|--------|-----------------------|------------------------------|
| GET    | `/usergames/`         | List user's games            |
| POST   | `/usergames/`         | Add a game to user's list    |
| PUT    | `/usergames/<id>/`    | Update playtime/status       |
| DELETE | `/usergames/<id>/`    | Remove from user's list      |

---

## 📝 Review Endpoints

| Method | Endpoint                               | Description                 |
|--------|----------------------------------------|-----------------------------|
| GET    | `/reviews/`                            | List all reviews            |
| POST   | `/reviews/`                            | Add a review                |
| GET    | `/reviews/<id>/`                       | Get review detail           |
| PUT    | `/reviews/<id>/`                       | Update review               |
| DELETE | `/reviews/<id>/`                       | Delete review               |
| GET    | `/reviews/by-game/<gid>/`              | Reviews for specific game   |
| GET    | `/reviews/games/`                      | Games with at least 1 review|

---

## ✅ Testing

Tests cover:
- Model creation and relationships
- Cascade deletes (user/game)
- Unique constraints on `UserGame`
- Review linkage
Run tests using:
```bash
python manage.py test
```

---

## 📁 ERD (Entity Relationship Diagram)

- `User` 1 ⟶ M `UserGame`
- `Game` 1 ⟶ M `UserGame`
- `User` 1 ⟶ M `Review`
- `Game` 1 ⟶ M `Review`

---

## 📌 Notes

- All game data uses `game_id` from RAWG to avoid duplicates.
- Platforms are stored as comma-separated strings.
- JWT tokens returned on login/signup.
- Error handling implemented in views and serializers.
