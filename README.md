<h1 align="center">MapReduce Word Count</h1>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)

<br />

## 🧐 About <a name = "about"></a>
A naive implementation to better understand the **MapReduce** paradigm.

MapReduce is a programming model for processing and generating big data sets with a parallel, distributed algorithm on a cluster.

The "MapReduce System" is usually composed of three functions (or steps):
**Map**: The map function, also referred to as the map task, processes a single key/value input pair and produces a set of intermediate key/value pairs.
**Shuffle**: The shuffle function transfer data from Mapper to Reducer. It is a mandatory operation for reducers to proceed their jobs further as the shuffling process serves as input for the reduce tasks.
**Reduce**: The reduce function, also referred to as the reduce task, consists of taking all key/value pairs produced in the map phase that share the same intermediate key and producing zero, one, or more data items.

## 🏁 Getting Started <a name = "getting_started"></a>

Use the Pipfile to install packages in the virtualenv:

```
pipenv install --dev
```

<br />

## 💻 Usage <a name="usage"></a>
Run the MapReduce example:
```
pipenv run wordcount
```

<br />

## 🐛 Test <a name = "deployment"></a>
Run Unit and Integration tests
```
pipenv run test
```

<br />

## ⛏️ Built Using <a name = "built_using"></a>

- [Pipenv](https://pipenv.pypa.io/en/latest/) | virtualenv and  packaging
- [Pytest](https://docs.pytest.org/en/7.1.x/) | testing

<br />

## ✍️ Authors <a name = "authors"></a>

- [@vittoriopolverino](https://github.com/vittoriopolverino)
