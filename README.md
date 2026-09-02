# Python Development Environments and Setup Guide

This guide covers the programming tools available for this module. **You are free to use any Python development environment that you prefer**. The examples and instructions work in any standard Python environment. While we provide Noteable for convenience, you may use any tool that can run Jupyter notebooks (.ipynb files).

In this module, you will develop code, primarily using the Jupyter Notebook programming environment. This is currently a very popular way of coding, especially in the field of data science. Jupyter has only been around since 2015 and has distinctive differences from other program-development tools.

Throughout this module, we provide a tool called Noteable which you can use to launch Jupyter Notebooks. As you work through each unit, you will find links to Noteable and will be given instructions on how to launch Jupyter Notebook activities using the tool.

Although this module has been designed so that all the exercises and assignments can be done using Jupyter, you should also have some knowledge of other ways that programs can be created.


## Development Environment Options


### Editing programs as text files

Program code is essentially the same as text, except that it must conform to the structure of some programming language. Each programming language has a **syntax** which determines the range of ways in which character symbols may be combined to produce a valid program. The language also has a **semantics** which determines what computations will take place when syntactically correct program code is executed.

One way to produce a program is to use a general-purpose, text-editing software tool. Many options exist, including Vim, Emacs, Notepad, Notepad++, Atom and Sublime Text. Most of these provide special editing modes for different types of file which furnish convenient functionality for working with files of these types. In particular, they usually have a Python mode that facilitates editing Python code.

### Integrated Development Environments (IDEs)

The design of a software tool to support programming can be taken further than just providing editing functions. The term **Integrated Development Environment** (usually abbreviated to **IDE**) refers to a software tool that is designed to support the whole process of creating programs, including editing, running and debugging, and also organising and combining different program components.

IDEs vary in complexity from simple combinations of the most useful functionality to extremely complicated systems which offer a huge variety of features (which most users will rarely, if ever, use). Most IDEs are primarily designed for a particular programming language but some support several languages. For example, [Eclipse](https://www.eclipse.org/) was designed for Java, but there is a plugin called [PyDev](https://www.pydev.org/) which enables Eclipse to be used for Python development; and Microsoft's [Visual Studio Code](https://code.visualstudio.com/) can also be used for Python.

One of the simplest and most easily accessible IDEs is [IDLE](https://docs.python.org/3/library/idle.html) which comes with most Python distributions. [Spyder](https://www.spyder-ide.org/) is a popular medium-complexity IDE that comes with the Anaconda distribution of Python and is well-suited for those who would like more features than IDLE but do not want something too elaborate. Somewhat more complex than Spyder, the [PyCharm](https://www.jetbrains.com/pycharm) IDE is very popular with professional Python developers.

The Linux operating system itself can be regarded as a kind of IDE since it provides a platform in which a wide range of tools dealing with all aspects of programming can be quite easily combined to provide a customised programming environment.

### Web-based programming

Instead of using locally-installed software, for some purposes, it is convenient to write and run code via a web interface. This interface links to a remote server that runs the code. A couple of examples are [Programiz Online Python](https://www.programiz.com/python-programming/online-compiler) and [w3schools Python Tutorial](https://www.w3schools.com/python).

These are more for beginners than for serious developers and may be quite limited with regard to code editing and organisation features. However, they have the advantage of allowing almost instant access to Python programming for anyone with a web browser.

As mentioned above, this module uses a web-based tool called Noteable for accessing Jupyter Notebook environments. Because it is online, you do not need to install anything on your own machine, and you can create your own notebooks there. Noteable will be the primary way in which you program in Python on this module, however, it's also a good idea to keep copies on your own machine, and if you want to view and run these outside of this module, you will need to install Jupyter Notebooks on your computer. The next reading provides a guide for this.

### Notebook programming

Support for the notebook style of programming is one of the main features of Jupyter Notebook. For the purposes of the current lesson, you only need to know that notebook programming environments provide a means for combining program code with accompanying documentation. This documentation can be used by the programmer to present any information relating to the code or to results obtained by running it.

Notebook programming can be seen as similar to a traditional kind of IDE software tool. However, Jupyter is actually implemented as a server program that creates an interface that is accessed via a web browser. This architecture is very flexible in that the Jupyter server can either be running locally on the same machine as the browser, or it can be running remotely on another machine.

### Collaborative web-based programming environments

Another advantage of server-based implementation of a programming interface is that it allows the possibility for multiple different machines (and people) to connect to the same server and have access to the same code. This means that code can potentially be developed collaboratively.

Platforms that support collaborative programming have become very popular recently. Among these are Google's [Colab](https://colab.research.google.com/), Microsoft's [Azure Notebooks](https://notebooks.azure.com/), and [Kaggle](https://www.kaggle.com/), the data science and machine learning community platform. All of these support Python and have interfaces very similar to the Jupyter Notebook interface that we shall be using.


## Working with Jupyter Notebooks in Noteable

For this module, you can use Noteable to open Jupyter Notebook (`.ipynb`) files. These notebooks, created by the tutor, offer both guidance and practice environments for your programming.

You may also use Anaconda to launch these notebook files, which will be necessary if you plan to program outside of this module. This page provides guidance specifically for launching Jupyter Notebooks via Noteable. Guidance on setting up Anaconda will be provided in the next section.

All Jupyter Notebook files for this module are stored in the University of Leeds GitHub repository (linked below). To open them in Noteable, you first need to clone the files from the GitHub repository and copy them into Noteable.

### Steps to clone and launch Jupyter Notebooks in Noteable:

1. Open Noteable via one of its URLs (these URLs are found on the main Minerva menu; the first you will come to is at **step 1.1.3**, but any of the Noteable links in the module will work and open an identical environment).
2. Select a personal notebook server from the drop-down menu. For this module, choose the **'Standard Python 3'** environment.
3. Select **'Start'**. If you have previously launched a Noteable server, you will be prompted to **'reconnect'** to it.
4. Once in the server environment, select **'Git'** from the top menu.
5. Choose **'Clone a repository'**.
6. Paste the URL of the University of Leeds GitHub repository (`https://github.com/Digital-Education-Service/GMD01-PfDS-Noteable`) into the input field.
7. Select **'Clone'**.

All the Jupyter Notebook files will now be cloned and appear in the file explorer on the left-hand side of Noteable. They will remain here unless manually deleted. Navigate through the folders to locate the files.

To launch a Jupyter Notebook, double-select the `.ipynb` from the file explorer, and follow the guidance on screen.

You will also encounter other files alongside the notebooks in these folders; these are necessary for certain notebooks to function properly and should always be kept in the same directory.

As you proceed through the module, you will be prompted to open specific notebook files depending on the activity you're working on. If you ever lose access to any notebook files, you can follow these steps again to re-clone them.

More information about using Noteable can be found on the [Edina website](https://noteable.edina.ac.uk/user-guide/#up_2).

### Completing other exercises in this module

Alongside the Jupyter Notebooks provided for this module, you will also come across smaller programming challenges and questions – usually labelled as 'exercises'. It is recommended that you use Noteable to complete these exercises, however, you should also be able to use any of the tools mentioned in this guide.

In order to open a blank Noteable environment, follow the guidance above but without cloning or uploading any pre-existing Jupyter Notebook files. This will give you an empty environment in which you can practise your code.

## Setting up Anaconda

The main way that you program in Python on this course will be using Jupyter Notebook in Noteable, and links to Noteable are provided when you are required to use Jupyter Notebook. However, you will need access to Python on your own computer if you want to write Python programs beyond this module.

We recommend that you install the free [Anaconda](https://www.anaconda.com/download) distribution of Python which will set up Python and lots of other useful tools for you. Installing Anaconda could take some time, so you may be able to continue working through the course content online while Anaconda is being downloaded and installed.

Anaconda includes several program development environments, including Jupyter Notebook, which will be the main way that we program in Python on this module. It also includes a large number of useful packages and a package manager. These extra packages allow you to include additional Python functionality beyond that included as standard in Python, and we will make use of some of these in this module. The package manager allows you to add new packages and any package 'dependencies', that is, other packages used by the one that you want.

Installing Anaconda should be fairly simple, but if you run into problems, we suggest you use the [Anaconda Support Center](https://anaconda.cloud/support-center) to try to find out how to fix the problem. Also, as with many computing and programming problems, asking a search engine is often a good way to get to an answer.

If you want to install Python by itself, you can get it from [www.python.org](https://www.python.org/), and this should be a much smaller download than Anaconda. However, installing Python in this way may not be as straightforward as Anaconda and you will need to write Python files in a text editor and run Python commands using the Python Interpreter. There is, however, extensive [Python documentation](https://docs.python.org/3/index.html) to support you.

**Task:** Now install Anaconda or Python on your computer.

### Starting Jupyter Notebook

The following will assume that you have installed Anaconda. There are several ways to start Jupyter Notebook, for example, by typing `jupyter notebook` in a terminal, or launching the Anaconda Navigator. If you're having trouble, have a look at the [Anaconda documentation](https://docs.anaconda.com/) or the [Jupyter documentation](https://jupyter-notebook.readthedocs.io/en/stable/), or ask a search engine.

Starting Jupyter Notebooks will launch the Notebook Dashboard in a web browser which may look like this:

![A screenshot of the Jupyter Notebook dashboard showing three tabs: 'Files', 'Running' and 'Clusters'. The 'Files' tab is selected and a number of folders are listed beneath it.](https://github.com/DES-ODL/OCOM5100M/raw/3be596ab3bb3e018388aa45c8eedfe058a7ad6a5/resources/content/resources/resources-images/Jupyter_Notebook_Dashboard_Screenshot.png)

Note that this is accessing information from your computer rather than the internet. The purpose of using a web browser to see things on your machine is so that Jupyter Notebook is platform-independent.

In the Notebook Dashboard, you should be able to see the folders/directories on your machine and navigate through them. If you want to open an `.ipynb` file that you've downloaded, you'll need to use the Notebook Dashboard to navigate to where you've saved it and select to open. Alternatively, you can create a new notebook by selecting the 'New' dropdown menu and selecting an option there, such as 'Python 3'.


---

## Introduction to Jupyter Notebook

### Introduction to Jupyter

You have now been provided with some information about the programming tools you will use in this module. In this video, Dr Jon Ward provides further explanation of Jupyter Notebook.

**VIDEO 1.1.6**

**Select the play button to start the video.**

- [View transcript (PDF)](https://minerva.leeds.ac.uk/bbcswebdav/pid-13276756-dt-content-rid83079377_4/xid-83079377_4)
- [View transcript (Word Doc)](https://minerva.leeds.ac.uk/bbcswebdav/pid-13276756-dt-content-rid83079376_4/xid-83079376_4)

---


## Summary: Your Choice

**The most important point**: You can complete all module work in any Python development environment. Whether you choose:
- Noteable (web-based, no installation)
- Anaconda with Jupyter Notebook (local, comprehensive)
- PyCharm or VS Code (professional IDEs)
- A simple text editor with Python
- Google Colab or another platform

...all are valid choices. The module content is designed to work with standard Python, so use the tools that work best for your learning style and preferences. Don't hesitate to experiment with different environments to find what suits you!
