[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

<div align="center">
  <a href="#">
    <img src="https://media0.giphy.com/media/G1ifnX4d5tYFACktp9/giphy.gif?cid=ecf05e47vy5sj6l8po69dt2xjl9cf6qv9gslsueejm9hhvrr&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="Logo" width="200" height="200">
  </a>
  <h3 align="center">Data Science</h3>
  <p align="center">First Evaluation Activity</p>

</div>

## 🔰 Getting Started

This project was created to perform a data extraction process from the Steam WEB API in Python.

<br/>

### 💾 Tools Used

[![vscode][vscode]][vscode-url]

### 🤖 Technologies used

[![Python][Python]][Python-url]

### 📋 Prerequisites

- 🐍Python

>💡Attention
>
> There is a ```requirements.txt``` file, where all dependencies are listed.
>
>Just run the ```install_requirements.bat``` (if on windows) or ```install_requirements.sh``` (if on linux) script to install the dependencies listed in that file.

<br/>

## 🎨 Features
The application has the following functionality:



### 🛠️ Search and Extract Data
By running the process with the ```-s``` flag you run the program in a way that searches for data on the Steam market through the WEB API.
It will be necessary to provide an AppID, identified by the ```-a``` flag and, optionally, a search string, if you want to search for specific items, identified by the ```-q``` flag.

The usage would be basically:
```python -u main.py -s -a XXX -q SSSS```

#### Exemplo:
``` 
python -u main.py -s -a 730 -q AK-47
python -u main.py -s -a 570
```

If main.py is executed within the project folder, manually, the data will be stored in the ```data``` folder partitioned by AppID.

<br/>

## 📑 Licenses

Distributed under the MIT License. See `LICENSE` for more information.

<br/>

## 🧻 TODOs
- [ ] Add functionality to save data from the project folder, not from the execution environment
- [ ] Add optional parameterization for pagination size of the search module (default is set to 100)

<!-- ASSETS -->

<!-- BADGE - Contributors -->

[contributors-shield]: https://img.shields.io/github/contributors/toledkrw/Aula-DataScience-Trabalho1.svg?style=for-the-badge
[contributors-url]: https://github.com/toledkrw/Aula-DataScience-Trabalho1/graphs/contributors

<!-- BADGE - Issues -->

[issues-shield]: https://img.shields.io/github/issues/toledkrw/Aula-DataScience-Trabalho1.svg?style=for-the-badge
[issues-url]: https://github.com/toledkrw/Aula-DataScience-Trabalho1/issues

<!-- BADGE - License -->

[license-shield]: https://img.shields.io/github/license/toledkrw/Aula-DataScience-Trabalho1.svg?style=for-the-badge
[license-url]: https://github.com/toledkrw/Aula-DataScience-Trabalho1/blob/main/LICENSE

<!--  -->
<!-- TECHNOLOGIES -->
<!--  -->

<!-- BADGE - Python -->

[Python]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

<!-- BADGE - vscode -->

[vscode]: https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white
[vscode-url]: https://code.visualstudio.com/
