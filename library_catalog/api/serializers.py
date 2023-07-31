from rest_framework import serializers
from transliterate import slugify

from library_catalog.models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'description', 'author']


    def create(self, validated_data):
        author = validated_data["author"]
        slug = slugify(validated_data["title"])

        book = Book.objects.create(title=validated_data["title"], slug=slug, description=validated_data['description'])
        book.author.set(author)
        return book

    def update(self, instance, validated_data):
        book = Book.objects.get(slug=instance.slug)

        instance.title = validated_data.get('title', instance.title)
        instance.slug = slugify(validated_data.get('title', instance.title))
        instance.description = validated_data.get('description', instance.description)
        instance.author.set(validated_data.get('author', book.author.all()))
        instance.save()

        return instance


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'bio', 'time_create']

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        slug_aut = f"{validated_data['first_name']} {validated_data['last_name']}"

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.slug = slugify(validated_data.get(slug_aut, instance.slug))
        instance.bio = validated_data.get('bio', instance.bio)
        instance.save()
        return instance
