from http.cookies import Morsel


def dockerfile(filename):
    with open(filename, 'r') as f:
        contents = f.read()
        str = """
```dockerfile:{filename}
{contents}
```""".format(filename=filename, contents=contents).strip() + "\n"
    print(str)


def docker_commands(suffix, extra_args):
    more_args = ""
    if len(extra_args) != 0:
        for arg in extra_args:
            more_args += " " + arg

    str = """

```:以下のコマンドを実行してください
docker build -t {suffix} -f Dockerfile.{suffix} .
docker run --rm {suffix}{more_args}
```
""".format(suffix=suffix, more_args=more_args).strip() + "\n"
    print(str)


def template(suffix, result=None, extra_args=[]):
    dockerfile("Dockerfile." + suffix)
    docker_commands(suffix, extra_args)
    if result is not None:
        print("""
```:コマンドの実行結果
{result}
```
""".format(result=result).strip() + "\n")


def nginx():
    print("""

```:以下のコマンドを実行してください
docker run nginx:1.23.1
```

これで、nginx によるウェブサーバーが立ち上がります。

```:コマンド実行結果
2022/09/03 07:14:58 [notice] 1#1: using the "epoll" event method
2022/09/03 07:14:58 [notice] 1#1: nginx/1.23.1
2022/09/03 07:14:58 [notice] 1#1: built by gcc 10.2.1 20210110 (Debian 10.2.1-6)
2022/09/03 07:14:58 [notice] 1#1: OS: Linux 5.10.102.1-microsoft-standard-WSL2
2022/09/03 07:14:58 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2022/09/03 07:14:58 [notice] 1#1: start worker processes
2022/09/03 07:14:58 [notice] 1#1: start worker process 31
2022/09/03 07:14:58 [notice] 1#1: start worker process 32
2022/09/03 07:14:58 [notice] 1#1: start worker process 33
2022/09/03 07:14:58 [notice] 1#1: start worker process 34
2022/09/03 07:14:58 [notice] 1#1: start worker process 35
2022/09/03 07:14:58 [notice] 1#1: start worker process 36
2022/09/03 07:14:58 [notice] 1#1: start worker process 37
2022/09/03 07:14:58 [notice] 1#1: start worker process 38
```

nginx を停止してみましょう。

```:以下のショートカットを実行してください
Ctrl + c
```

これで SIGINT が送られ…

```:ショートカット実行結果
2022/09/03 07:15:40 [notice] 1#1: signal 2 (SIGINT) received, exiting
2022/09/03 07:15:40 [notice] 1#1: signal 14 (SIGALRM) received
...
...
2022/09/03 07:15:40 [notice] 1#1: worker process 38 exited with code 0
2022/09/03 07:15:40 [notice] 1#1: exit
```

…nginx が停止しました。


Ctrl+c できれいに停止できるのは、nginx の docker イメージが CMD の exec form を使っているからです。

```:以下のコマンドを実行してください
docker inspect nginx
```

CMD の exec form を使っていることが確認できます。

```:コマンド実行結果
"Config": {
    "Cmd": [
        "nginx",
        "-g",
        "daemon off;"
    ]
}
```

""")


def nginx_nonstop():
    print("""
```:以下のショートカットを実行してください
Ctrl + c
```

```実行結果
2022/09/03 05:48:46 [notice] 7#7: start worker process 13
2022/09/03 05:48:46 [notice] 7#7: start worker process 14
2022/09/03 05:48:46 [notice] 7#7: start worker process 15
^C
```

nginx が停止しません！

コレを停止するには、別ターミナルでdocker stopを実行する必要があります。

```:別ターミナルで、以下のコマンドを実行してください
docker stop cnt-cmd-nginx
```

先ほどと違って`signal 2 (SIGINT) received, exiting`とは表示されずに、急にnginxのログが出力されなくなり停止しているのがわかると思います。

```コマンド実行結果
2022/09/03 05:48:46 [notice] 7#7: start worker process 14
2022/09/03 05:48:46 [notice] 7#7: start worker process 15
```

""")


def main():
    # template("cmd1",  "abc")  # CMD ["echo", "abc"]
    # template("cmd2",  "abc def")  # CMD ["cho", "abc", "def]
    # template("cmd3",  "abc")  # CMD echo abc
    # template("cmd4",  "abc def")  # CMD echo abc def
    # template("cmd5",  "/home/your_username")  # CMD echo "$HOME"
    # template("cmd6", "/home/your_username")  # CMD ["sh", "-c", "echo $HOME"]
    # nginx()
    # template("cmd-nginx")  # CMD ["sh", "-c", "echo $HOME"]
    # nginx_nonstop()
    # template("cmd7")  # CMD tail - f / dev/null
    # template("cmd8")  # CMD["tail", "-f", "/dev/null"]

    # template("entrypoint1",  "abc")  # ENTRYPOINT ["echo", "abc"]
    # template("entrypoint2",  "abc def")  # ENTRYPOINT ["cho", "abc", "def]
    # template("entrypoint3",  "abc")  # ENTRYPOINT echo abc
    # template("entrypoint4",  "abc def")  # ENTRYPOINT echo abc def
    # template("entrypoint5",  "/home/your_username")  # ENTRYPOINT echo "$HOME"
    # # ENTRYPOINT ["sh", "-c", "echo $HOME"]
    # template("entrypoint6", "/home/your_username")
    # template("entrypoint-nginx1")  # ENTRYPOINT [ "nginx", "-g", "daemon off;"]
    # template("entrypoint-nginx2")  # ENTRYPOINT nginx -g "daemon off;"
    # template("entrypoint7")  # ENTRYPOINT tail - f / dev/null
    # template("entrypoint8")  # ENTRYPOINT["tail", "-f", "/dev/null"]

    template("cmd-and-entrypoint1",  "abc")  # ENTRYPOINT ["echo", "abc"]
    template("cmd1",  "ERROR")
    template("entrypoint1", "abc def", ["def"])
    template("cmd-and-entrypoint2")
    template("cmd-and-entrypoint3")


if __name__ == "__main__":
    main()
