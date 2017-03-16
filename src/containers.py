from threading import RLock


class ContainerList:
    def __init__(self):
        self._lock = RLock()
        self._actions = []
        self._depth = 0
        self._score = float('-inf')

    def smart_set(self, actions, depth, score):
        if score > self._score or (score == self._score and depth < self._depth):
            with self._lock:
                self._actions = actions
                self._depth = depth
                self._score = score
            print('containerList: SMART SET setting actions with score and depth', self._actions, self._score, self._depth)
        else:
            print('containerList: SMART SET action was not good enough')

    def set(self, actions):
        with self._lock:
            self._actions = actions
        print('containerList: setting actions', self._actions)

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
