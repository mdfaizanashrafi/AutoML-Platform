# 🤖 AutoML Platform – No-Code Machine Learning for Everyone

An end-to-end **AutoML system** designed to help **non-technical users** build, train, and deploy machine learning models **without writing code**.

🔧 Upload your dataset → ⚙️ Preprocess the data → 🧠 Train models → 🚀 Deploy predictions → 🎯 Visualize results

---

## 📌 Problem Statement

> **Non-technical users struggle to build machine learning models due to the lack of coding knowledge and complex ML workflows.**

---

## 💡 Solution

A user-friendly GUI-based AutoML platform that enables business analysts and domain experts to:
- Upload structured datasets via drag-and-drop
- Perform automated preprocessing
- Select and train ML models
- Tune hyperparameters visually
- Deploy trained models via API
- Visualize evaluation metrics and predictions

---
```
## 🌐 Tech Stack

| Layer         | Technology            | Purpose                             |
|--------------|------------------------|-------------------------------------|
| **Frontend** | PyQt5                  | Drag-and-drop GUI for user control  |
| **Backend**  | FastAPI                | ML processing APIs and orchestration |
| **ML/DL**     | Scikit-learn, TensorFlow | Classical ML and neural networks    |
| **Data**      | Polars                 | Fast preprocessing and validation   |
| **Database** | PostgreSQL             | Store models, metadata, user configs |
| **DevOps**    | Docker, Kubernetes     | Containerized microservices         |
| **CI/CD**     | Jenkins                | Automated retraining on new data    |

---
```
## 🚀 Features

- ✅ Drag-and-drop CSV upload interface
- ✅ Polars-powered preprocessing (null handling, encoding, scaling)
- ✅ Auto model selection based on data type
- ✅ Hyperparameter tuning sliders
- ✅ Real-time metric visualization (accuracy, ROC, confusion matrix, etc.)
- ✅ Model deployment as REST API
- ✅ PostgreSQL-backed model management
- ✅ Docker/Kubernetes support for scalable deployments
- ✅ Jenkins integration for automated retraining

---

## 📂 Project Structure (Modular & Scalable)
```
automl-platform/ 
    ├── backend/ # Core OOP modules for ML & preprocessing 
    ├── frontend/ # PyQt5 GUI code and layouts 
    ├── models/ # Saved trained models 
    ├── pipelines/ # Preprocessing + training pipeline files 
    ├── data/ # Uploaded and test datasets 
    ├── database/ # PostgreSQL connection and schemas 
    ├── docker/ # Dockerfiles and docker-compose config 
    ├── jenkins/ # Jenkinsfiles for automation 
    ├── k8s/ # Kubernetes manifests 
    ├── docs/ # Project documentation 
    ├── tests/ # Unit and integration tests 
    ├── requirements.txt # Python dependencies 
    ├── setup.cfg # Linter and formatter configuration 
    └── README.md # Project intro and setup guide
```


---

## 🚀 Getting Started

### 📦 Requirements
- Python 3.10+
- pip
- Docker & Docker Compose
- Git

### 🔃 Setup

git clone https://github.com/mdfaizanashrafi/automl-platform.git
cd automl-platform

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt



---

### 🛣️ `roadmap.md`

```markdown
# 🗺 Roadmap

- ✅ Phase 1: Project Initialization & Structure
- ⏳ Phase 2: PyQt GUI with Dataset Upload
- ⏳ Phase 3: OOP Backend for ML Pipeline
- ⏳ Phase 4: Model Training & Tuning Logic
- ⏳ Phase 5: Polars Preprocessing Module
- ⏳ Phase 6: Dockerize ML Microservices
- ⏳ Phase 7: Unit Testing & Logging
- ⏳ Phase 8: Kubernetes + Jenkins Setup
- ⏳ Phase 9: PostgreSQL Integration
- ⏳ Phase 10: Docs + Polish


# 🎯 Sample Use Case

1. User opens the GUI.
2. Drags and drops a CSV dataset.
3. Selects target variable and preprocessing options.
4. Chooses model type or lets the system auto-select.
5. Trains and evaluates the model with one click.
6. Deploys the model to a REST endpoint.
7. Retrieves predictions via API.


# 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to open:
- A Pull Request for code changes
- An Issue for bugs or suggestions



