# ranpass
Simple Random Password Generator CLI Tool.

### Requirements
This package requires Python 3 (it is 2021 after all). What else, let's see... a human to use it I guess? 

### Installing
To install this CLI tool you can clone this repo and then run the below command from within the directory
```
python setup.py install
```

Or alternatively, you can do
```
pip install ranpass
```

Both the above commands would install the package globally and `ranpass` will be available on your system.

### How to use
Generate a random password
```
ranpass generate -l <length of password desired> -o <option of password type>
```
There are four options for password type
1. Only lowercase alphabets
2. Lowercase + uppercase alphabets
3. Alphanumeric
4. Alphanumeric + Special characters (Default option, because passwords should be as secure as possible)

If you want to see these options in the terminal, run `ranpass generate -h`. You could also run `ranpass -h` to see the available commands. (`generate` is the only command right now).

### Feedback
Please feel free to leave feedback in issues/PRs.