import os
import pickle
import random
import typing as tp

from sklearn import datasets, tree


class TemplateModel:
    def __init__(self, model_filepath: str) -> None:
        model_filepath = self._get_absolute_path(model_filepath)
        if os.path.exists(model_filepath):
            self._load_model(model_filepath)
        else:
            self._train_model()
            self._save_model(model_filepath)

    def predict_model(self, input_data: tp.List[float]) -> float:
        return self._model.predict([input_data])

    @staticmethod
    def _get_absolute_path(model_filepath: str) -> str:
        if not os.path.isabs(model_filepath):
            module_path = os.path.dirname(os.path.abspath(__file__))
            model_filepath = os.path.join(module_path, model_filepath)
        return model_filepath

    def _load_model(self, path: str) -> None:
        with open(path, "rb") as file:
            self._model = pickle.load(file)

    def _train_model(self):
        iris_df = datasets.load_iris()
        X_train, y_train = iris_df.data, iris_df.target
        self._model = tree.DecisionTreeClassifier()
        self._model.fit(X_train, y_train)

    def _save_model(self, path: str) -> None:
        with open(path, "w+b") as model_file:
            pickle.dump(self._model, model_file)

    @staticmethod
    def _get_random_model_time(min_time, max_time):
        random_ms = random.uniform(min_time, max_time)
        return random_ms
