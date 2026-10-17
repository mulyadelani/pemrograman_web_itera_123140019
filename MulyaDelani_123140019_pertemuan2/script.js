const STORAGE_KEY = "meja-kuliah-tasks";
const WEATHER_URL =
  "https://api.open-meteo.com/v1/forecast?latitude=-5.36&longitude=105.31&current_weather=true";
const QUOTE_URL = "https://dummyjson.com/quotes/random";

class TaskItem {
  constructor({ id, title, course = "", deadline, priority = "sedang", completed = false }) {
    this.id = id || (crypto.randomUUID ? crypto.randomUUID() : `${Date.now()}-${Math.random()}`);
    this.title = title;
    this.course = course;
    this.deadline = deadline;
    this.priority = priority;
    this.completed = completed;
  }
}

class DashboardApp {
  constructor() {
    this.storageMessage = document.querySelector("#storage-message");
    this.tasks = this.loadTasks();
    this.filter = "semua";
    this.editingId = null;
    this.form = document.querySelector("#task-form");
    this.list = document.querySelector("#task-list");
    this.bindEvents();
    this.render();
    this.startClock();
    this.loadWidgets();
  }

  loadTasks() {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (!saved) return [];
      const parsed = JSON.parse(saved);
      if (!Array.isArray(parsed)) throw new Error("Format data bukan daftar tugas.");
      return parsed.map((task) => new TaskItem(task));
    } catch (error) {
      this.showStorageMessage(
        `Data tersimpan tidak dapat dibaca: ${error.message}. Periksa penyimpanan browser Anda.`
      );
      return [];
    }
  }

  saveTasks() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(this.tasks));
      this.storageMessage.hidden = true;
    } catch (error) {
      this.showStorageMessage(
        `Perubahan belum tersimpan di browser: ${error.message}. Coba kosongkan ruang penyimpanan.`
      );
    }
  }

  showStorageMessage(message) {
    this.storageMessage.textContent = message;
    this.storageMessage.hidden = false;
  }

  bindEvents() {
    this.form.addEventListener("submit", (event) => {
      event.preventDefault();
      const formData = new FormData(this.form);
      const task = new TaskItem({
        title: formData.get("title").trim(),
        course: formData.get("course").trim(),
        deadline: formData.get("deadline"),
        priority: formData.get("priority"),
      });

      if (this.editingId) {
        this.tasks = this.tasks.map((item) =>
          item.id === this.editingId
            ? new TaskItem({ ...item, ...task, id: item.id, completed: item.completed })
            : item
        );
      } else {
        this.tasks = [...this.tasks, task];
      }
      this.saveTasks();
      this.resetForm();
      this.render();
    });

    document.querySelector("#f-cancel").addEventListener("click", () => this.resetForm());
    document.querySelector(".filters").addEventListener("click", (event) => {
      const button = event.target.closest("[data-filter]");
      if (!button) return;
      this.filter = button.dataset.filter;
      document.querySelectorAll("[data-filter]").forEach((chip) => {
        chip.classList.toggle("active", chip === button);
      });
      this.renderTasks();
    });

    this.list.addEventListener("click", (event) => {
      const button = event.target.closest("[data-action]");
      if (!button) return;
      const { action, id } = button.dataset;
      const task = this.tasks.find((item) => item.id === id);
      if (!task) return;

      if (action === "toggle") {
        this.tasks = this.tasks.map((item) =>
          item.id === id ? new TaskItem({ ...item, completed: !item.completed }) : item
        );
      } else if (action === "edit") {
        this.editTask(task);
        return;
      } else if (action === "delete") {
        this.tasks = this.tasks.filter((item) => item.id !== id);
        if (this.editingId === id) this.resetForm();
      }

      this.saveTasks();
      this.render();
    });
  }

  editTask(task) {
    this.editingId = task.id;
    this.form.elements.title.value = task.title;
    this.form.elements.course.value = task.course;
    this.form.elements.deadline.value = task.deadline;
    this.form.elements.priority.value = task.priority;
    document.querySelector("#form-title").textContent = "Edit tugas";
    document.querySelector("#f-submit").textContent = "Simpan perubahan";
    document.querySelector("#f-cancel").hidden = false;
    document.querySelector("#f-title").focus();
  }

  resetForm() {
    this.editingId = null;
    this.form.reset();
    document.querySelector("#form-title").textContent = "Tambah tugas";
    document.querySelector("#f-submit").textContent = "Tambah tugas";
    document.querySelector("#f-cancel").hidden = true;
  }

  render() {
    this.renderTasks();
    this.renderStats();
    this.renderNextTask();
  }

  renderTasks() {
    const visibleTasks = this.tasks
      .filter((task) => {
        if (this.filter === "aktif") return !task.completed;
        if (this.filter === "selesai") return task.completed;
        return true;
      })
      .sort((first, second) => first.deadline.localeCompare(second.deadline));

    if (!visibleTasks.length) {
      const messages = {
        semua: "Belum ada tugas. Tambahkan tugas kuliah pertamamu di sini.",
        aktif: "Semua tugas sudah beres. Waktunya istirahat sejenak!",
        selesai: "Belum ada tugas yang selesai. Semangat!",
      };
      this.list.innerHTML = `<li class="empty">${messages[this.filter]}</li>`;
      return;
    }

    this.list.innerHTML = visibleTasks
      .map((task) => {
        const overdue = !task.completed && task.deadline < this.today();
        let deadlineLabel = new Date(`${task.deadline}T00:00:00`).toLocaleDateString("id-ID", {
          day: "numeric",
          month: "short",
          year: "numeric",
        });
        deadlineLabel = `${overdue ? "Terlambat" : "Tenggat"} · ${deadlineLabel}`;
        return `
          <li class="task ${task.completed ? "is-done" : ""} ${overdue ? "is-overdue" : ""}">
            <button class="check" data-action="toggle" data-id="${this.escape(task.id)}"
              aria-label="${task.completed ? "Tandai belum selesai" : "Tandai selesai"}">
              ${task.completed ? "✓" : ""}
            </button>
            <div class="task-copy">
              <h3>${this.escape(task.title)}</h3>
              <p>${task.course ? `${this.escape(task.course)} <span aria-hidden="true">·</span> ` : ""}
                <span class="deadline">${deadlineLabel}</span></p>
            </div>
            <span class="priority priority-${this.escape(task.priority)}">${this.escape(task.priority)}</span>
            <div class="task-actions">
              <button class="icon-btn" data-action="edit" data-id="${this.escape(task.id)}" aria-label="Edit ${this.escape(task.title)}">Edit</button>
              <button class="icon-btn delete" data-action="delete" data-id="${this.escape(task.id)}" aria-label="Hapus ${this.escape(task.title)}">Hapus</button>
            </div>
          </li>`;
      })
      .join("");
  }

  renderStats() {
    const completed = this.tasks.filter((task) => task.completed).length;
    const active = this.tasks.length - completed;
    const progress = this.tasks.length ? Math.round((completed / this.tasks.length) * 100) : 0;
    document.querySelector("#stats").innerHTML = `
      <p class="eyebrow">RINGKASAN</p>
      <div class="stat-row"><span>Tugas aktif</span><strong>${active}</strong></div>
      <div class="stat-row"><span>Selesai</span><strong>${completed}</strong></div>
      <div class="progress-track" role="progressbar" aria-label="Progres tugas" aria-valuenow="${progress}" aria-valuemin="0" aria-valuemax="100">
        <span style="width: ${progress}%"></span>
      </div>
      <p class="progress-label">${progress}% dari semua tugas selesai</p>`;
  }

  renderNextTask() {
    const next = this.tasks
      .filter((task) => !task.completed)
      .sort((first, second) => first.deadline.localeCompare(second.deadline))[0];
    const container = document.querySelector("#next");
    container.innerHTML = next
      ? `<p class="eyebrow">FOKUS BERIKUTNYA</p>
         <h2>${this.escape(next.title)}</h2>
         <p>${next.course ? `${this.escape(next.course)} · ` : ""}Tenggat ${new Date(`${next.deadline}T00:00:00`).toLocaleDateString("id-ID", { day: "numeric", month: "long" })}</p>`
      : `<p class="eyebrow">FOKUS BERIKUTNYA</p><h2>Semua terkendali.</h2><p>Tambahkan tugas untuk mulai menyusun prioritas.</p>`;
  }

  startClock() {
    const update = () => {
      const now = new Date();
      document.querySelector("#clock").textContent = now.toLocaleTimeString("id-ID", {
        hour: "2-digit",
        minute: "2-digit",
      });
      document.querySelector("#date").textContent = now.toLocaleDateString("id-ID", {
        weekday: "long",
        day: "numeric",
        month: "long",
      });
    };
    update();
    setInterval(update, 60_000);
  }

  async loadWidgets() {
    const quoteElement = document.querySelector("#quote");
    const weatherElement = document.querySelector("#weather");
    const [quoteResult, weatherResult] = await Promise.allSettled([
      fetch(QUOTE_URL).then((response) => {
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return response.json();
      }),
      fetch(WEATHER_URL).then((response) => {
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return response.json();
      }),
    ]);

    if (quoteResult.status === "fulfilled") {
      const { quote, author } = quoteResult.value;
      quoteElement.innerHTML = `<span>“${this.escape(quote)}”</span><small>— ${this.escape(author)}</small>`;
    } else {
      quoteElement.textContent = `Kutipan belum dapat dimuat: ${quoteResult.reason.message}`;
      quoteElement.classList.add("widget-error");
    }

    if (weatherResult.status === "fulfilled" && weatherResult.value.current_weather) {
      const { temperature, windspeed, weathercode } = weatherResult.value.current_weather;
      weatherElement.innerHTML = `
        <p class="eyebrow">CUACA ITERA · LAMPUNG SELATAN</p>
        <div class="weather-temp">${Math.round(temperature)}<span>°C</span></div>
        <p>${this.weatherDescription(weathercode)} <span aria-hidden="true">·</span> Angin ${Math.round(windspeed)} km/jam</p>
        <small>Sumber: Open-Meteo</small>`;
    } else {
      const reason =
        weatherResult.status === "rejected"
          ? weatherResult.reason.message
          : "Data cuaca saat ini tidak tersedia.";
      weatherElement.innerHTML = `<p class="eyebrow">CUACA ITERA</p><p class="widget-error">Cuaca belum dapat dimuat: ${this.escape(reason)}</p>`;
    }
  }

  weatherDescription(code) {
    if (code === 0) return "Cerah";
    if ([1, 2, 3].includes(code)) return "Berawan";
    if ([45, 48].includes(code)) return "Berkabut";
    if ([51, 53, 55, 56, 57].includes(code)) return "Gerimis";
    if ([61, 63, 65, 66, 67, 80, 81, 82].includes(code)) return "Hujan";
    if ([71, 73, 75, 77, 85, 86].includes(code)) return "Salju";
    if ([95, 96, 99].includes(code)) return "Badai petir";
    return "Kondisi cuaca";
  }

  today() {
    const now = new Date();
    const localToday = new Date(now.getTime() - now.getTimezoneOffset() * 60_000);
    return localToday.toISOString().slice(0, 10);
  }

  escape(value) {
    return String(value).replace(/[&<>"']/g, (character) => {
      const entities = { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" };
      return entities[character];
    });
  }
}

document.addEventListener("DOMContentLoaded", () => new DashboardApp());