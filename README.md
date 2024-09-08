# Stock Management Backend

This is the backend application for the Stock Management system. It provides an API for managing stocks, including CRUD operations and pagination. The application is built with Flask and uses MongoDB for data storage.

- Live Site - https://stock-frontend-5yat.onrender.com/

## Features

- CRUD operations for stocks

## Prerequisites

Ensure you have the following installed on your machine:

- [Python](https://www.python.org/) (v3.8 or higher recommended)
- [MongoDB](https://www.mongodb.com/try/download/community) (installed and running)

## Getting Started

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo/backend
```

### 2. Create a Virtual Environment



```bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
Copy code
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

```bash
Copy code
MONGO_URL=mongodb://localhost:27017/stocks_db
This specifies the MongoDB connection URL.
```

### 5. Run the Flask Application

```bash
Copy code
flask run
The API will be available at http://localhost:5000.
```

### 6. Running Tests (Optional)

```bash
Copy code
pytest
Make sure you have pytest installed (pip install pytest).
```

# Stock Management Frontend

This is the frontend application for the Stock Management system. It allows users to manage a list of stocks with features like adding, updating, deleting, and paginating through stock entries. The application is built with React and styled using Tailwind CSS.

## Features

- Add new stocks
- View and list existing stocks
- Edit and delete stocks


## Prerequisites

Ensure you have the following installed on your machine:

- [Node.js](https://nodejs.org/) (v16.x or higher recommended)
- [npm](https://www.npmjs.com/) (comes with Node.js) or [yarn](https://yarnpkg.com/) (optional)

## Getting Started

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo/frontend

npm install
# or if you use yarn
yarn install

REACT_APP_API_URL=http://localhost:5000

npm start
# or if you use yarn
yarn start

npm run build
# or if you use yarn
yarn build
```
