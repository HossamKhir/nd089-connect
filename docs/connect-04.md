---
marp: true
theme: gaia
class: gaia
color: black
---

<!--
_class:
  - gaia
  - lead
-->

# AI Programming with Python

![bg right](https://www.udacity.com/www-proxy/contentful/assets/2y9b3o528xhq/2dmDLmWvCncVHcQ6lz9u5v/9ebc8c914fcf0e8b546bce78133b2a4a/OpenGraph_Udacity_Logo_Update__1_.png)

## Session 4

[attendance](../README.md)

---

<!--
_class:
  - gaia
  - lead
-->

![bg right:33%](https://www.gannett-cdn.com/presto/2019/01/07/USAT/e6caf4d6-83e2-4d98-a91a-85a25eca03da-ginni2017_downloadimage_with-background_780x981.jpg)

> Some people call this artificial intelligence, but the reality is this technology will enhance us.
> So instead of artificial intelligence, I think we'll augment our intelligence.

# [Gini Rometty](https://en.wikipedia.org/wiki/Ginni_Rometty)

---

# Agenda

- Q&A
- Review
  - Anaconda
  - Jupyter Notebooks
- Q&A _(encore)_

---

# Anaconda: environment management

- `conda create -n` ENV_NAME \[python=X.x\] \[PACKAGE_LIST\]
- `conda activate` ENV_NAME
- `conda list` \[-n ENV_NAME\] \[PACKAGE_LIST\]
- `conda deactivate`
- `conda env export` > ENV.yaml
- `conda env create -f` ENV.yaml
- `conda env list` &amp; `conda info --envs`
- `conda env remove -n` ENV_NAME

---

> N.B: On removing environments, make sure the target environment is not active in the current session

---

# Anaconda: package management

> An environment must be active to use package management

- `conda list`
- `conda install` \[PACKAGE_NAME \[PACKAGE_NAME\]&#8230;\]
- `conda remove` \[\[PACKAGE_NAME\]&#8230;\]
- `conda update` \[\[PACKAGE_NAME\]&#8230;\] &amp; `conda update --all`
- `conda search` \[QUERY_PACKAGE\]

---

# Jupyter

> **Ju**lia, **Pyt**hon, **R**

```sh
cd path/to/notebooks/directory
python3 -m jupyter notebook # also jupyter notebook should work
```

```sh
python3 -m jupyter nbconvert --to html notebook.ipynb
```

---

<!--
_class:
  - gaia
  - lead
-->

# Q&A _(encore)_ <!-- fit -->

---

<!--
_class:
  - gaia
  - lead
 -->

# Thank You

## Good Luck

## Have Fun
