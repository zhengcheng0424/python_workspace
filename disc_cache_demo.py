from diskcache import Cache

if __name__ == '__main__':
    disk_cache = Cache()
    disk_cache["test"] = 1
    disk_cache["q"] = "2"
    disk_cache[3] = 33
    disk_cache[4] = ["20"]
    disk_cache.set('U', 7890)
    print(disk_cache)
    with Cache(disk_cache.directory) as c:
        print(c.get('U'))
        c.set('q', "2000")
        c.set('W', 999, expire=60)
        c.get('W', read=True, expire_time=True)
    print(disk_cache.get('u'))  # none
    print(disk_cache.get('U'))  # 7890
    print([{v: disk_cache[v]} for v in disk_cache.iterkeys()])
    print(disk_cache.get('W', read=True, expire_time=True))
    disk_cache.close()


def greet(name):
    print(f"Hello {name}!")


greet("Apple")
