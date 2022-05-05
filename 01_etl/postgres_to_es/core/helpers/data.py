import abc
from typing import Any

from core.helpers.storages import BaseStorage


class DbLoader:
    """Класс для работы с базой данных."""
    def __init__(self, logger=None):
        self.connection = None
        self.logger = logger

    @abc.abstractmethod
    def connect(self):
        pass


class State:
    """
    Класс для хранения состояния при работе с данными, чтобы постоянно не перечитывать данные с начала.
    Здесь представлена реализация с сохранением состояния в файл.
    В целом ничего не мешает поменять это поведение на работу с БД или распределённым хранилищем.
    """

    def __init__(self, storage: BaseStorage):
        self.storage = storage

    def set_state(self, key: str, value: Any) -> None:
        """Установить состояние для определённого ключа"""
        self.storage.save_state({key: value})

    def get_state(self, key: str) -> Any:
        """Получить состояние по определённому ключу"""
        state = self.storage.retrieve_state().get(key)
        if state:
            state = state.decode()
        return state or None
