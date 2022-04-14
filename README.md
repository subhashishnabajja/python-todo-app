# A (very) simple todo app made with [Python](https://www.python.org/) and [Tkinter](https://tkdocs.com/)

## Starting the app

1. Clone the repository.

```bash
git clone <repo-link>
```

2. Start the command line and enter the following command (Make sure that you've installed **Python** and `pip` on your system).
   This will install all the required packages.

```bash
pip install -r ./requirements.txt
```

4. Now setup the environment variables. Create `.local.env` at the root. Enter the following text in the file.
   The app is made with `Mysql` as the primary database. Ther efore setup and start the `Mysql` database before starting the app.

```env
DATABASE_USER=<your-username>
DATABASE_PASSWORD=<your-password>
DATABASE_NAME=<your-database-name>
```

5. The final step is to run the actual app. Run the following command.

```bash
python main.py
# OR
python3 main.py
```

## Creating a user

When starting the app for the first time it asks you to create a user.

![Create user Form]("https://github.com/subhashishnabajja/todo-app/blob/main/images/create-vault.png")

After creating the user you will be presented with main application window. You now add and delete todo. Enjoy ❤.

![Main]("https://github.com/subhashishnabajja/todo-app/blob/main/images/main-app.png")
