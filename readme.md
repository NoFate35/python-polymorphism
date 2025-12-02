## Skill badges
![Poetry](https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
# About project
In this course, I have thoroughly examined polymorphism and its implementation mechanisms, and I have learned how to use it correctly.
### Topics to be considered:
* Subtype polymorphism;
* Parametric polymorphism;
* Dispatching and its types;
* Dependency inversion and injection;
* SOLID.
### Installation
The __poetry__ project manager must be installed to work with the project
```
git clone https://github.com/NoFate35/python-polymorphism.git
cd python-polymorphism
poetry install
make test
```
The tests should be run for each folder separately, like:
```
poetry run pytest factory_pattern -vv
```
the game_character_state task should be run with the _--capture=no_ flag:
```
poetry run pytest PROBATIONS/game_character_state --capture=no
```
### Related materials
https://ru.wikipedia.org/wiki/Принцип_единственной_ответственности

https://www.youtube.com/watch?v=wX6BBaQZpzE

https://github.com/Hexlet/patterns

https://ru.wikipedia.org/wiki/Антипаттерн

https://ru.hexlet.io/blog/posts/arhitektura-i-oop

https://ru.wikipedia.org/wiki/Принцип_разделения_интерфейса

https://ru.hexlet.io/courses/js-abp/lessons/fsm/theory_unit
