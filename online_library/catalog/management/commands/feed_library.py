from django.core.management.base import BaseCommand
from django.db import transaction
from catalog.models import Author, Publisher, Book
import random
from datetime import date

class Command(BaseCommand):
    help = "Seed the database with demo data for the online_library project."

    def add_arguments(self, parser):
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Flush related tables before seeding (deletes existing Authors/Publishers/Books).",
        )
        parser.add_argument(
            "--seed",
            type=int,
            default=42,
            help="Random seed for reproducibility (default: 42).",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        rnd_seed = options["seed"]
        random.seed(rnd_seed)

        if options["reset"]:
            self.stdout.write(self.style.WARNING("Deleting existing data…"))
            Book.objects.all().delete()
            Author.objects.all().delete()
            Publisher.objects.all().delete()

        if Author.objects.exists() or Publisher.objects.exists() or Book.objects.exists():
            self.stdout.write(self.style.WARNING(
                "Some data already exists. Use --reset to start clean, "
                "or proceed to augment the current dataset."
            ))

        self.stdout.write(self.style.MIGRATE_HEADING(f"Seeding with seed={rnd_seed}…"))

        # ---------- AUTHORS ----------
        first_names = ["Jane", "John", "Alice", "Bob", "Eva", "Michael", "Sophia", "Liam", "Olivia", "Noah",
                       "Emma", "William", "Ava", "James", "Isabella", "Benjamin", "Mia", "Elijah", "Charlotte", "Lucas"]
        last_names = ["Doe", "Smith", "Johnson", "Williams", "Brown", "Miller", "Davis", "Wilson", "Moore", "Taylor",
                      "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson"]

        authors_data = []
        while len(authors_data) < 70:
            name = f"{random.choice(first_names)} {random.choice(last_names)}"
            age = random.randint(25, 75)
            if (name, age) not in authors_data:  # unikaj duplikatów
                authors_data.append((name, age))

        authors = [Author(name=n, age=a) for n, a in authors_data]
        Author.objects.bulk_create(authors)
        authors = list(Author.objects.all().order_by("id"))

        # ---------- PUBLISHERS ----------
        publisher_names = [
            "Penguin Random House", "HarperCollins", "Simon & Schuster", "Hachette Book Group",
            "Macmillan Publishers", "Scholastic", "Bloomsbury", "Oxford University Press",
            "Cambridge University Press", "Pearson", "Springer", "Wiley", "Routledge",
            "SAGE Publications", "McGraw-Hill Education", "Cengage Learning", "Faber & Faber",
            "Kensington Publishing", "Houghton Mifflin Harcourt", "Grosset & Dunlap",
            "Tor Books", "Chronicle Books", "Sourcebooks", "W. W. Norton & Company",
            "DK Publishing", "Workman Publishing", "Algonquin Books", "Abrams Books", "Graywolf Press",
            "Europa Editions", "Atlantic Books", "Taschen", "Harlequin", "Quercus Publishing",
            "Orion Publishing", "Pan Macmillan", "Farrar, Straus and Giroux", "Little, Brown and Company",
            "Viking Press", "Knopf", "Chronicle Publishing", "Thames & Hudson", "Oxford Press",
            "Cambridge Press", "Pearson Longman", "Springer Nature", "Wiley-Blackwell", "Routledge Taylor",
            "Scribner"
        ]
        publishers = [Publisher(name=n) for n in publisher_names]
        Publisher.objects.bulk_create(publishers)
        publishers = list(Publisher.objects.all().order_by("id"))

        # ---------- BOOKS ----------
        titles = [
            "The Last Horizon", "Whispers of Time", "Journey Through Shadows", "The Hidden Path",
            "Echoes of Eternity", "The Silent Watcher", "Fragments of Light", "Beneath the Stars",
            "The Forgotten Garden", "Shadows of the Mind", "The Crimson Tide", "Winds of Destiny",
            "The Lost Chronicle", "Reflections of the Heart", "A Dance with Fate", "Beyond the Veil",
            "The Secret Keeper", "Whispers in the Dark", "Threads of Tomorrow", "The Golden Compass",
            "The Moonlit Road", "A World Apart", "The Endless Sea", "Voices of the Past", "Shattered Dreams",
            "The Emerald Flame", "Journey of Souls", "The Winter's Tale", "The Sapphire Key", "The Hidden Realm",
            "Twilight Memories", "The Iron Crown", "Echoes of Silence", "The Mystic River", "Fallen Kingdoms",
            "The Whispering Wind", "Secrets of the Forest", "The Silver Locket", "Beyond the Horizon",
            "The Shadowed Gate", "A Light in the Darkness", "The Forgotten Temple", "Tides of Change",
            "The Phoenix Reborn", "The Last Voyage", "Whispers of the Heart", "The Enchanted Grove",
            "The Crystal Lake", "Paths of Glory", "The Midnight Hour", "The Lost Legacy", "The Endless Journey",
            "The Secret of Shadows", "Dreams of Fire", "The Hidden Truth", "Voices from Afar", "The Final Chapter",
            "Beneath the Moon", "The Crimson Mask", "The Silent Promise", "Winds of Change", "The Golden Horizon",
            "The Emerald Key", "Tales of the Forgotten", "The Last Guardian", "Echoes of Destiny",
            "The Hidden Song", "Shattered Stars", "The Mystic Crown", "A Journey Beyond", "The Silent Forest",
            "The Secret Path", "Whispers of the Night", "The Shadowed Heart", "The Endless Flame",
            "The Crystal Gate", "The Last Enchantment", "Voices of Light", "The Hidden Mirror",
            "Fragments of Time", "The Golden Phoenix", "Beyond the Shadows", "The Forgotten Realm",
            "The Silent Tide", "The Crimson Rose", "Journey into Darkness", "The Hidden Key",
            "The Mystic Lake", "Whispers of Eternity", "The Last Dream", "Echoes of the Past",
            "The Hidden Chronicle", "The Golden Path", "Shadows of Eternity", "The Crystal Crown",
            "The Silent Horizon", "The Forgotten Journey", "Voices in the Mist", "The Hidden Flame"
        ]

        books = []

        def random_pubdate():
            year = random.choice([2019, 2020, 2021, 2022, 2023, 2024, 2025])
            month = random.randint(1, 12)
            day = random.randint(1, 28)
            return date(year, month, day)

        for t in titles:
            pages = random.randint(120, 900)
            price = round(random.uniform(39.0, 279.0), 2)
            rating = round(random.uniform(2.5, 5.0), 1)
            publisher = random.choice(publishers)
            pubdate = random_pubdate()
            available_copies = random.randint(1, 10)
            category = random.choice(['novel','drama','comedy','romance','diary','science fiction','fantasy'])
            books.append(Book(
                name=t,
                pages=pages,
                price=price,
                rating=rating,
                publisher=publisher,
                pubdate=pubdate,
                available_copies=available_copies,
                category=category
            ))

        Book.objects.bulk_create(books)
        books = list(Book.objects.all().order_by("id"))

        for b in books:
            k = random.choice([1, 1, 2, 2, 3])  # częściej 1–2 autorów
            b.authors.add(*random.sample(authors, k))

        self.stdout.write(self.style.SUCCESS("Seeding complete!\n"))
        self.stdout.write(f"Authors:    {Author.objects.count()}")
        self.stdout.write(f"Publishers: {Publisher.objects.count()}")
        self.stdout.write(f"Books:      {Book.objects.count()}")

        self.stdout.write("\nExample checks:")
        self.stdout.write(f"- Any book rated >= 4.5? {Book.objects.filter(rating__gte=4.5).exists()}")
        self.stdout.write(f"- Cheap books (< 30 PLN): {Book.objects.filter(price__lt=30).count()}")
        self.stdout.write(f"- Books published in 2024: {Book.objects.filter(pubdate__year=2024).count()}")
