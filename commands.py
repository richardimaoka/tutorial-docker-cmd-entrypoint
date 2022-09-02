def dockerfile(filename):
    with open(filename, 'r') as f:
        contents = f.read()
        str = """
```dockerfile:{filename}
{contents}
```""".format(filename=filename, contents=contents).strip() + "\n"
    print(str)


def docker_commands(suffix, category):
    str = """

以下のコマンドを実行してください。

```sh
docker build -t {suffix} -f Dockerfile.{suffix} .
docker run {suffix}
```
""".format(suffix=suffix, category=category).strip() + "\n"
    print(str)


def template(suffix, category, result=None):
    dockerfile("Dockerfile." + suffix)
    docker_commands(suffix, category)
    if result is not None:
        print("""
```sh:docker runの結果        g
{result}
```
        """.format(result=result).strip() + "\n")


def main():
    template("cmd1", "cmd", "abc")  # CMD ["echo", "abc"]
    template("cmd2", "cmd")  # CMD ["cho", "abc", "def]
    template("cmd3", "cmd")  # CMD echo abc
    template("cmd4", "cmd")  # CMD echo abc def
    template("cmd5", "cmd")  # CMD echo "$HOME"
    template("cmd6", "cmd")  # CMD ["sh", "-c", "echo $HOME"]
    print("""
```sh
# SIGTERM not received with shell form
docker run nginx:1.21
```

以下のショートカットを実行してください。

```sh
# Ctrl + c 
```

以下のコマンドを実行してください。

````sh
docker build - t nginx: cmd-shellform - f Dockerfile.cmd-nginx .
docker run - -name cnt-nginx-shellform nginx: cmd-shellform
# Ctrl + c, not working!!
```

```sh:another terminal
docker stop cnt-nginx-shellform
""")
    template("cmd7", "cmd")  # CMD ["echo", "abc", "def]
    template("cmd8", "cmd")  # CMD["tail", "-f", "/dev/null"]
    template("cmd9", "cmd")  # CMD tail - f / dev/null


if __name__ == "__main__":
    main()
