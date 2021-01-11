import uploads


class Animal:
    @property
    def birth(self):
        print("I'm alive")

    def date(self):
        """Show the bith date

        Args:
            dt: date from birth animal

        Returns:
            The date

        Raises:
            DateError: If date is not set
        """


class Parrot:
    def __init__(self):
        # Composition
        self.animal = Animal()


parrot = Parrot()
parrot.animal.birth

print(uploads.__file__)
