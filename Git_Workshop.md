# Git/GUI Workshop Setup

## Repository Setup

1. Install Git following the steps [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
2. Verify that it installed correctly by running `git` in a terminal shell or command prompt window and verify that the command doesn't result in an error
3. Clone the Hyperloop repository (use SSH)
    * [Generate SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
    * [Add new SSH key to your account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
4. Navigate to the folder where you cloned the repository and verify that the file structure maches what is shown on GitHub


## GUI Setup
1. Install [VS Code](https://code.visualstudio.com), open the application, open the folder for the Hyperloop repository, and open a new terminal shell

2. Switch to the UI branch, pull any recent changes, and navigate to GUI folder
    ```
    git checkout UI
    git pull
    cd GUI
    ```

3. Install `python 3.9`

4. Create a virtual environment
    `python -m venv <environment_name>`
    * Example: `python -m venv gui_env`

5. Activate the virtual environment
    * MacOS/Linux: `source <environment_name>/bin/activate`
        * Example: `source gui_env/bin/activate`
    * Windows: `<environment_name>\Scripts\activate`
        * Example: `gui_env\Scripts\activate`

6. Install the required dependencies: `python -m pip install -r requirements.txt`

7. Run the GUI: `python main.py`
    * Members are _actively_ working on the GUI so feel free to comment out code that causes an error (it's probably currently being developed)

8. Deactivate the virtual environment (when finished working): `deactivate`
