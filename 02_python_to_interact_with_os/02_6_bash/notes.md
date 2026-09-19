# Signaling process

- `Ctrl-C`: Send an interrupt signal `SIGINT` to the program. This won't forcibly terminate the program, but will signal it to finish whatever it's doing and shut down.

- `Ctrl-Z`: Send a pause signal `SIGSTOP`. The program stops but isn't terminated. You can bring up the last `SIGSTOP`'d program in a terminal by running `fg`.

- `kill <pid>`: Send a `SIGTERM` to politely request a program to shut down.


# Conditionals & Loops

## Conditionals

```bash
if command; then
    # run if `command` returns exit code 0 (succeed)
else
    # run if `command` returns other exit codes (failed)
fi
```

## Loops

```bash
while command; do
    # run if command returns exit code 0.
    # loop breaks if command returns non-zero exit codes (failed).
done
```

```bash
for val in myarray; do
    # ...
done

```

## `test` command

Evaluates a given condition. Exits with:
- `0` if condition is **True**
- `1` if condition is **False** 

Syntax: `test <condition>` or `[ condition ]`

## Arithmetic operations

- Placed within double parentheses: `((<operation>))`

- Not necessary if variable is declared as int or float (see below)


> [!NOTE]
> Variables are of `string` type by default, even without double quotes `"`. To declare other var types, use the `declare` command.
