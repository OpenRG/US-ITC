# US-ITC Advanced Python Training

|  | [Jason DeBacker](http://jasondebacker.com) |
|--------------|--------------------------------------------------------------|
| Email | [jason.debacker@openrg.com](mailto:jason.debacker@openrg.com) |
| GitHub | [jdebacker](https://github.com/jdebacker) |

## Course description ##

This training is intended to provide Economists at the USITC with instructions on advanced modeling and data management techniques in Python. Participants will learn skills and to use tools that will make their code more efficient and better able to leverage the USITC’s high speed computational environment. A portion of the training will include a code review (see module 1e), where Commission staff will provide a dataset and code for a sample model and the class will work through revising the code to make it more efficient.

## Daily Schedule ##

The training will be held from 9:00am to 5:30pm each day.  The schedule will include a lunch break from 12:00pm to 1:30pm.  We'll take a 15 minute break in the morning and afternoon.  Jason will hold "office hours" from 4:30pm to 5:30pm each day for participants to ask questions or get help with their code.

## Course Schedule and Topics ##


| Date     | Day | Topic                                  |
|----------|----------------------------------------|--------|
| Oct. 16  | W  | Numerical Optimization Methods          |
|   |   | SciPy: Optimizers and Rootfinders          |
|   |   | Applying optimization methods: GMM and MLE          |
|   |   |  Job Search Model: Theory          |
| Oct. 17  | Th  | Dynamic Programming in Python: Job Search Model         |
|   | | Brute Force: VFI and PFI |
|   | | Using Just in Time Compilation with Numba |
   |   | | Using the GPU with Jax           |
|   | |  Parallel Computing with Dask          |
|   |   |  Application: Estimating a job search model with SMM          |
| Oct. 18  | F  |  Efficient Methods with Big Data: Dask DataFrames          |
|   |   | Parameter Validation with ParamTools          |
|   |  |  Applying new techniques to existing code       |
| Future |   |  Best practices with Sparse Matrices          |
|   |   | Optimizing Development Workflow  |
|  |   |  Unit Tests and Continuous Integration Testing          |
|   |   |  Documentation Tools         |


## Course Prep  ##

### Software Installation ###
To get the most out of this training, participants should have the following installed on their computers:

#### Installing Python ####
We recommend that you download the Anaconda distribution of Python provided by [Anaconda](https://www.anaconda.com/download). We also recommend the most recent stable version of Python, which is currently Python 3.12. This can be done from the [Anaconda download page](https://www.anaconda.com/download) for Windows, Mac OSX, and Linux machines. The code we will be writing uses common Python libraries such as `NumPy`, `SciPy`, `pickle`, `os`, `matplotlib`, and `time`, which are all included in the Anaconda distribution. If you are using a different distribution of Python, you may need to install these packages separately.

#### Text Editor ####

In our recommended Python development workflow, you will write Python scripts and modules (`*.py` files) in a text editor. Then you will run those scripts from your terminal. You will want a capable text editor for developing your code. Many capable text editors exist, but we recommend [Visual Studio Code](https://code.visualstudio.com) (VS Code). As you progress through this training program, you will also use Python interactively in a Jupyter Notebook or iPython session. VS Code will be helpful here as well as it will allow you open Jupyter Notebooks and run Python interactively through the text editor.

VS Code is free and will be included with your installation of Anaconda. This is a very capable text editor and will include syntax highlighting for Python and and built in Git controls. In addition to the basics, you may want to use a more advanced linter for Python. This will help you correct syntax errors on the fly and provide helpful information as you declare objects and call functions. [This link](https://code.visualstudio.com/docs/python/linting) provides step-by-step instructions on using more advanced linting in VS Code.

Some extensions that we recommend installing into your VS Code:
* `cornflakes-linter`
* Git Extension Pack
* GitLens
* Jupyter
* Markdown All in One
* Pylance

In addition, [GitHub Copilot](https://github.com/features/copilot) is an amazing resource and can be added as an extension to VS Code. However, this service is not free of charge and does require an internet connection to work.

### Python Basics ###

In addition, the October training days assume some familiarity with Python and some of the packages that are most used in data science and economics.  These include the standard library, Numpy, Pandas, and Matplotlib.  Materials to get you up to speed on these can be found in the first several chapters of the [United Nations OG-Core Overlapping Generations Model Training](https://eapd-drb.github.io/UN-OG-Training/) tutorial.

There  are several ways to interact with Python:

1. [Jupyter Notebook](https://jupyter.org/)
2. iPython session
3. Running a Python script from the command line
4. Running a Python script from an IDE such as [Spyder](https://www.spyder-ide.org/).

While you may pick the method that works best for you, the instructor will primarily be using Jupyter Notebooks or by writing in VS Code and executing the source code in the command line.  You should be able to follow along with any of these methods.