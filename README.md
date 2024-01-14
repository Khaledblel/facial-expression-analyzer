<div align="center">
<h1 align="center">
<br>Facial Expression Analyzer Web Application</h1>
This repository contains code for a simple web application that predicts facial expressions using a pre-trained deep learning model. The application is built using Flask for the server-side and TensorFlow.js for client-side image processing.
<h3>◦ Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white" alt="CSS" />
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python" />
<img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
<img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
<img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E" alt="JavaScript" />
<img src="https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white" alt="jQuery" />
<img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white" alt="TensorFlow.js" />
<img src="https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white" alt="Keras" />
</p>
<img src="https://img.shields.io/github/license/Khaledblel/facial-expression-analyzer?style=flat-square&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/Khaledblel/facial-expression-analyzer?style=flat-square&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/Khaledblel/facial-expression-analyzer?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/Khaledblel/facial-expression-analyzer?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>


##  📚 Table of Contents
- [Introduction](#-Introduction)
- [Features](#-features)
-  [Dependencies](#-dependencies)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Usage](#-Usage)
- [Contributing](#-Contributing)
- [License](#-license)


## 🌟 Introduction

The **Facial Expression Analyzer** is a web application that allows users to upload an image containing a face, and it predicts the emotion expressed in the face. The deep learning model used for prediction has been pre-trained to recognize seven different emotions: Anger, Disgust, Fear, Happy, Sad, Surprise, and Neutral.

## ✨ Features

- 🖼️ Image upload for emotion prediction
- ⚙️ Real-time prediction using TensorFlow.js
- 🎨 Simple and intuitive user interface

🛠️ Dependencies
----------------

-   Flask
-   TensorFlow
-   jQuery
-   TensorFlow.js
-   NumPy
-   Jinja2
-   OpenCV
-   Pillow


📂 Project Structure
--------------------

-   📁 templates: Contains HTML templates for the web application.
-   📁 static: Holds static files such as stylesheets and JavaScript code.
-   📄 app.py: Flask application file with the server-side logic.
-   📄 model_filter.h5: Pre-trained deep learning model for emotion prediction.
-   📄 requirements.txt: Lists all Python dependencies needed for the project.

## 🚀 Getting Started

1. Clone the facial-expression-analyzer repository:
```sh
git clone https://github.com/Khaledblel/facial-expression-analyzer
```

2. Change to the project directory:
```sh
cd facial-expression-analyzer
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

4. Running facial-expression-analyzer
```sh
python app.py
```


🤖 Usage
--------

1.  Open the web application in your browser.
2.  Click on the "Choose File" button to upload an image containing a face.
3.  Press the "Analyze" button to predict the emotion in the uploaded image.
4.  View the predicted emotion displayed on the page.



## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/Khaledblel/facial-expression-analyzer/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/Khaledblel/facial-expression-analyzer/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/Khaledblel/facial-expression-analyzer/issues)**: Submit bugs found or log feature requests for KHALEDBLEL.

#### *Contributing Guidelines*

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>





📄 License
----------

This project is licensed under the GPLv3 License
