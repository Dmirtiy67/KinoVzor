// index.js
const API_URL = "http://localhost:8000";
const moviesContainer = document.getElementById("movies-container");
const searchInput = document.getElementById("search-input");
const movieModal = document.getElementById("movie-modal");
const closeModal = document.getElementById("close-modal");
const reviewText = document.getElementById("review-text");
const reviewStars = document.getElementById("review-stars");
const addReviewBtn = document.getElementById("btn-add-review");
const adminFunctions = document.getElementById("admin-functions");
const addMovieBtn = document.getElementById("btn-add-movie");
const addMovieForm = document.getElementById("add-movie-form");

const token = localStorage.getItem("access_token");
const isAdminUser = localStorage.getItem("user_role") === "admin";

// Получение фильмов с фильтром
async function fetchMovies(query = "") {
    try {
        let url = '${API_URL}/films';
        if (query) url += '?search=${encodeURIComponent(query)}';
        const res = await fetch(url);
        const data = await res.json();
        renderMovies(data);
    } catch (err) {
        console.error("Ошибка при получении фильмов:", err);
    }
}

// Рендер фильмов
function renderMovies(movies) {
    moviesContainer.innerHTML = "";
    movies.forEach(film => {
        const div = document.createElement("div");
        div.className = "movie-card";
        div.innerHTML = `
            <img src="${film.image_url}" alt="${film.name}" class="movie-img" data-id="${film.id}">
            <h3>${film.name}</h3>
            <p>${film.year} | ${film.genre} | ${film.actors.join(", ")}</p>
            <button class="btn-view" data-id="${film.id}">Смотреть</button>
        `;
        moviesContainer.appendChild(div);
    });

    document.querySelectorAll(".btn-view").forEach(btn => btn.addEventListener("click", () => openMovieModal(btn.dataset.id)));
    document.querySelectorAll(".movie-img").forEach(img => img.addEventListener("click", () => openMovieModal(img.dataset.id)));
}

// Модальное окно фильма
async function openMovieModal(filmId) {
    try {
        const res = await fetch(`${API_URL}/films/${filmId}`);
        const film = await res.json();

        document.getElementById("movie-img").src = film.image_url;
        document.getElementById("movie-name").textContent = film.name;
        document.getElementById("movie-year-genre-actors").textContent = '${film.year} | ${film.genre} | ${film.actors.join(", ")}';
        document.getElementById("movie-description").textContent = film.description;

        const reviewsList = document.getElementById("reviews-list");
        reviewsList.innerHTML = "";
        film.reviews.forEach(r => {
            const div = document.createElement("div");
            div.textContent = '${r.user.name}: ${"⭐".repeat(r.stars)} - ${r.description}';
            reviewsList.appendChild(div);
        });

        document.getElementById("add-review").style.display = token ? "block" : "none";
        adminFunctions.style.display = isAdminUser ? "block" : "none";

        movieModal.style.display = "flex";

        // Добавление отзыва
        addReviewBtn.onclick = async () => {
            const payload = {
                description: reviewText.value,
                stars: parseInt(reviewStars.value),
                film_id: film.id
            };
            try {
                await fetch(`${API_URL}/reviews`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": 'Bearer ${token}'
                    },
                    body: JSON.stringify(payload)
                });
                reviewText.value = "";
                reviewStars.value = "1";
                fetchMovies(); // обновление списка фильмов
                openMovieModal(film.id); // обновление отзывов
            } catch (err) {
                alert("Ошибка при добавлении отзыва: " + err.message);
            }
        };
    } catch (err) {
        console.error("Ошибка при открытии фильма:", err);
}
}

// Добавление фильма (только админ)
if (isAdminUser && addMovieBtn && addMovieForm) {
    addMovieBtn.style.display = "block";
    addMovieForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const formData = new FormData(addMovieForm);
        const payload = {
            name: formData.get("name"),
            year: parseInt(formData.get("year")),
            genre: formData.get("genre"),
            actors: formData.get("actors").split(",").map(a => a.trim()),
            description: formData.get("description"),
            image_url: formData.get("image_url"),
        };
        try {
            await fetch(`${API_URL}/films`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": 'Bearer ${token}'
                },
                body: JSON.stringify(payload)
            });
            fetchMovies();
            addMovieForm.reset();
            alert("Фильм добавлен!");
        } catch (err) {
            alert("Ошибка при добавлении фильма: " + err.message);
        }
    });
}

// Закрытие модального окна
closeModal.addEventListener("click", () => { movieModal.style.display = "none"; });

// Поиск фильмов
searchInput.addEventListener("input", () => { fetchMovies(searchInput.value); });

// Загрузка фильмов при старте
document.addEventListener("DOMContentLoaded", () => { fetchMovies(); });

// Функция выхода
function logoutUser() {
    localStorage.removeItem("access_token");
    localStorage.removeItem("user_role");
    window.location.href = "/auth.html";
}
