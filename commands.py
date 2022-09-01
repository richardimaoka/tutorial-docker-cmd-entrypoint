
# # CMD ["echo", "abc"]

def template(comment, suffix, category) -> str:
    str = """
# {comment}
docker build -t {suffix} -f Dockerfile.{suffix} .
docker images --filter=reference='{category}*'
docker run cmd1
docker inspect cmd1 --format='CMD {{.Config.Cmd}}'
""".format(comment=comment, suffix=suffix, category=category).strip()

    print(str)


def main():
    template(suffix="cmd1", category="cmd", comment='CMD ["echo", "abc"]')
    template(suffix="cmd1", category="cmd", comment='CMD ["echo", "abc"]')


if __name__ == "__main__":
    main()
