
def test_save_and_load_experiment(tmp_path):
    original = Experiment(
        experiment_id="cake-001",
        observer="Ada",
        cake_name="Chocolate Cake",
        rating=9.5,
    )

    file_path = tmp_path / "experiment.json"

    original.save_to_file(file_path)
    loaded = Experiment.load_from_file(file_path)

    assert loaded.experiment_id == original.experiment_id
    assert loaded.observer == original.observer
    assert loaded.cake_name == original.cake_name
    assert loaded.rating == original.rating
