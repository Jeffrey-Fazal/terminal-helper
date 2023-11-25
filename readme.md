# Terminal Helper

A command-line assistant built in Python that utilizes the OpenAI API to provide concise answers to user queries about terminal commands and other queries. Through a simple prompt, it asks the user a question and returns an answer after asking OpenAI.

## Setup

1. Install the OpenAI library:

```bash
pip install openai
```

2. Open `credentials.py.sample` and add your organization key and API key.

3. Rename `credentials.py.sample` to `credentials.py`.

## Usage

1. Run the script using Python:

```bash
python terminalhelper.py
```

2. Ask for a command like you would to a person.

## Add to alias

(Optional) Add the script to your alias file to easily summon it from the command line.
To add the script to your alias file and easily summon it from the command line in Linux, follow these steps:

1. **Locate your alias file:** The default alias file for most Linux distributions is `~/.bashrc`. You can open this file using a text editor like Nano or Vim:

```bash
nano ~/.bashrc
```

2. **Add the alias:** At the end of the file, add the following line:

```
alias terminalhelper="python /path/to/terminalhelper.py"
```

Replace `/path/to/terminalhelper.py` with the actual path to your `terminalhelper.py` script. For example, if the script is in your home directory, you would use:

```
alias terminalhelper="python ~/terminalhelper.py"
```

3. **Save the alias file:** Save and close the alias file.

4. **Reload your aliases:** To make the alias changes take effect, you need to reload your aliases. You can do this by logging out and back in, or by running the following command:

```bash
source ~/.bashrc
```

Now, you can invoke the script simply by typing `terminalhelper` in your terminal.