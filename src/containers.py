from threading import RLock


class ContainerList:
    def __init__(self):
        self._lock = RLock()
        self._actions = []

    def set(self, actions):
        with self._lock:
            self._actions = actions

    def get(self):
        with self._lock:
            return self._actions.copy()


class ContainerBool:
    def __init__(self, value):
        self._lock = RLock()
        self._bool = value

    def set(self, _bool):
        with self._lock:
            self._bool = _bool

    def get(self):
        return self._bool
