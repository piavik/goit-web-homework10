import json
from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from datetime import datetime

from quotes.models import Quote, Tag, Author

filename_quotes = "quotes/static/quotes.json"
filename_authors = "quotes/static/authors.json"

class Command(BaseCommand):
    help = "Upload quotes from json to db"

    def __read_json__(self, filename, *args, **kwargs):
        try:
            with open(filename) as file:
                return json.load(file)
        except FileNotFoundError:
            raise CommandError('File "%s" not found' % filename_authors)

    def handle(self, *args, **kwargs):
        authors_data = self.__read_json__(filename_authors)
        quotes_data = self.__read_json__(filename_quotes)

        authors = []
        for author_data in authors_data:
            author_data["born_date"] = datetime.strptime(author_data['born_date'], "%B %d, %Y").date()
            authors.append(Author(**author_data))

        try: 
            Author.objects.bulk_create(authors)
        except ConnectionError:
            raise CommandError("Could not connect to database")

        all_tags = set([tag for entry in quotes_data for tag in entry['tags']])

        # one by one to catch each individual IntegrityError
        for tag in all_tags:
            try:
                Tag.objects.create(name=tag)
            except ConnectionError:
                raise CommandError("Could not connect to database")
            except IntegrityError:
                # ignore
                ...

        for quote_entry in quotes_data:
            quote_author = Author.objects.filter(fullname=quote_entry['author']).first()
            quote_tags = Tag.objects.filter(name__in=quote_entry['tags']).all()

            # Direct assignment to the forward side of a many-to-many set is prohibited.
            # Quote_id is required before making many2many relationship for tags
            # so creating DB record without tag and adding it later 
            Quote.objects.create(quote=quote_entry['quote'], author=quote_author)

            # add tags (here is "later")
            # TODO: refactor as there are too many DB operations
            quote_object = Quote.objects.filter(quote=quote_entry['quote']).first()
            quote_object.tags.set(quote_tags)
            quote_object.save()
