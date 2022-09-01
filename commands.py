def template(suffix, category, comment) -> str:
    str = """
# {comment}
docker build -t {suffix} -f Dockerfile.{suffix} .
docker images --filter=reference='{category}*'
docker run {suffix}
docker inspect {suffix} --format='CMD {{.Config.Cmd}}'
""".format(comment=comment, suffix=suffix, category=category).strip() + "\n"

    print(str)


def main():
    template("cmd1", "cmd", 'CMD ["echo", "abc"]')
    template("cmd2", "cmd", 'CMD ["cho", "abc", "def]')
    template("cmd3", "cmd", 'CMD echo abc')
    template("cmd4", "cmd", 'CMD echo abc def')
    template("cmd5", "cmd", 'CMD echo "$HOME"')
    template("cmd6", "cmd", 'CMD ["sh", "-c", "echo $HOME"]')
    print("""
# SIGTERM not received with shell form
docker run nginx: 1.21
# Ctrl + c works

docker build -t nginx:cmd-shellform -f Dockerfile.cmd-nginx .
docker run --name cnt-nginx-shellform nginx:cmd-shellform
# Ctrl + c, not working!!

# another terminal
docker stop cnt-nginx-shellform
""")
    template("cmd7", "cmd", 'CMD ["echo", "abc", "def]')
    template("cmd7", "cmd", 'CMD["tail", "-f", "/dev/null"]')
    template("cmd7", "cmd", 'CMD tail - f / dev/null')


if __name__ == "__main__":
    main()
