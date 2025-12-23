const API_URL = "http://localhost:8000";

async function loginUser() {
    const email = document.getElementById("login-email").value;
    const password = document.getElementById("login-password").value;

    try {
        const res = await fetch(`${API_URL}/auth/login`, {
            method: "POST",
            headers: {"Content-Type":"application/json"},
            body: JSON.stringify({email, password})
        });

        if(!res.ok) throw new Error("Неправильно указаны почта или пароль");

        const data = await res.json();
        localStorage.setItem("access_token", data.access_token);
        localStorage.setItem("user_role", data.role);

        window.location.href = "/index.html";
    } catch(err) {
        alert(err.message);
    }
}

async function registerUser() {
    const name = document.getElementById("reg-name").value;
    const email = document.getElementById("reg-email").value;
    const password = document.getElementById("reg-password").value;

    try {
        const res = await fetch(`${API_URL}/auth/register`, {
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({name,email,password})
        });

        if(!res.ok) throw new Error("Ошибка регистрации");

        alert("Вы успешно зарегистрированы!");
        document.getElementById("reg-form").reset();
    } catch(err) {
        alert(err.message);
    }
}

function logoutUser() {
    localStorage.removeItem("access_token");
    localStorage.removeItem("user_role");
    window.location.href="/auth.html";
}
