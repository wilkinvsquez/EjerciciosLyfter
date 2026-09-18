class Student:
    def __init__(self, name, section, grades):
        self.name = name
        self.section = section
        for key, value in grades.items():
            setattr(self, key, value)

    def average(self, subject_keys):
        """Returns the average of the grades listed in subject_keys."""
        grades = [getattr(self, key) for key in subject_keys]
        return sum(grades) / len(grades)

    def failed_subjects(self, min_grade, subject_labels):
        """Returns a list of (label, grade) tuples for subjects below min_grade."""
        return [
            (label, getattr(self, key))
            for key, label in subject_labels.items()
            if getattr(self, key) < min_grade
        ]

    def matches(self, name, section):
        """Checks whether this student matches the given name and section."""
        return self.name == name and self.section == section

    def to_dict(self, subject_keys):
        """Converts the student into a flat dict (for CSV export)."""
        row = {"name": self.name, "section": self.section}
        for key in subject_keys:
            row[key] = getattr(self, key)
        return row

    @classmethod
    def from_row(cls, row, subject_keys):
        """Builds a Student from a raw CSV row (all strings)."""
        grades = {key: float(row[key]) for key in subject_keys}
        return cls(row["name"], row["section"], grades)
