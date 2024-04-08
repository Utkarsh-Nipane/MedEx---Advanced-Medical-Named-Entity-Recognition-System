![image](https://github.com/Devilreaper123/System-s-Integration/assets/67621176/2185640c-8408-4d2c-8d58-8ef592482891)

# Final Project : System's Integration

## Welcome to the GitHub Repository of Ronit Shahu!

This repository houses the code for our innovative project. Whether you're looking to contribute or simply explore, we're thrilled to have you here!

---

## Getting Started

These instructions will guide you through getting a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9 or Higher**: Essential for running the Python-based application.
- **pip**: The Python package installer, used for managing Python packages.

### Setting Up a Virtual Environment

Using a virtual environment is recommended to manage dependencies for your project. This ensures that your project's dependencies are kept separate from your system-wide Python packages.

#### 1. Install virtualenv

If you haven't installed `virtualenv` yet, install it using pip:

```bash
pip install virtualenv
```

#### 2. Create a Virtual Environment

Navigate to the project directory and create a virtual environment named `venv`:

```bash
virtualenv venv
```

#### 3. Activate the Virtual Environment

- **On Windows:**

  ```bash
  .\venv\Scripts\activate
  ```

- **On Unix or MacOS:**

  ```bash
  source venv/bin/activate
  ```

You should see `(venv)` appear at the beginning of your command line prompt, indicating that the virtual environment is active.

#### 4. Install Dependencies

With the virtual environment active, install the project dependencies:

```bash
pip install -r Requirements.txt
```

### Running the Application

With your virtual environment set up and dependencies installed, you're ready to run the application:
```bash
python api.py
```
and then run : 
```bash
streamlit run app.py
```

---
### Testing the Application

To test the model, use the file name:
```bash
Medicine data.txt
```
Since the data inside is used from Harvard's NLP dataset (n2c2 Challenge), it has been carefully extracted so as not to reveal any sensitive data (HIPAA Compliance). Unfortunatly more data cannot be revealed to maintain the NDA.

---

## Contributing

Your contributions are what make the community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

---

We hope this guide helps you get started with "Final Project : System's Integration". Happy coding!

---
