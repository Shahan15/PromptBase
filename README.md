# 🧠 PromptBase — AI Prompt Refinement & Management App

PromptBase is a full-stack application that allows users to create, refine, save, and manage AI prompts.
It integrates with OpenAI/Gemini for prompt optimisation and uses Supabase for authentication and persistent storage.

---

## 🚀 Features

### ✨ Prompt Tools

* Create AI prompts
* Refine prompts using OpenAI/Gemini API
* Save prompts to your account
* Mark prompts as favourites
* Reuse previously saved prompts
* Categorise prompts (optional)

### 👤 User Accounts

* Supabase Auth for sign-up/login
* User-specific prompt storage
* Secure handling of API keys via `.env`

### 🗂️ Database

Powered by **Supabase**, with tables such as:

* `prompts`
* `favourites`
* `users` (handled by Supabase auth)

---

## 🔌 Supabase Client

The backend uses a small ORM-like helper class to communicate with Supabase.
It provides clean functions for database operations:

* `insert(table, data)`
* `fetch(table, filters)`
* `update(table, filters, updates)`
* `delete(table, filters)`

This keeps all database logic consistent and reusable across the application.

---

## 🔑 Environment Variables

Your `.env` file should include:

```
SUPABASE_URL=your-url-here
SUPABASE_KEY=your-key-here
OPENAI_API_KEY=your-openai-key
```

⚠️ Make sure your `.env` is in `.gitignore`.

---

## 🛠️ Installation & Setup

### 1. Clone the repo

```
git clone <your-repo-url>
cd PromptBase
```

### 2. Create & activate a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add your `.env` file

Create a `.env` file in the root directory.

### 5. Run the backend

```
python main.py
```

(or whichever entrypoint you use)

---

## 🧪 Example Backend Flow

1. User submits a prompt
2. Backend sends prompt → OpenAI/Gemini
3. API returns refined prompt
4. Backend saves prompt in Supabase using `SupabaseClient`
5. Frontend displays results
6. User can favourite, edit, or delete saved prompts

---
# 🧠 PromptBase — AI Prompt Refinement & Management App

PromptBase is a full-stack application that allows users to create, refine, save, and manage AI prompts.
It integrates with OpenAI/Gemini for prompt optimisation and uses Supabase for authentication and persistent storage.

---

## 🚀 Features

### ✨ Prompt Tools

* Create AI prompts
* Refine prompts using OpenAI/Gemini API
* Save prompts to your account
* Mark prompts as favourites
* Reuse previously saved prompts
* Categorise prompts (optional)

### 👤 User Accounts

* Supabase Auth for sign-up/login
* User-specific prompt storage
* Secure handling of API keys via `.env`

### 🗂️ Database

Powered by **Supabase**, with tables such as:

* `prompts`
* `favourites`
* `users` (handled by Supabase auth)

---

## 🔌 Supabase Client

The backend uses a small ORM-like helper class to communicate with Supabase.
It provides clean functions for database operations:

* `insert(table, data)`
* `fetch(table, filters)`
* `update(table, filters, updates)`
* `delete(table, filters)`

This keeps all database logic consistent and reusable across the application.

---

## 🔑 Environment Variables

Your `.env` file should include:

```
SUPABASE_URL=your-url-here
SUPABASE_KEY=your-key-here
OPENAI_API_KEY=your-openai-key
```

⚠️ Make sure your `.env` is in `.gitignore`.

---

## 🛠️ Installation & Setup

### 1. Clone the repo

```
git clone <your-repo-url>
cd PromptBase
```

### 2. Create & activate a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add your `.env` file

Create a `.env` file in the root directory.

### 5. Run the backend

```
python main.py
```

(or whichever entrypoint you use)

---

## 🧪 Example Backend Flow

1. User submits a prompt
2. Backend sends prompt → OpenAI/Gemini
3. API returns refined prompt
4. Backend saves prompt in Supabase using `SupabaseClient`
5. Frontend displays results
6. User can favourite, edit, or delete saved prompts

---

## 📦 Roadmap

* [ ] Add prompt search
* [ ] Add categories/tags
* [ ] Add prompt version history
* [ ] Add analytics dashboard
* [ ] Deploy to production

---

## 💬 Contact

For questions or improvements, reach out anytime.

## 📦 Roadmap

* [ ] Add prompt search
* [ ] Add categories/tags
* [ ] Add prompt version history
* [ ] Add analytics dashboard
* [ ] Deploy to production

---

## 💬 Contact

For questions or improvements, reach out anytime.
